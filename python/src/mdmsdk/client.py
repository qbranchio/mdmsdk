"""The mdm API client."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, Self

import httpx2

from ._gen.client import AuthenticatedClient
from ._services import SERVICES
from ._transport import AsyncRetryTransport, ClientCredentials, RetryPolicy, RetryTransport, current_key

DEFAULT_BASE_URL = "https://enroll.dev"
DEFAULT_TOKEN_URL = "https://id.enroll.dev/oauth/token"
DEFAULT_AUDIENCE = "https://enroll.dev/api"


class Client:
    """Calls the mdm API. Give it account client credentials, or a token
    (a delegated token from ``tokens.create``).

    Resources are attributes: ``client.me.get()``, ``client.catalog.get(level=...)``.
    """

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        token: str | Callable[[], str] | None = None,
        base_url: str = DEFAULT_BASE_URL,
        token_url: str = DEFAULT_TOKEN_URL,
        audience: str = DEFAULT_AUDIENCE,
        actor: str | None = None,
        user_agent: str | None = None,
        transport: httpx2.BaseTransport | None = None,
        async_transport: httpx2.AsyncBaseTransport | None = None,
        retry: RetryPolicy | None = None,
        timeout: float = 60.0,
    ) -> None:
        if token is not None:
            tokens: Callable[[], str] = token if callable(token) else (lambda: token)  # type: ignore[assignment]
        elif client_id and client_secret:
            tokens = ClientCredentials(client_id, client_secret, token_url, audience)
        else:
            raise ValueError("mdmsdk: pass client_id and client_secret, or token")
        self.retry = retry or RetryPolicy()
        inner = transport or httpx2.HTTPTransport()
        sync = RetryTransport(inner, tokens, actor, user_agent, self.retry)
        self._http = httpx2.Client(base_url=base_url.rstrip("/"), timeout=timeout, transport=sync)
        self._ahttp = httpx2.AsyncClient(base_url=base_url.rstrip("/"), timeout=timeout,
                                         transport=AsyncRetryTransport(async_transport or httpx2.AsyncHTTPTransport(), sync))
        self._gen = AuthenticatedClient(base_url=base_url.rstrip("/"), token="").set_httpx_client(self._http)
        self._gen.set_async_httpx_client(self._ahttp)
        for name, cls in SERVICES.items():
            setattr(self, name, cls(self))

    def __getattr__(self, name: str) -> Any:  # resources are set in __init__
        raise AttributeError(name)

    def close(self) -> None:
        self._http.close()

    async def aclose(self) -> None:
        await self._ahttp.aclose()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class idempotency_key:
    """Use a caller-chosen Idempotency-Key for the writes inside the block:
    ``with idempotency_key("order-42"): client.tenants.create(...)``."""

    def __init__(self, key: str) -> None:
        self._key = key
        self._token: Any = None

    def __enter__(self) -> None:
        self._token = current_key.set(self._key)

    def __exit__(self, *args: object) -> None:
        current_key.reset(self._token)
