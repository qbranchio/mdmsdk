// Package mdmsdk is the Go client for the mdm API: tenants, members,
// groups, devices, profiles, and commands for Apple devices.
//
// It authenticates as an account client (Auth0 client credentials) or with
// a delegated token, retries what is safe to retry with a stable
// Idempotency-Key, decodes RFC 9457 problems into typed errors, and verifies
// Standard Webhooks signatures.
//
// The surface is generated from openapi/openapi.yaml and methods.yaml; the
// behavior is specified once in scenarios/ and tested here and in the Python
// SDK. See AGENTS.md before changing anything.
package mdmsdk
