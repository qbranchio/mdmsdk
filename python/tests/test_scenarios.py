"""Replays every file in ../scenarios against the Python SDK, as the Go SDK does."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Any

import httpx2
import pytest
import yaml

import mdmsdk
from mdmsdk.models import GetCatalogLevel

SCENARIOS = sorted((Path(__file__).resolve().parents[2] / "scenarios").glob("*.yaml"))


def _calls(client: mdmsdk.Client, op: str, args: dict[str, Any], use_async: bool) -> Any:
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
        assert got.to_dict() == expect["result"]
    assert len(requests) == expect["attempts"]
    if expect.get("waited_at_least_seconds"):
        assert sum(waited) >= expect["waited_at_least_seconds"]
