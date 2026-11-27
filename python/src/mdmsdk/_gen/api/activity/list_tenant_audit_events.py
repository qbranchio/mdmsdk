from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.audit_page import AuditPage
from ...models.problem import Problem
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    tenant: str,
    *,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    actor: str | Unset = UNSET,
    action: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(mdm_actor, Unset):
        headers["Mdm-Actor"] = mdm_actor



    

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["actor"] = actor

    params["action"] = action

    params["resource_type"] = resource_type

    params["resource_id"] = resource_id

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tenants/{tenant}/audit-events".format(tenant=quote(str(tenant), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AuditPage | Problem | None:
    if response.status_code == 200:
        response_200 = AuditPage.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AuditPage | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    actor: str | Unset = UNSET,
    action: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Response[AuditPage | Problem]:
    """ A tenant's activity

     Who did what in the tenant, newest first, as sentences. Admin app owners and admins (not viewers)
    and account clients with `tenants:read`; never delegated tokens. Filters narrow the list; the cursor
    works only for the request that issued it.

    Args:
        tenant (str):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        actor (str | Unset):
        action (str | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditPage | Problem]
     """


    kwargs = _get_kwargs(
        tenant=tenant,
from_=from_,
to=to,
actor=actor,
action=action,
resource_type=resource_type,
resource_id=resource_id,
limit=limit,
cursor=cursor,
mdm_actor=mdm_actor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    tenant: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    actor: str | Unset = UNSET,
    action: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> AuditPage | Problem | None:
    """ A tenant's activity

     Who did what in the tenant, newest first, as sentences. Admin app owners and admins (not viewers)
    and account clients with `tenants:read`; never delegated tokens. Filters narrow the list; the cursor
    works only for the request that issued it.

    Args:
        tenant (str):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        actor (str | Unset):
        action (str | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditPage | Problem
     """


    return sync_detailed(
        tenant=tenant,
client=client,
from_=from_,
to=to,
actor=actor,
action=action,
resource_type=resource_type,
resource_id=resource_id,
limit=limit,
cursor=cursor,
mdm_actor=mdm_actor,

    ).parsed

async def asyncio_detailed(
    tenant: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    actor: str | Unset = UNSET,
    action: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Response[AuditPage | Problem]:
    """ A tenant's activity

     Who did what in the tenant, newest first, as sentences. Admin app owners and admins (not viewers)
    and account clients with `tenants:read`; never delegated tokens. Filters narrow the list; the cursor
    works only for the request that issued it.

    Args:
        tenant (str):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        actor (str | Unset):
        action (str | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditPage | Problem]
     """


    kwargs = _get_kwargs(
        tenant=tenant,
from_=from_,
to=to,
actor=actor,
action=action,
resource_type=resource_type,
resource_id=resource_id,
limit=limit,
cursor=cursor,
mdm_actor=mdm_actor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    tenant: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    actor: str | Unset = UNSET,
    action: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> AuditPage | Problem | None:
    """ A tenant's activity

     Who did what in the tenant, newest first, as sentences. Admin app owners and admins (not viewers)
    and account clients with `tenants:read`; never delegated tokens. Filters narrow the list; the cursor
    works only for the request that issued it.

    Args:
        tenant (str):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        actor (str | Unset):
        action (str | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditPage | Problem
     """


    return (await asyncio_detailed(
        tenant=tenant,
client=client,
from_=from_,
to=to,
actor=actor,
action=action,
resource_type=resource_type,
resource_id=resource_id,
limit=limit,
cursor=cursor,
mdm_actor=mdm_actor,

    )).parsed
