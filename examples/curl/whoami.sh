#!/bin/sh
# Who am I: an account client token, then me and the supervised catalog.
set -eu
token=$(curl -sf https://id.enroll.dev/oauth/token \
  -d grant_type=client_credentials -d audience=https://enroll.dev/api \
  -d client_id="$MDM_CLIENT_ID" -d client_secret="$MDM_CLIENT_SECRET" | jq -r .access_token)
curl -sf https://enroll.dev/api/v1/me -H "Authorization: Bearer $token"
curl -sf "https://enroll.dev/api/v1/catalog?level=supervised" -H "Authorization: Bearer $token" | jq '.entries | length'
