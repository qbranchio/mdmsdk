"""A webhook receiver: verify the raw body, answer 2xx at once, work after,
and deduplicate on webhook-id."""

import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from mdmsdk.models import CommandCompletedEvent, DeviceEnrolledEvent
from mdmsdk.webhooks import SignatureError, Verifier

# The endpoint's secret; add the previous one while a rotation is under way.
verifier = Verifier(os.environ["MDM_WEBHOOK_SECRET"])
seen: set[str] = set()


class Receiver(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        body = self.rfile.read(int(self.headers.get("Content-Length", "0")))
        try:
            event = verifier.event(body, dict(self.headers.items()))
        except SignatureError:
            self.send_response(401)
            self.end_headers()
            return
        self.send_response(204)
        self.end_headers()
        msg_id = self.headers.get("webhook-id", "")
        if msg_id in seen:
            return
        seen.add(msg_id)
        if isinstance(event, DeviceEnrolledEvent):
            print("device", event.data.device_id, "enrolled in tenant", event.data.tenant_id)
        elif isinstance(event, CommandCompletedEvent):
            print("command", event.data.command_uuid, event.data.request_type, event.data.status)


HTTPServer(("", 8080), Receiver).serve_forever()
