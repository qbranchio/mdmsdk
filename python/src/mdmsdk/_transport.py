"""The transport under the generated client: auth, Mdm-Actor, the
Idempotency-Key, and retries. The rules match the Go SDK; scenarios/ tests both."""

from __future__ import annotations

import asyncio
import contextvars
import json
import secrets
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any, cast

import httpx2
from tenacity import AsyncRetrying, RetryCallState, Retrying, retry_if_result, stop_after_attempt, stop_after_delay

from . import __version__


@dataclass(frozen=True)
class OpInfo:
    id: str
    idempotent: bool = False
    retry_transport: bool = False


current_op: contextvars.ContextVar[OpInfo | None] = contextvars.ContextVar("mdm_op", default=None)
current_key: contextvars.ContextVar[str | None] = contextvars.ContextVar("mdm_idempotency_key", default=None)


@dataclass
class RetryPolicy:
    attempts: int = 6
    initial: float = 0.5
    max_wait: float = 15.0
    total: float = 90.0
    max_retry_after: float = 60.0
    sleep: Callable[[float], None] = time.sleep
    jitter: Callable[[], float] = lambda: secrets.randbelow(1_000_000) / 1_000_000


def retryable(method: str, op: OpInfo | None, status: int, code: str) -> bool:
    """The retry table of the SDK spec. status 0 is a transport error."""
    transient = status in (0, 429, 502, 504) or (status == 503 and code != "admin_app_unavailable")
    if method in ("GET", "HEAD", "PUT", "DELETE"):
        return transient
    if method == "POST" and op is not None:
        if op.idempotent:
            return transient or (status == 409 and code == "idempotency_in_flight")
        if op.retry_transport:
            return status in (0, 429)
    return False


def problem_code(resp: httpx2.Response) -> str:
    if resp.status_code < 400:
        return ""
    try:
        body: Any = json.loads(resp.content)
    except ValueError:
        return ""
    return str(cast(dict[str, Any], body).get("code", "")) if isinstance(body, dict) else ""


def retry_after(resp: httpx2.Response | None, limit: float) -> float | None:
    if resp is None:
        return None
    value = resp.headers.get("Retry-After")
    if value is None or not value.isdigit():
        return None
    return min(float(value), limit)


class RetryTransport(httpx2.BaseTransport):
    def __init__(self, inner: httpx2.BaseTransport, token: Callable[[], str], actor: str | None,
                 user_agent: str | None, policy: RetryPolicy) -> None:
        self._inner = inner
        self.token = token
        self.actor = actor
        self.user_agent = f"{user_agent} mdmsdk-python/{__version__}" if user_agent else f"mdmsdk-python/{__version__}"
        self.policy = policy

    def handle_request(self, request: httpx2.Request) -> httpx2.Response:
        op = current_op.get()
        key = current_key.get()
        if op is not None and op.idempotent and not key:
            key = secrets.token_hex(16)
        body = request.read()
        p = self.policy
        step = {"n": 0}

        def send() -> tuple[httpx2.Response | None, Exception | None]:
            r = httpx2.Request(request.method, request.url, headers=request.headers, content=body)
            r.headers["Authorization"] = f"Bearer {self.token()}"
            r.headers["User-Agent"] = self.user_agent
            if self.actor:
                r.headers["Mdm-Actor"] = self.actor
            if key:
                r.headers["Idempotency-Key"] = key
            try:
                resp = self._inner.handle_request(r)
                resp.read()
                return resp, None
            except httpx2.TransportError as exc:
                return None, exc

        def should_retry(outcome: tuple[httpx2.Response | None, Exception | None]) -> bool:
            resp, exc = outcome
            status = 0 if exc is not None or resp is None else resp.status_code
            return retryable(request.method, op, status, problem_code(resp) if resp is not None else "")

        def wait(state: RetryCallState) -> float:
            outcome = state.outcome.result() if state.outcome is not None else (None, None)
            after = retry_after(outcome[0], p.max_retry_after)
            if after is not None:
                return after
            delay = min(p.initial * (2 ** step["n"]), p.max_wait)
            step["n"] += 1
            return p.jitter() * delay

        retrying = Retrying(retry=retry_if_result(should_retry), stop=stop_after_attempt(p.attempts) | stop_after_delay(p.total),
                            wait=wait, sleep=p.sleep, retry_error_callback=lambda s: s.outcome.result() if s.outcome else (None, None),
                            reraise=False)
        resp, exc = retrying(send)
        if exc is not None:
            raise exc
        assert resp is not None
        return resp


class ClientCredentials:
    """Account client tokens: fetched, cached, and refreshed 60 s before expiry."""

    def __init__(self, client_id: str, client_secret: str, token_url: str, audience: str,
                 http: httpx2.Client | None = None, now: Callable[[], float] = time.time) -> None:
        self._id, self._secret, self._url, self._audience = client_id, client_secret, token_url, audience
        self._http = http or httpx2.Client(timeout=30)
        self._now = now
        self._token: str | None = None
        self._expires = 0.0

    def __call__(self) -> str:
        if self._token is None or self._now() >= self._expires - 60:
            resp = self._http.post(self._url, data={"grant_type": "client_credentials", "client_id": self._id,
                                                    "client_secret": self._secret, "audience": self._audience})
            resp.raise_for_status()
            body: Any = resp.json()
            self._token = str(body["access_token"])
            self._expires = self._now() + float(body.get("expires_in", 300))
        return self._token


class AsyncRetryTransport(httpx2.AsyncBaseTransport):
    """RetryTransport for AsyncClient: the same rules, with an async sleep."""

    def __init__(self, inner: httpx2.AsyncBaseTransport, sync: RetryTransport,
                 sleep: Callable[[float], Awaitable[None]] | None = None) -> None:
        self._inner = inner
        self._sync = sync
        self._sleep = sleep

    async def handle_async_request(self, request: httpx2.Request) -> httpx2.Response:
        op = current_op.get()
        key = current_key.get()
        if op is not None and op.idempotent and not key:
            key = secrets.token_hex(16)
        body = await request.aread()
        p = self._sync.policy
        step = {"n": 0}

        async def send() -> tuple[httpx2.Response | None, Exception | None]:
            r = httpx2.Request(request.method, request.url, headers=request.headers, content=body)
            r.headers["Authorization"] = f"Bearer {self._sync.token()}"
            r.headers["User-Agent"] = self._sync.user_agent
            if self._sync.actor:
                r.headers["Mdm-Actor"] = self._sync.actor
            if key:
                r.headers["Idempotency-Key"] = key
            try:
                resp = await self._inner.handle_async_request(r)
                await resp.aread()
                return resp, None
            except httpx2.TransportError as exc:
                return None, exc

        def should_retry(outcome: tuple[httpx2.Response | None, Exception | None]) -> bool:
            resp, exc = outcome
            status = 0 if exc is not None or resp is None else resp.status_code
            return retryable(request.method, op, status, problem_code(resp) if resp is not None else "")

        def wait(state: RetryCallState) -> float:
            outcome = state.outcome.result() if state.outcome is not None else (None, None)
            after = retry_after(outcome[0], p.max_retry_after)
            if after is not None:
                return after
            delay = min(p.initial * (2 ** step["n"]), p.max_wait)
            step["n"] += 1
            return p.jitter() * delay

        async def default_sleep(seconds: float) -> None:
            p.sleep(seconds) if p.sleep is not time.sleep else await asyncio.sleep(seconds)

        retrying = AsyncRetrying(retry=retry_if_result(should_retry), stop=stop_after_attempt(p.attempts) | stop_after_delay(p.total),
                                 wait=wait, sleep=self._sleep or default_sleep,
                                 retry_error_callback=lambda s: s.outcome.result() if s.outcome else (None, None))
        outcome: tuple[httpx2.Response | None, Exception | None] = await retrying(send)
        resp, exc = outcome
        if exc is not None:
            raise exc
        assert resp is not None
        return resp
