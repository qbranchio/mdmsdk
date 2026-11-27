"""Verify and decode the mdm API's webhook deliveries.

Deliveries are signed per Standard Webhooks 1.0 (webhook-id,
webhook-timestamp, webhook-signature; HMAC-SHA256 with the endpoint's whsec_
secret). During a rotation the server signs with the new and the previous
secret for 24 hours, so a receiver can hold either.

Receiver rules: verify the raw body before parsing it, answer 2xx within
10 s and do the work after, deduplicate on webhook-id, and know that 410
disables the endpoint.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any, cast

from standardwebhooks.webhooks import Webhook, WebhookVerificationError

from ._gen.models import (
    CommandCompletedEvent,
    DeviceEnrolledEvent,
    DeviceOSBehindEvent,
    DevicePolicyStatusEvent,
    DeviceUnenrolledEvent,
    PushCertificateExpiringEvent,
    TenantDeletedEvent,
    TenantDeletingEvent,
)

__all__ = ["Event", "SignatureError", "Verifier", "parse"]

Event = (
    CommandCompletedEvent | DeviceEnrolledEvent | DeviceOSBehindEvent | DevicePolicyStatusEvent
    | DeviceUnenrolledEvent | PushCertificateExpiringEvent | TenantDeletedEvent | TenantDeletingEvent
)

_BY_TYPE: dict[str, Any] = {
    "command.completed": CommandCompletedEvent,
    "device.enrolled": DeviceEnrolledEvent,
    "device.os_behind": DeviceOSBehindEvent,
    "device.policy_status": DevicePolicyStatusEvent,
    "device.unenrolled": DeviceUnenrolledEvent,
    "push_certificate.expiring": PushCertificateExpiringEvent,
    "tenant.deleted": TenantDeletedEvent,
    "tenant.deleting": TenantDeletingEvent,
}


class SignatureError(Exception):
    """No secret verified the delivery, or its timestamp is outside the tolerance."""


class Verifier:
    """Checks deliveries against the endpoint's secret, and the previous one during a rotation."""

    def __init__(self, *secrets: str) -> None:
        if not secrets:
            raise ValueError("webhooks: no secret")
        self._hooks = [Webhook(s) for s in secrets]

    def verify(self, body: bytes, headers: Mapping[str, str]) -> None:
        """Raises SignatureError unless one secret verifies the raw body."""
        lowered = {k.lower(): v for k, v in headers.items()}
        for hook in self._hooks:
            try:
                hook.verify(body, lowered, json_parse=False)
                return
            except WebhookVerificationError:
                continue
        raise SignatureError("webhooks: signature does not verify")

    def event(self, body: bytes, headers: Mapping[str, str]) -> Event:
        """Verifies, then decodes the delivery into its typed event."""
        self.verify(body, headers)
        return parse(body)


def parse(body: bytes) -> Event:
    """Decodes a verified body into its typed event, by its type field."""
    raw: Any = json.loads(body)
    if not isinstance(raw, dict):
        raise TypeError("webhooks: not an event")
    data = cast(dict[str, Any], raw)
    cls = _BY_TYPE.get(str(data.get("type")))
    if cls is None:
        raise ValueError(f"webhooks: unknown event type {data.get('type')!r}")
    return cast(Event, cls.from_dict(data))
