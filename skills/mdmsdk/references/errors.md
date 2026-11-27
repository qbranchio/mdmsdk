# Error codes

| Status | Code | Meaning | Retried |
|---|---|---|---|
| 400 | `bad_request` | the body could not be decoded | no |
| 400 | `invalid_parameter` | a path or query parameter is malformed | no |
| 400 | `invalid_cursor` | a page cursor is not for this request | no |
| 401 | `unauthorized` | the token is missing, wrong, or expired | no |
| 403 | `insufficient_scope` | an account client lacks the scope | no |
| 403 | `insufficient_permission` | a delegated token lacks the permission | no |
| 403 | `not_delegable` | the operation is not open to delegated tokens | no |
| 403 | `needs_all` | the operation needs a token that reaches the whole tenant | no |
| 404 | `not_found` | absent, removed, or outside the caller's reach | no |
| 409 | `conflict` | a unique value is taken, or the device's state does not allow it | no |
| 409 | `idempotency_in_flight` | the same Idempotency-Key is still running | yes |
| 409 | `tenant_deleting` | the tenant is being deleted | no |
| 409 | `licence_exceeded` | a device, tenant, or people limit | no |
| 409 | `licence_expired` | the tenant's licence has ended | no |
| 422 | `validation_failed` | the body fails validation; `errors` names the fields | no |
| 422 | `idempotency_key_reused` | the key was used with another request | no |
| 429 | `rate_limited` | over the rate limit; wait `Retry-After` | yes |
| 503 | `auth0_unavailable` | the identity provider could not be reached | yes |
| 503 | `admin_app_unavailable` | not configured on the server | no |
