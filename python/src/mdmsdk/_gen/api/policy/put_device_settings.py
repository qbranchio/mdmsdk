from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.device import Device
from ...models.policy import Policy
from ...models.problem import Problem
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    tenant: str,
    id: UUID,
    *,
    body: Policy,
    mdm_actor: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(mdm_actor, Unset):
        headers["Mdm-Actor"] = mdm_actor



    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/tenants/{tenant}/devices/{id}/settings".format(tenant=quote(str(tenant), safe=""),id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Device | Problem | None:
    if response.status_code == 202:
        response_202 = Device.from_dict(response.json())



        return response_202

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Device | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant: str,
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: Policy,
    mdm_actor: str | Unset = UNSET,

) -> Response[Device | Problem]:
    """ Set the device's own settings

     Replaces the device's own items and rebuilds its effective policy (its assigned profiles, then these
    items). When the result changes its revision increments and its status turns pending. An enrolled
    device whose level and OS are known gets it as declarations built for its level now, announced with
    a DeclarativeManagement command. Any other device gets them once DeviceInformation reports its level
    and OS. Devices below iOS and iPadOS 17 get none. The status turns applied when the device reports
    every declaration valid and active. An empty list removes the settings.

    Args:
        tenant (str):
        id (UUID):
        mdm_actor (str | Unset):
        body (Policy): Settings: items from the catalog (GET /api/v1/catalog). Items a device's
            level or OS cannot take are left out of its declarations and reported unsupported. Secret
            keys (marked in the catalog) are write-only: responses show {"secret": "set"}; a PUT that
            sends it keeps the stored value, a string replaces it, and leaving the key out clears it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Device | Problem]
     """


    kwargs = _get_kwargs(
        tenant=tenant,
id=id,
body=body,
mdm_actor=mdm_actor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    tenant: str,
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: Policy,
    mdm_actor: str | Unset = UNSET,

) -> Device | Problem | None:
    """ Set the device's own settings

     Replaces the device's own items and rebuilds its effective policy (its assigned profiles, then these
    items). When the result changes its revision increments and its status turns pending. An enrolled
    device whose level and OS are known gets it as declarations built for its level now, announced with
    a DeclarativeManagement command. Any other device gets them once DeviceInformation reports its level
    and OS. Devices below iOS and iPadOS 17 get none. The status turns applied when the device reports
    every declaration valid and active. An empty list removes the settings.

    Args:
        tenant (str):
        id (UUID):
        mdm_actor (str | Unset):
        body (Policy): Settings: items from the catalog (GET /api/v1/catalog). Items a device's
            level or OS cannot take are left out of its declarations and reported unsupported. Secret
            keys (marked in the catalog) are write-only: responses show {"secret": "set"}; a PUT that
            sends it keeps the stored value, a string replaces it, and leaving the key out clears it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Device | Problem
     """


    return sync_detailed(
        tenant=tenant,
id=id,
client=client,
body=body,
mdm_actor=mdm_actor,

    ).parsed

async def asyncio_detailed(
    tenant: str,
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: Policy,
    mdm_actor: str | Unset = UNSET,

) -> Response[Device | Problem]:
    """ Set the device's own settings

     Replaces the device's own items and rebuilds its effective policy (its assigned profiles, then these
    items). When the result changes its revision increments and its status turns pending. An enrolled
    device whose level and OS are known gets it as declarations built for its level now, announced with
    a DeclarativeManagement command. Any other device gets them once DeviceInformation reports its level
    and OS. Devices below iOS and iPadOS 17 get none. The status turns applied when the device reports
    every declaration valid and active. An empty list removes the settings.

    Args:
        tenant (str):
        id (UUID):
        mdm_actor (str | Unset):
        body (Policy): Settings: items from the catalog (GET /api/v1/catalog). Items a device's
            level or OS cannot take are left out of its declarations and reported unsupported. Secret
            keys (marked in the catalog) are write-only: responses show {"secret": "set"}; a PUT that
            sends it keeps the stored value, a string replaces it, and leaving the key out clears it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Device | Problem]
     """


    kwargs = _get_kwargs(
        tenant=tenant,
id=id,
body=body,
mdm_actor=mdm_actor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    tenant: str,
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: Policy,
    mdm_actor: str | Unset = UNSET,

) -> Device | Problem | None:
    """ Set the device's own settings

     Replaces the device's own items and rebuilds its effective policy (its assigned profiles, then these
    items). When the result changes its revision increments and its status turns pending. An enrolled
    device whose level and OS are known gets it as declarations built for its level now, announced with
    a DeclarativeManagement command. Any other device gets them once DeviceInformation reports its level
    and OS. Devices below iOS and iPadOS 17 get none. The status turns applied when the device reports
    every declaration valid and active. An empty list removes the settings.

    Args:
        tenant (str):
        id (UUID):
        mdm_actor (str | Unset):
        body (Policy): Settings: items from the catalog (GET /api/v1/catalog). Items a device's
            level or OS cannot take are left out of its declarations and reported unsupported. Secret
            keys (marked in the catalog) are write-only: responses show {"secret": "set"}; a PUT that
            sends it keeps the stored value, a string replaces it, and leaving the key out clears it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Device | Problem
     """


    return (await asyncio_detailed(
        tenant=tenant,
id=id,
client=client,
body=body,
mdm_actor=mdm_actor,

    )).parsed
