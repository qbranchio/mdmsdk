// A webhook receiver: verify the raw body, answer 2xx at once, work after,
// and deduplicate on webhook-id.
package main

import (
	"context"
	"log"
	"net/http"
	"os"
	"sync"
	"time"

	"github.com/qbranchio/mdmsdk/api"
	"github.com/qbranchio/mdmsdk/webhooks"
)

func main() {
	// The endpoint's secret; add the previous one while a rotation is under way.
	v, err := webhooks.New(os.Getenv("MDM_WEBHOOK_SECRET"))
	if err != nil {
		log.Fatal(err)
	}
	var seen sync.Map
	work := make(chan api.WebhookEvent, 64)
	go func() {
		for e := range work {
			switch ev, _ := e.ValueByDiscriminator(); ev := ev.(type) {
			case api.DeviceEnrolledEvent:
				log.Printf("device %s enrolled in tenant %s", ev.Data.DeviceId, ev.Data.TenantId)
			case api.CommandCompletedEvent:
				log.Printf("command %s (%s): %s", ev.Data.CommandUuid, ev.Data.RequestType, ev.Data.Status)
			default:
				log.Printf("event %T", ev)
			}
		}
	}()
	handler := v.Handler(func(_ context.Context, id string, e api.WebhookEvent) error {
		if _, dup := seen.LoadOrStore(id, struct{}{}); !dup {
			work <- e
		}
		return nil
	})
	srv := &http.Server{Addr: ":8080", Handler: handler, ReadHeaderTimeout: 5 * time.Second}
	log.Fatal(srv.ListenAndServe())
}
