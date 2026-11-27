"""Who am I: configure an account client, call me, list the supervised
catalog, and handle an error by its code."""

import os

import mdmsdk
from mdmsdk.models import GetCatalogLevel

client = mdmsdk.Client(client_id=os.environ["MDM_CLIENT_ID"], client_secret=os.environ["MDM_CLIENT_SECRET"])

try:
    me = client.me.get()
except mdmsdk.errors.Forbidden as err:
    if err.code == "insufficient_scope":
        raise SystemExit(f"the client lacks a scope: {err.detail} ({err.instance})") from err
    raise
print("caller:", me.kind)

catalog = client.catalog.get(level=GetCatalogLevel.SUPERVISED)
print("settings for supervised devices:", len(catalog.entries))
