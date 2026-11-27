// Package webhooks verifies and decodes the mdm API's webhook deliveries.
//
// Deliveries are signed per Standard Webhooks 1.0: headers webhook-id,
// webhook-timestamp, and webhook-signature, HMAC-SHA256 with the endpoint's
// whsec_ secret. During a secret rotation the server signs with both the new
// and the previous secret for 24 hours, so a receiver can hold either.
//
// Receiver rules: verify the raw body before parsing it, answer 2xx within
// 10 s and do the work after, deduplicate on webhook-id, and know that 410
// disables the endpoint.
package webhooks

import (
	"context"
	"errors"
	"fmt"
	"io"
	"net/http"

	standardwebhooks "github.com/standard-webhooks/standard-webhooks/libraries/go"

	"github.com/qbranchio/mdmsdk/api"
)

// MaxBody bounds the body Handler reads.
const MaxBody = 1 << 20

// ErrSignature means no secret verified the delivery, or its timestamp is
// outside the tolerance.
var ErrSignature = errors.New("webhooks: signature does not verify")

// Verifier checks deliveries against one or more endpoint secrets.
type Verifier struct {
	hooks []*standardwebhooks.Webhook
}

// New builds a Verifier from the endpoint's secret (whsec_...). Pass the
// previous secret too while a rotation is under way.
func New(secrets ...string) (*Verifier, error) {
	if len(secrets) == 0 {
		return nil, errors.New("webhooks: no secret")
	}
	v := &Verifier{}
	for _, s := range secrets {
		h, err := standardwebhooks.NewWebhook(s)
		if err != nil {
			return nil, fmt.Errorf("webhooks: secret: %w", err)
		}
		v.hooks = append(v.hooks, h)
	}
	return v, nil
}

// Verify checks the raw body and headers of a delivery.
func (v *Verifier) Verify(body []byte, header http.Header) error {
	for _, h := range v.hooks {
		if h.Verify(body, header) == nil {
			return nil
		}
	}
	return ErrSignature
}

// Parse decodes a verified body into an event. Switch on the result of
// event.ValueByDiscriminator() to get the typed event.
func Parse(body []byte) (api.WebhookEvent, error) {
	var e api.WebhookEvent
	if err := e.UnmarshalJSON(body); err != nil {
		return api.WebhookEvent{}, fmt.Errorf("webhooks: %w", err)
	}
	return e, nil
}

// Handler verifies, parses, and passes each delivery to fn. It answers 204
// when fn returns nil, 401 when the signature does not verify, 400 when the
// body is not an event, and 500 when fn fails (the server retries).
func (v *Verifier) Handler(fn func(ctx context.Context, id string, event api.WebhookEvent) error) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		body, err := io.ReadAll(io.LimitReader(r.Body, MaxBody+1))
		if err != nil || len(body) > MaxBody {
			http.Error(w, "body too large or unreadable", http.StatusBadRequest)
			return
		}
		if err := v.Verify(body, r.Header); err != nil {
			http.Error(w, "signature does not verify", http.StatusUnauthorized)
			return
		}
		event, err := Parse(body)
		if err != nil {
			http.Error(w, "not an event", http.StatusBadRequest)
			return
		}
		if err := fn(r.Context(), r.Header.Get("webhook-id"), event); err != nil {
			http.Error(w, "handler failed", http.StatusInternalServerError)
			return
		}
		w.WriteHeader(http.StatusNoContent)
	})
}
