// Delegated tokens: your backend issues a short-lived token for one of your
// users, limited to their members and the permissions they need, and that
// user's client calls the API with it.
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/qbranchio/mdmsdk"
	"github.com/qbranchio/mdmsdk/api"
)

func main() {
	ctx := context.Background()
	backend, err := mdmsdk.New(mdmsdk.WithClientCredentials(os.Getenv("MDM_CLIENT_ID"), os.Getenv("MDM_CLIENT_SECRET")))
	if err != nil {
		log.Fatal(err)
	}

	// After your own checks: this user may see and lock their kids' devices.
	members := []string{"ext:crm-41", "ext:crm-42"}
	tok, err := backend.Tokens.Create(ctx, api.TokenRequest{
		Tenant:      "ext:family-7",
		Subject:     "user-123",
		Members:     &members,
		Permissions: []api.TokenRequestPermissions{api.TokenRequestPermissionsDevicesRead, api.TokenRequestPermissionsCommandsWrite},
	})
	if err != nil {
		log.Fatal(err)
	}

	// The user's client: at most 900 s, never refreshed; ask the backend again.
	user, err := mdmsdk.New(mdmsdk.WithToken(tok.AccessToken))
	if err != nil {
		log.Fatal(err)
	}
	for d, err := range user.Devices.List(ctx, "ext:family-7", nil) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(d.Name)
	}
}
