// Who am I: configure an account client, call me, list the supervised
// catalog, and handle an error by its code.
package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"os"

	"github.com/qbranchio/mdmsdk"
	"github.com/qbranchio/mdmsdk/api"
)

func main() {
	ctx := context.Background()
	client, err := mdmsdk.New(mdmsdk.WithClientCredentials(os.Getenv("MDM_CLIENT_ID"), os.Getenv("MDM_CLIENT_SECRET")))
	if err != nil {
		log.Fatal(err)
	}

	me, err := client.Me.Get(ctx)
	var apiErr *mdmsdk.Error
	switch {
	case errors.As(err, &apiErr) && apiErr.Code == "insufficient_scope":
		log.Fatalf("the client lacks a scope: %s (%s)", apiErr.Detail, apiErr.Instance)
	case err != nil:
		log.Fatal(err)
	}
	fmt.Println("caller:", me.Kind)

	level := api.GetCatalogParamsLevelSupervised
	catalog, err := client.Catalog.Get(ctx, &api.GetCatalogParams{Level: &level})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("settings for supervised devices:", len(catalog.Entries))
}
