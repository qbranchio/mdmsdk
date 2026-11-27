package mdmsdk

import (
	"bytes"
	"context"
	"encoding/json"
	"errors"
	"io"
	"net/http"
	"path/filepath"
	"sync"
	"testing"
	"time"

	"github.com/qbranchio/mdmsdk/api"
)

type scenario struct {
	Name string `yaml:"name"`
	Call struct {
		Operation      string         `yaml:"operation"`
		Args           map[string]any `yaml:"args"`
		IdempotencyKey *string        `yaml:"idempotency_key"`
	} `yaml:"call"`
	Responses []struct {
		Status  int               `yaml:"status"`
		Headers map[string]string `yaml:"headers"`
		Body    any               `yaml:"body"`
	} `yaml:"responses"`
	Expect struct {
		Attempts             int            `yaml:"attempts"`
		SameIdempotencyKey   *bool          `yaml:"same_idempotency_key"`
		WaitedAtLeastSeconds float64        `yaml:"waited_at_least_seconds"`
		Result               any            `yaml:"result"`
		Error                map[string]any `yaml:"error"`
	} `yaml:"expect"`
}

// scripted serves a scenario's responses in order and records the requests.
type scripted struct {
	mu   sync.Mutex
	s    scenario
	reqs []*http.Request
}

func (t *scripted) RoundTrip(r *http.Request) (*http.Response, error) {
	t.mu.Lock()
	defer t.mu.Unlock()
	i := len(t.reqs)
	t.reqs = append(t.reqs, r)
	if i >= len(t.s.Responses) {
		return nil, errors.New("scenario: more requests than scripted responses")
	}
	sr := t.s.Responses[i]
	var body []byte
	switch b := sr.Body.(type) {
	case string:
		body = []byte(b)
	case nil:
	default:
		body, _ = json.Marshal(b)
	}
	h := http.Header{}
	for k, v := range sr.Headers {
		h.Set(k, v)
	}
	return &http.Response{StatusCode: sr.Status, Header: h, Body: io.NopCloser(bytes.NewReader(body)), Request: r}, nil
}

// calls runs a scenario's operation. Every operation in methods.yaml that a
// scenario uses needs an entry.
var calls = map[string]func(ctx context.Context, c *Client, args map[string]any) (any, error){
	"getMe": func(ctx context.Context, c *Client, _ map[string]any) (any, error) { return c.Me.Get(ctx) },
	"getCatalog": func(ctx context.Context, c *Client, args map[string]any) (any, error) {
		p := &api.GetCatalogParams{}
		if l, ok := args["level"].(string); ok {
			lv := api.GetCatalogParamsLevel(l)
			p.Level = &lv
		}
		return c.Catalog.Get(ctx, p)
	},
}

func TestScenarios(t *testing.T) {
	files, err := filepath.Glob(filepath.Join("scenarios", "*.yaml"))
	if err != nil || len(files) == 0 {
		t.Fatal("no scenarios")
	}
	for _, f := range files {
		var s scenario
		read(t, f, &s)
		t.Run(s.Name, func(t *testing.T) {
			tr := &scripted{s: s}
			var waited time.Duration
			c, err := New(WithToken("t"), WithBaseURL("https://api.test"), WithHTTPClient(&http.Client{Transport: tr}))
			if err != nil {
				t.Fatal(err)
			}
			c.retry.sleep = func(_ context.Context, d time.Duration) error { waited += d; return nil }
			c.retry.jitter = func() float64 { return 0.5 }
			call, ok := calls[s.Call.Operation]
			if !ok {
				t.Fatalf("no call for %s", s.Call.Operation)
			}
			ctx := context.Background()
			if s.Call.IdempotencyKey != nil {
				ctx = WithIdempotencyKey(ctx, *s.Call.IdempotencyKey)
			}
			got, err := call(ctx, c, s.Call.Args)
			if len(tr.reqs) != s.Expect.Attempts {
				t.Errorf("attempts: got %d, want %d", len(tr.reqs), s.Expect.Attempts)
			}
			if s.Expect.WaitedAtLeastSeconds > 0 && waited < time.Duration(s.Expect.WaitedAtLeastSeconds*float64(time.Second)) {
				t.Errorf("waited %v, want at least %vs", waited, s.Expect.WaitedAtLeastSeconds)
			}
			if s.Expect.SameIdempotencyKey != nil {
				keys := map[string]bool{}
				for _, r := range tr.reqs {
					keys[r.Header.Get("Idempotency-Key")] = true
				}
				if *s.Expect.SameIdempotencyKey && (len(keys) != 1 || keys[""]) {
					t.Errorf("idempotency keys across attempts: %v", keys)
				}
			}
			if s.Expect.Error != nil {
				var e *Error
				if !errors.As(err, &e) {
					t.Fatalf("want an *Error, got %v", err)
				}
				want := s.Expect.Error
				if string(e.Kind) != want["kind"] || e.Code != want["code"] || float64(e.Status) != toFloat(want["status"]) {
					t.Errorf("error: got kind=%s code=%q status=%d, want %v", e.Kind, e.Code, e.Status, want)
				}
				if inst, ok := want["instance"].(string); ok && e.Instance != inst {
					t.Errorf("instance: got %q, want %q", e.Instance, inst)
				}
				return
			}
			if err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			gotJSON, _ := json.Marshal(got)
			wantJSON, _ := json.Marshal(s.Expect.Result)
			var g, w any
			_ = json.Unmarshal(gotJSON, &g)
			_ = json.Unmarshal(wantJSON, &w)
			if !jsonEqual(g, w) {
				t.Errorf("result: got %s, want %s", gotJSON, wantJSON)
			}
		})
	}
}

func toFloat(v any) float64 {
	switch n := v.(type) {
	case int:
		return float64(n)
	case float64:
		return n
	}
	return -1
}

func jsonEqual(a, b any) bool {
	x, _ := json.Marshal(a)
	y, _ := json.Marshal(b)
	return bytes.Equal(x, y)
}
