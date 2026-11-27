# Scenarios

Behavior both SDKs must show, written once. Each file is one case: a call, the responses a mock transport returns in order, and what the SDK must do. The Go and Python test suites replay every file.

```yaml
name: short sentence
call:
  operation: getMe          # an operationId from methods.yaml
  args: {}                  # path, query, and body arguments by name
  idempotency_key: null     # a caller-supplied key, or null for the SDK's own
responses:                  # served in order, one per attempt
  - status: 503
    headers: {Retry-After: "0"}
    body: {...}             # JSON; a string for a non-JSON body
expect:
  attempts: 2               # requests sent
  same_idempotency_key: true   # every attempt carried the same key (writes only)
  result: {...}             # the decoded result, or
  error: {kind: NotFound, code: not_found, status: 404}
```

Error kinds: BadRequest, Unauthorized, Forbidden, NotFound, Conflict, Validation, RateLimited, Unavailable, Server, Unexpected.
