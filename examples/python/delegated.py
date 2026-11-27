"""Delegated tokens: your backend issues a short-lived token for one of your
users, limited to their members and the permissions they need, and that
user's client calls the API with it."""

import os

import mdmsdk
from mdmsdk.models import TokenRequest, TokenRequestPermissionsItem

backend = mdmsdk.Client(client_id=os.environ["MDM_CLIENT_ID"], client_secret=os.environ["MDM_CLIENT_SECRET"])

# After your own checks: this user may see and lock their kids' devices.
tok = backend.tokens.create(TokenRequest(
    tenant="ext:family-7",
    subject="user-123",
    members=["ext:crm-41", "ext:crm-42"],
    permissions=[TokenRequestPermissionsItem.DEVICESREAD, TokenRequestPermissionsItem.COMMANDSWRITE],
))

# The user's client: at most 900 s, never refreshed; ask the backend again.
user = mdmsdk.Client(token=tok.access_token)
for device in user.devices.list("ext:family-7"):
    print(device.name)
