from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.member import Member
from ...models.member_request import MemberRequest
from ...models.problem import Problem
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    tenant: str,
    *,
    body: MemberRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(mdm_actor, Unset):
        headers["Mdm-Actor"] = mdm_actor



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tenants/{tenant}/members".format(tenant=quote(str(tenant), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Member | Problem | None:
    if response.status_code == 201:
        response_201 = Member.from_dict(response.json())



        return response_201

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

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Member | Problem]:
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
    body: MemberRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Response[Member | Problem]:
    """ Create a member

     A member is a person as an owner of devices. external_id is the account's own id for the person,
    unique in the tenant; 409 when it is taken.

    Args:
        tenant (str):
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):
        body (MemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Member | Problem]
     """


    kwargs = _get_kwargs(
        tenant=tenant,
body=body,
idempotency_key=idempotency_key,
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
    body: MemberRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Member | Problem | None:
    """ Create a member

     A member is a person as an owner of devices. external_id is the account's own id for the person,
    unique in the tenant; 409 when it is taken.

    Args:
        tenant (str):
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):
        body (MemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Member | Problem
     """


    return sync_detailed(
        tenant=tenant,
client=client,
body=body,
idempotency_key=idempotency_key,
mdm_actor=mdm_actor,

    ).parsed

async def asyncio_detailed(
    tenant: str,
    *,
    client: AuthenticatedClient,
    body: MemberRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Response[Member | Problem]:
    """ Create a member

     A member is a person as an owner of devices. external_id is the account's own id for the person,
    unique in the tenant; 409 when it is taken.

    Args:
        tenant (str):
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):
        body (MemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Member | Problem]
     """


    kwargs = _get_kwargs(
        tenant=tenant,
body=body,
idempotency_key=idempotency_key,
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
    body: MemberRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Member | Problem | None:
    """ Create a member

     A member is a person as an owner of devices. external_id is the account's own id for the person,
    unique in the tenant; 409 when it is taken.

    Args:
        tenant (str):
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):
        body (MemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Member | Problem
     """


    return (await asyncio_detailed(
        tenant=tenant,
client=client,
body=body,
idempotency_key=idempotency_key,
mdm_actor=mdm_actor,

    )).parsed
