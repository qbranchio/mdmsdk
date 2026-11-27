from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem import Problem
from ...models.tenant import Tenant
from ...models.tenant_request import TenantRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: TenantRequest,
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
        "url": "/api/v1/tenants",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Problem | Tenant | None:
    if response.status_code == 201:
        response_201 = Tenant.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Problem | Tenant]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TenantRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Response[Problem | Tenant]:
    """ Create a tenant

     Account clients only (tenants:write). external_id is the account's own id for the tenant, unique in
    the account; 409 when it is taken.

    Args:
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):
        body (TenantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Tenant]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,
mdm_actor=mdm_actor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: TenantRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Problem | Tenant | None:
    """ Create a tenant

     Account clients only (tenants:write). external_id is the account's own id for the tenant, unique in
    the account; 409 when it is taken.

    Args:
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):
        body (TenantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Tenant
     """


    return sync_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,
mdm_actor=mdm_actor,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TenantRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Response[Problem | Tenant]:
    """ Create a tenant

     Account clients only (tenants:write). external_id is the account's own id for the tenant, unique in
    the account; 409 when it is taken.

    Args:
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):
        body (TenantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Tenant]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,
mdm_actor=mdm_actor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TenantRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Problem | Tenant | None:
    """ Create a tenant

     Account clients only (tenants:write). external_id is the account's own id for the tenant, unique in
    the account; 409 when it is taken.

    Args:
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):
        body (TenantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Tenant
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,
mdm_actor=mdm_actor,

    )).parsed
