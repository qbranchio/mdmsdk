"""Runs one generated operation with the operation's facts in context and
turns a non-success response into an Error."""

from __future__ import annotations

import importlib
from collections.abc import Mapping
from typing import Any, cast

from ._transport import OpInfo, current_op
from .errors import decode_error


def _result(resp: Any, op: OpInfo) -> Any:
    status = int(resp.status_code)
    if 200 <= status < 300:
        return resp.parsed
    headers = cast(Mapping[str, str], resp.headers or {})
    raise decode_error(status, str(headers.get("content-type", "")), bytes(resp.content))


def call(client: Any, module: str, op: OpInfo, kwargs: dict[str, Any]) -> Any:
    mod = importlib.import_module(module, package=__package__)
    token = current_op.set(op)
    try:
        resp = mod.sync_detailed(client=client._gen, **kwargs)
    finally:
        current_op.reset(token)
    return _result(resp, op)


async def call_async(client: Any, module: str, op: OpInfo, kwargs: dict[str, Any]) -> Any:
    mod = importlib.import_module(module, package=__package__)
    token = current_op.set(op)
    try:
        resp = await mod.asyncio_detailed(client=client._gen, **kwargs)
    finally:
        current_op.reset(token)
    return _result(resp, op)
