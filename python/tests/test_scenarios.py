"""Replays every file in ../scenarios against the Python SDK, as the Go SDK does."""

from __future__ import annotations

import asyncio
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

import httpx2
import pytest
import yaml

import mdmsdk
from mdmsdk.models import GetCatalogLevel

SCENARIOS = sorted((Path(__file__).resolve().parents[2] / "scenarios").glob("*.yaml"))


def _norm(v: Any) -> Any:
    """Compare decoded values: datetimes by instant, a null field equal to an absent one."""
    if isinstance(v, dict):
        return {k: _norm(x) for k, x in v.items() if x is not None}
    if isinstance(v, list):
        return [_norm(x) for x in v]
    if isinstance(v, str) and len(v) >= 20 and v[4] == "-" and v[10] == "T":
        try:
            return datetime.fromisoformat(v)
        except ValueError:
            return v
    return v


def _run(coro_or_value: Any, use_async: bool) -> Any:
    return asyncio.run(coro_or_value) if use_async else coro_or_value


def _calls(client: mdmsdk.Client, op: str, args: dict[str, Any], use_async: bool) -> Any:
    m = mdmsdk.models
    if op == "createTenant":
        body = m.TenantRequest.from_dict(args["body"])
        return _run(client.tenants.create_async(body) if use_async else client.tenants.create(body), use_async)
    if op == "updateTenant":
        body = m.TenantUpdate.from_dict(args["body"])
        return _run(client.tenants.update_async(args["tenant"], body) if use_async else client.tenants.update(args["tenant"], body), use_async)
    if op == "createMember":
        body = m.MemberRequest.from_dict(args["body"])
        return _run(client.members.create_async(args["tenant"], body) if use_async else client.members.create(args["tenant"], body), use_async)
    if op == "createGroup":
        body = m.GroupRequest.from_dict(args["body"])
        return _run(client.groups.create_async(args["tenant"], body) if use_async else client.groups.create(args["tenant"], body), use_async)
    if op == "deleteDevice":
        did = uuid.UUID(args["id"])
        return _run(client.devices.delete_async(args["tenant"], did) if use_async else client.devices.delete(args["tenant"], did), use_async)
    if op == "queryTenant":
        body = m.QueryRequest.from_dict(args["body"])
        return _run(client.tenants.query_async(args["tenant"], body) if use_async else client.tenants.query(args["tenant"], body), use_async)
    if op == "listTenantAuditEvents":
        if use_async:
            async def drain() -> list[Any]:
                return [e async for e in client.activity.list_async(args["tenant"])]
            return asyncio.run(drain())
        return list(client.activity.list(args["tenant"]))
    if op == "getMe":
        return asyncio.run(client.me.get_async()) if use_async else client.me.get()
    if op == "getCatalog":
        kw = {"level": GetCatalogLevel(args["level"])} if "level" in args else {}
        return asyncio.run(client.catalog.get_async(**kw)) if use_async else client.catalog.get(**kw)
    raise AssertionError(f"no call for {op}")


@pytest.mark.parametrize("use_async", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize("path", SCENARIOS, ids=[p.stem for p in SCENARIOS])
def test_scenario(path: Path, use_async: bool) -> None:
    s = yaml.safe_load(path.read_text())
    requests: list[httpx2.Request] = []
    waited: list[float] = []

    def handler(request: httpx2.Request) -> httpx2.Response:
        i = len(requests)
        requests.append(request)
        r = s["responses"][i]
        body = r.get("body")
        content = body.encode() if isinstance(body, str) else json.dumps(body).encode() if body is not None else b""
        return httpx2.Response(r["status"], headers=r.get("headers") or {}, content=content)

    policy = mdmsdk.RetryPolicy(sleep=waited.append, jitter=lambda: 0.5)
    mock = httpx2.MockTransport(handler)
    client = mdmsdk.Client(token="t", base_url="https://api.test", transport=mock, async_transport=mock, retry=policy)
    expect = s["expect"]
    call = s["call"]
    if expect.get("error"):
        with pytest.raises(mdmsdk.Error) as info:
            _calls(client, call["operation"], call.get("args") or {}, use_async)
        e = info.value
        want = expect["error"]
        assert e.kind == want["kind"]
        assert e.code == want["code"]
        assert e.status == want["status"]
        if "instance" in want:
            assert e.instance == want["instance"]
    else:
        got = _calls(client, call["operation"], call.get("args") or {}, use_async)
        if isinstance(got, list):
            got_dict: Any = [g.to_dict() for g in got]
        else:
            got_dict = None if got is None else got.to_dict()
        assert _norm(got_dict) == _norm(expect["result"])
    assert len(requests) == expect["attempts"]
    for i, want in enumerate(expect.get("cursors") or []):
        assert requests[i].url.params.get("cursor", "") == want
    if expect.get("waited_at_least_seconds"):
        assert sum(waited) >= expect["waited_at_least_seconds"]
