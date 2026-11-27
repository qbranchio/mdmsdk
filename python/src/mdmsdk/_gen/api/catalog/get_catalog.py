from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.catalog_response import CatalogResponse
from ...models.get_catalog_level import GetCatalogLevel
from ...models.problem import Problem
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    level: GetCatalogLevel | Unset = UNSET,
    os: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(mdm_actor, Unset):
        headers["Mdm-Actor"] = mdm_actor



    

    params: dict[str, Any] = {}

    json_level: str | Unset = UNSET
    if not isinstance(level, Unset):
        json_level = level.value

    params["level"] = json_level

    params["os"] = os


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/catalog",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> CatalogResponse | Problem | None:
    if response.status_code == 200:
        response_200 = CatalogResponse.from_dict(response.json())



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

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[CatalogResponse | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    level: GetCatalogLevel | Unset = UNSET,
    os: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Response[CatalogResponse | Problem]:
    """ Settings a device can take

     Every setting mdm can manage, from Apple's device-management schema (Release-v27.2). With level,
    only entries that level can take; with os too, only those that iOS version has. Keys carry their own
    level and version limits.

    Args:
        level (GetCatalogLevel | Unset):
        os (str | Unset):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogResponse | Problem]
     """


    kwargs = _get_kwargs(
        level=level,
os=os,
mdm_actor=mdm_actor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    level: GetCatalogLevel | Unset = UNSET,
    os: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> CatalogResponse | Problem | None:
    """ Settings a device can take

     Every setting mdm can manage, from Apple's device-management schema (Release-v27.2). With level,
    only entries that level can take; with os too, only those that iOS version has. Keys carry their own
    level and version limits.

    Args:
        level (GetCatalogLevel | Unset):
        os (str | Unset):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogResponse | Problem
     """


    return sync_detailed(
        client=client,
level=level,
os=os,
mdm_actor=mdm_actor,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    level: GetCatalogLevel | Unset = UNSET,
    os: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Response[CatalogResponse | Problem]:
    """ Settings a device can take

     Every setting mdm can manage, from Apple's device-management schema (Release-v27.2). With level,
    only entries that level can take; with os too, only those that iOS version has. Keys carry their own
    level and version limits.

    Args:
        level (GetCatalogLevel | Unset):
        os (str | Unset):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogResponse | Problem]
     """


    kwargs = _get_kwargs(
        level=level,
os=os,
mdm_actor=mdm_actor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    level: GetCatalogLevel | Unset = UNSET,
    os: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> CatalogResponse | Problem | None:
    """ Settings a device can take

     Every setting mdm can manage, from Apple's device-management schema (Release-v27.2). With level,
    only entries that level can take; with os too, only those that iOS version has. Keys carry their own
    level and version limits.

    Args:
        level (GetCatalogLevel | Unset):
        os (str | Unset):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogResponse | Problem
     """


    return (await asyncio_detailed(
        client=client,
level=level,
os=os,
mdm_actor=mdm_actor,

    )).parsed
