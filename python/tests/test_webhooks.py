from __future__ import annotations

from datetime import UTC, datetime, timedelta

import pytest
from standardwebhooks.webhooks import Webhook

from mdmsdk.models import TenantDeletedEvent
from mdmsdk.webhooks import SignatureError, Verifier, parse

NEW = "whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw"
OLD = "whsec_C2FVsBQIhrscChlQIMV+b5sSYspob7oD"
BODY = b'{"type":"tenant.deleted","timestamp":"2026-11-27T00:00:00Z","data":{"tenant_id":"00000000-0000-4000-8000-0000000000a1","tenant_external_id":null}}'


def headers(at: datetime, *secrets: str) -> dict[str, str]:
    sigs = [Webhook(s).sign("msg_1", at, BODY.decode()) for s in secrets]
    return {"webhook-id": "msg_1", "webhook-timestamp": str(int(at.timestamp())), "webhook-signature": " ".join(sigs)}


@pytest.mark.parametrize(
    ("hold", "signed", "age", "ok"),
    [
        ((NEW,), (NEW,), 0, True),
        ((NEW,), (NEW, OLD), 0, True),
        ((OLD,), (NEW, OLD), 0, True),
        ((NEW, OLD), (OLD,), 0, True),
        ((NEW,), (OLD,), 0, False),
        ((NEW,), (NEW,), 3600, False),
    ],
)
def test_verify(hold: tuple[str, ...], signed: tuple[str, ...], age: int, ok: bool) -> None:
    at = datetime.now(UTC) - timedelta(seconds=age)
    v = Verifier(*hold)
    if ok:
        v.verify(BODY, headers(at, *signed))
    else:
        with pytest.raises(SignatureError):
            v.verify(BODY, headers(at, *signed))


def test_event_is_typed() -> None:
    e = Verifier(NEW).event(BODY, headers(datetime.now(UTC), NEW))
    assert isinstance(e, TenantDeletedEvent)
    assert str(e.data.tenant_id) == "00000000-0000-4000-8000-0000000000a1"


def test_unknown_type() -> None:
    with pytest.raises(ValueError, match="unknown event type"):
        parse(b'{"type":"nope","timestamp":"x","data":{}}')
