package mdmsdk

import (
	"bytes"
	"context"
	"crypto/rand"
	"encoding/hex"
	"encoding/json"
	"io"
	"math"
	mrand "math/rand/v2"
	"net/http"
	"strconv"
	"time"

	"github.com/cenkalti/backoff/v5"
)

// opInfo is what the transport knows about the operation a request belongs to.
type opInfo struct {
	id string
	// idempotent: the operation declares Idempotency-Key and stores responses.
	idempotent bool
	// retryTransport: a POST that may be retried on transport errors and 429 (createToken).
	retryTransport bool
}

type opKey struct{}

func withOp(ctx context.Context, op opInfo) context.Context {
	return context.WithValue(ctx, opKey{}, op)
}

type keyKey struct{}

// WithIdempotencyKey makes a write use key instead of one the SDK generates.
// A retry of the same logical call must reuse the same key and body.
func WithIdempotencyKey(ctx context.Context, key string) context.Context {
	return context.WithValue(ctx, keyKey{}, key)
}

// retryPolicy bounds retries: at most attempts, exponential backoff from
// initial with full jitter, each wait capped at maxWait, all of them within
// total, and Retry-After honored up to maxRetryAfter.
type retryPolicy struct {
	attempts      int
	initial       time.Duration
	maxWait       time.Duration
	total         time.Duration
	maxRetryAfter time.Duration
	sleep         func(context.Context, time.Duration) error
	jitter        func() float64
}

var defaultRetry = retryPolicy{attempts: 6, initial: 500 * time.Millisecond, maxWait: 15 * time.Second,
	total: 90 * time.Second, maxRetryAfter: 60 * time.Second, sleep: sleepCtx, jitter: mrand.Float64}

func sleepCtx(ctx context.Context, d time.Duration) error {
	t := time.NewTimer(d)
	defer t.Stop()
	select {
	case <-ctx.Done():
		return ctx.Err()
	case <-t.C:
		return nil
	}
}

// doer is the low-level client's HTTP doer: auth, Mdm-Actor, the
// idempotency key, and retries.
type doer struct{ c *Client }

func (d doer) Do(req *http.Request) (*http.Response, error) {
	c := d.c
	ctx := req.Context()
	op, _ := ctx.Value(opKey{}).(opInfo)
	var body []byte
	if req.Body != nil {
		var err error
		if body, err = io.ReadAll(req.Body); err != nil {
			return nil, err
		}
		_ = req.Body.Close()
	}
	key, _ := ctx.Value(keyKey{}).(string)
	if op.idempotent && key == "" {
		key = newKey()
	}
	bo := backoff.NewExponentialBackOff()
	bo.InitialInterval, bo.MaxInterval, bo.Multiplier, bo.RandomizationFactor = c.retry.initial, c.retry.maxWait, 2, 0
	start := time.Now()
	waited := time.Duration(0)
	for attempt := 1; ; attempt++ {
		r := req.Clone(ctx)
		if body != nil {
			r.Body = io.NopCloser(bytes.NewReader(body))
			r.ContentLength = int64(len(body))
		}
		tok, err := c.tokens.Token()
		if err != nil {
			return nil, err
		}
		tok.SetAuthHeader(r)
		if c.actor != "" {
			r.Header.Set("Mdm-Actor", c.actor)
		}
		if key != "" {
			r.Header.Set("Idempotency-Key", key)
		}
		ua := "mdmsdk-go/" + Version
		if c.userAgent != "" {
			ua = c.userAgent + " " + ua
		}
		r.Header.Set("User-Agent", ua)

		resp, err := c.http.Do(r)
		var wait time.Duration
		retry := false
		switch {
		case err != nil:
			if ctx.Err() != nil {
				return nil, ctx.Err()
			}
			retry = retryable(r.Method, op, 0, "")
		default:
			var code string
			code, resp = peekCode(resp)
			retry = retryable(r.Method, op, resp.StatusCode, code)
			wait = retryAfter(resp, c.retry.maxRetryAfter)
		}
		// A retried DELETE that answers 404: an earlier attempt deleted it.
		if err == nil && attempt > 1 && r.Method == http.MethodDelete && resp.StatusCode == http.StatusNotFound {
			_ = resp.Body.Close()
			resp.StatusCode, resp.Status = http.StatusNoContent, "204 No Content"
			resp.Body, resp.ContentLength = http.NoBody, 0
			resp.Header = http.Header{}
			return resp, nil
		}
		if !retry || attempt >= c.retry.attempts {
			return resp, err
		}
		if wait == 0 {
			// Full jitter over the exponential step.
			step := bo.NextBackOff()
			wait = time.Duration(c.retry.jitter() * float64(step))
		}
		if time.Since(start)+waited+wait > c.retry.total {
			return resp, err
		}
		if resp != nil {
			_, _ = io.Copy(io.Discard, resp.Body)
			_ = resp.Body.Close()
		}
		if err := c.retry.sleep(ctx, wait); err != nil {
			return nil, err
		}
		waited += wait
	}
}

// retryable is the retry table of the SDK spec.
func retryable(method string, op opInfo, status int, code string) bool {
	transient := status == 0 || status == http.StatusTooManyRequests || status == http.StatusBadGateway ||
		status == http.StatusGatewayTimeout || (status == http.StatusServiceUnavailable && code != "admin_app_unavailable")
	switch method {
	case http.MethodGet, http.MethodHead, http.MethodPut, http.MethodDelete:
		return transient
	case http.MethodPost:
		if op.idempotent {
			return transient || (status == http.StatusConflict && code == "idempotency_in_flight")
		}
		if op.retryTransport {
			return status == 0 || status == http.StatusTooManyRequests
		}
	}
	return false
}

// peekCode reads a problem's code and gives back a response whose body can
// still be read.
func peekCode(resp *http.Response) (string, *http.Response) {
	if resp.StatusCode < 400 {
		return "", resp
	}
	raw, err := io.ReadAll(io.LimitReader(resp.Body, 1<<20))
	_ = resp.Body.Close()
	resp.Body = io.NopCloser(bytes.NewReader(raw))
	if err != nil {
		return "", resp
	}
	var p struct {
		Code string `json:"code"`
	}
	_ = json.Unmarshal(raw, &p)
	return p.Code, resp
}

func retryAfter(resp *http.Response, limit time.Duration) time.Duration {
	v := resp.Header.Get("Retry-After")
	if v == "" {
		return 0
	}
	secs, err := strconv.Atoi(v)
	if err != nil || secs < 0 {
		return 0
	}
	d := time.Duration(secs) * time.Second
	return time.Duration(math.Min(float64(d), float64(limit)))
}

func newKey() string {
	b := make([]byte, 16)
	_, _ = rand.Read(b)
	return hex.EncodeToString(b)
}

func orEmpty[T any](p *T) *T {
	if p == nil {
		return new(T)
	}
	return p
}
