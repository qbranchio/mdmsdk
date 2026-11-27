package webhooks

import (
	"context"
	"net/http"
	"net/http/httptest"
	"strconv"
	"strings"
	"testing"
	"time"

	standardwebhooks "github.com/standard-webhooks/standard-webhooks/libraries/go"

	"github.com/qbranchio/mdmsdk/api"
)

const (
	secretNew = "whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw"
	secretOld = "whsec_C2FVsBQIhrscChlQIMV+b5sSYspob7oD"
	body      = `{"type":"tenant.deleted","timestamp":"2026-11-27T00:00:00Z","data":{"tenant_id":"00000000-0000-4000-8000-0000000000a1","tenant_external_id":null}}`
)

// signed returns headers carrying a signature per secret, as the server
// sends during a rotation.
func signed(t *testing.T, at time.Time, secrets ...string) http.Header {
	t.Helper()
	h := http.Header{}
	h.Set("webhook-id", "msg_1")
	h.Set("webhook-timestamp", strconv.FormatInt(at.Unix(), 10))
	var sigs []string
	for _, s := range secrets {
		wh, err := standardwebhooks.NewWebhook(s)
		if err != nil {
			t.Fatal(err)
		}
		sig, err := wh.Sign("msg_1", at, []byte(body))
		if err != nil {
			t.Fatal(err)
		}
		sigs = append(sigs, sig)
	}
	h.Set("webhook-signature", strings.Join(sigs, " "))
	return h
}

func TestVerify(t *testing.T) {
	now := time.Now()
	for _, tt := range []struct {
		name    string
		hold    []string
		signed  []string
		at      time.Time
		wantErr bool
	}{
		{"one secret", []string{secretNew}, []string{secretNew}, now, false},
		{"rotation: receiver holds the new secret", []string{secretNew}, []string{secretNew, secretOld}, now, false},
		{"rotation: receiver still holds the old secret", []string{secretOld}, []string{secretNew, secretOld}, now, false},
		{"receiver holds both, server signs with one", []string{secretNew, secretOld}, []string{secretOld}, now, false},
		{"wrong secret", []string{secretNew}, []string{secretOld}, now, true},
		{"stale timestamp", []string{secretNew}, []string{secretNew}, now.Add(-time.Hour), true},
	} {
		t.Run(tt.name, func(t *testing.T) {
			v, err := New(tt.hold...)
			if err != nil {
				t.Fatal(err)
			}
			err = v.Verify([]byte(body), signed(t, tt.at, tt.signed...))
			if (err != nil) != tt.wantErr {
				t.Fatalf("Verify: %v, want error %v", err, tt.wantErr)
			}
		})
	}
}

func TestHandler(t *testing.T) {
	v, err := New(secretNew)
	if err != nil {
		t.Fatal(err)
	}
	var got any
	h := v.Handler(func(_ context.Context, id string, e api.WebhookEvent) error {
		if id != "msg_1" {
			t.Errorf("id %q", id)
		}
		got, err = e.ValueByDiscriminator()
		return err
	})
	req := httptest.NewRequestWithContext(t.Context(), http.MethodPost, "/hooks", strings.NewReader(body))
	req.Header = signed(t, time.Now(), secretNew)
	rec := httptest.NewRecorder()
	h.ServeHTTP(rec, req)
	if rec.Code != http.StatusNoContent {
		t.Fatalf("status %d: %s", rec.Code, rec.Body)
	}
	if _, ok := got.(api.TenantDeletedEvent); !ok {
		t.Fatalf("decoded %T, want api.TenantDeletedEvent", got)
	}

	req = httptest.NewRequestWithContext(t.Context(), http.MethodPost, "/hooks", strings.NewReader(body))
	req.Header = signed(t, time.Now(), secretOld)
	rec = httptest.NewRecorder()
	h.ServeHTTP(rec, req)
	if rec.Code != http.StatusUnauthorized {
		t.Fatalf("status %d, want 401", rec.Code)
	}
}
