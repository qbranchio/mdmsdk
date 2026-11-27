from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem import Problem
from ...models.token_request import TokenRequest
from ...models.token_response import TokenResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: TokenRequest,
    mdm_actor: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(mdm_actor, Unset):
        headers["Mdm-Actor"] = mdm_actor



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tokens",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Problem | TokenResponse | None:
    if response.status_code == 201:
        response_201 = TokenResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Problem | TokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TokenRequest,
    mdm_actor: str | Unset = UNSET,

) -> Response[Problem | TokenResponse]:
    """ Issue a delegated token for one of the account's users

     Account clients with tokens:issue. The account's backend asks for a token for one of its users after
    applying its own rules; the user then calls the API directly with it. The token reaches one tenant
    of the account and, within it, the listed members (and their devices), the current members of the
    listed groups, or all of it, with the listed permissions (each one the client itself holds). It
    lasts ttl seconds, at most 900, and is never refreshed: ask again. Signed ES256 with mdm's keys (GET
    /api/.well-known/jwks.json).

    Args:
        mdm_actor (str | Unset):
        body (TokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | TokenResponse]
     """


    kwargs = _get_kwargs(
        body=body,
mdm_actor=mdm_actor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: TokenRequest,
    mdm_actor: str | Unset = UNSET,

) -> Problem | TokenResponse | None:
    """ Issue a delegated token for one of the account's users

     Account clients with tokens:issue. The account's backend asks for a token for one of its users after
    applying its own rules; the user then calls the API directly with it. The token reaches one tenant
    of the account and, within it, the listed members (and their devices), the current members of the
    listed groups, or all of it, with the listed permissions (each one the client itself holds). It
    lasts ttl seconds, at most 900, and is never refreshed: ask again. Signed ES256 with mdm's keys (GET
    /api/.well-known/jwks.json).

    Args:
        mdm_actor (str | Unset):
        body (TokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | TokenResponse
     """


    return sync_detailed(
        client=client,
body=body,
mdm_actor=mdm_actor,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TokenRequest,
    mdm_actor: str | Unset = UNSET,

) -> Response[Problem | TokenResponse]:
    """ Issue a delegated token for one of the account's users

     Account clients with tokens:issue. The account's backend asks for a token for one of its users after
    applying its own rules; the user then calls the API directly with it. The token reaches one tenant
    of the account and, within it, the listed members (and their devices), the current members of the
    listed groups, or all of it, with the listed permissions (each one the client itself holds). It
    lasts ttl seconds, at most 900, and is never refreshed: ask again. Signed ES256 with mdm's keys (GET
    /api/.well-known/jwks.json).

    Args:
        mdm_actor (str | Unset):
        body (TokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | TokenResponse]
     """


    kwargs = _get_kwargs(
        body=body,
mdm_actor=mdm_actor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TokenRequest,
    mdm_actor: str | Unset = UNSET,

) -> Problem | TokenResponse | None:
    """ Issue a delegated token for one of the account's users

     Account clients with tokens:issue. The account's backend asks for a token for one of its users after
    applying its own rules; the user then calls the API directly with it. The token reaches one tenant
    of the account and, within it, the listed members (and their devices), the current members of the
    listed groups, or all of it, with the listed permissions (each one the client itself holds). It
    lasts ttl seconds, at most 900, and is never refreshed: ask again. Signed ES256 with mdm's keys (GET
    /api/.well-known/jwks.json).

    Args:
        mdm_actor (str | Unset):
        body (TokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | TokenResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
mdm_actor=mdm_actor,

    )).parsed
