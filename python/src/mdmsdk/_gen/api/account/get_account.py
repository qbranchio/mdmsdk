from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account import Account
from ...models.problem import Problem
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    mdm_actor: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(mdm_actor, Unset):
        headers["Mdm-Actor"] = mdm_actor



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/account",
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Account | Problem | None:
    if response.status_code == 200:
        response_200 = Account.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Account | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    mdm_actor: str | Unset = UNSET,

) -> Response[Account | Problem]:
    """ The caller's account

     Its name, contact, API clients, and registered browser origins. Account clients, and console owners
    and admins.

    Args:
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Account | Problem]
     """


    kwargs = _get_kwargs(
        mdm_actor=mdm_actor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    mdm_actor: str | Unset = UNSET,

) -> Account | Problem | None:
    """ The caller's account

     Its name, contact, API clients, and registered browser origins. Account clients, and console owners
    and admins.

    Args:
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Account | Problem
     """


    return sync_detailed(
        client=client,
mdm_actor=mdm_actor,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    mdm_actor: str | Unset = UNSET,

) -> Response[Account | Problem]:
    """ The caller's account

     Its name, contact, API clients, and registered browser origins. Account clients, and console owners
    and admins.

    Args:
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Account | Problem]
     """


    kwargs = _get_kwargs(
        mdm_actor=mdm_actor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    mdm_actor: str | Unset = UNSET,

) -> Account | Problem | None:
    """ The caller's account

     Its name, contact, API clients, and registered browser origins. Account clients, and console owners
    and admins.

    Args:
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Account | Problem
     """


    return (await asyncio_detailed(
        client=client,
mdm_actor=mdm_actor,

    )).parsed
