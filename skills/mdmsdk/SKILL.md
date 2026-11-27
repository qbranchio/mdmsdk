---
name: mdmsdk
description: Use when writing code that calls the mdm API (Apple device management: tenants, members, groups, devices, profiles, commands, webhooks) from Go or Python, or when the user mentions mdmsdk, enroll.dev, delegated tokens, or MDM tenants. Covers setup, auth choice, the call pattern, errors, retries, and the rules that are easy to get wrong.
---

# mdmsdk

Go: `go get github.com/qbranchio/mdmsdk`. Python: `pip install mdmsdk` (3.11+).

## Choose the credential

| Caller | Use | Reaches |
|---|---|---|
| Your backend | account client: `client_id` + `client_secret` | every tenant of your account, limited by the client's scopes |
| One of your users, from your backend or a browser | delegated token from `tokens.create` | one tenant, its listed members or groups or all of it, the listed permissions, at most 900 s |

Admin app, console, and platform sign-ins are not SDK callers.

## Set up

Go:

```go
client, err := mdmsdk.New(mdmsdk.WithClientCredentials(id, secret)) // production defaults
// mdmsdk.WithToken(delegated), mdmsdk.WithActor(userID), mdmsdk.WithBaseURL(url)
```

Python:

```python
client = mdmsdk.Client(client_id=id, client_secret=secret)  # or token=delegated, actor=user_id, base_url=url
```

First call `me` to check the credential: Go `client.Me.Get(ctx)`, Python `client.me.get()`.

## Call pattern

Resources are fields (Go) or attributes (Python) of the client; methods mirror `methods.yaml`. Python methods have `_async` twins. Results are the API's model types (Go `github.com/qbranchio/mdmsdk/api`, Python `mdmsdk.models`).

Runnable examples: `examples/go`, `examples/python`, `examples/curl`. Copy from them.

## Errors

Every non-success answer is one error type: Go `*mdmsdk.Error` (`errors.As`, or `errors.Is(err, mdmsdk.ErrNotFound)`), Python `mdmsdk.Error` subclasses (`mdmsdk.errors.NotFound`, ...).

- Branch on `code`, never on status or title. `references/errors.md` lists every code.
- Quote `instance` (`urn:request:<id>`) when reporting a problem.
- A tenant, member, group, or device outside the caller's reach answers 404, not 403.
- 403 `insufficient_scope` (account client) and `insufficient_permission` (delegated token) mean the credential lacks a scope or permission.

## Retries and idempotency

The SDK retries for you. Do not wrap calls in your own retry loop.

- Retried: transport errors, 429 (after `Retry-After`), 502, 503, 504 on GET, PUT, DELETE, and POSTs that declare an `Idempotency-Key`; 409 `idempotency_in_flight` on those POSTs.
- Never retried: other 409s (`conflict`, `tenant_deleting`, `licence_exceeded`, `licence_expired`), 400, 401, 403, 404, 422, and 503 `admin_app_unavailable`.
- At most 6 attempts within 90 s.
- POSTs that declare it get an `Idempotency-Key` generated once and reused on every attempt. To make a retry across processes safe, supply your own: Go `mdmsdk.WithIdempotencyKey(ctx, key)`, Python `with mdmsdk.idempotency_key(key):`. The same key needs the byte-identical body; the server keeps the answer 24 h.

## Rules

- Commands and some writes are asynchronous (202): the response is a reference; read the result later or receive a webhook.
- Policy reaches devices only as declarations; a setting's status comes from the device, not from the write.
- Only the operator registers account clients and browser origins; the API cannot.
- Send `actor` (Mdm-Actor) with an account client so the audit trail names your user.
