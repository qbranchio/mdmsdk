from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ade_public_key import ADEPublicKey
from ...models.problem import Problem
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    holder: UUID,
    *,
    mdm_actor: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(mdm_actor, Unset):
        headers["Mdm-Actor"] = mdm_actor



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/account/holders/{holder}/ade/public-key".format(holder=quote(str(holder), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> ADEPublicKey | Problem | None:
    if response.status_code == 200:
        response_200 = ADEPublicKey.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[ADEPublicKey | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    holder: UUID,
    *,
    client: AuthenticatedClient,
    mdm_actor: str | Unset = UNSET,

) -> Response[ADEPublicKey | Problem]:
    """ The holder's public key for Apple Business Manager

     The certificate to give Apple Business Manager when adding mdm as a device management service; made
    on first request. mdm keeps its private key to decrypt the server token.

    Args:
        holder (UUID):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ADEPublicKey | Problem]
     """


    kwargs = _get_kwargs(
        holder=holder,
mdm_actor=mdm_actor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    holder: UUID,
    *,
    client: AuthenticatedClient,
    mdm_actor: str | Unset = UNSET,

) -> ADEPublicKey | Problem | None:
    """ The holder's public key for Apple Business Manager

     The certificate to give Apple Business Manager when adding mdm as a device management service; made
    on first request. mdm keeps its private key to decrypt the server token.

    Args:
        holder (UUID):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ADEPublicKey | Problem
     """


    return sync_detailed(
        holder=holder,
client=client,
mdm_actor=mdm_actor,

    ).parsed

async def asyncio_detailed(
    holder: UUID,
    *,
    client: AuthenticatedClient,
    mdm_actor: str | Unset = UNSET,

) -> Response[ADEPublicKey | Problem]:
    """ The holder's public key for Apple Business Manager

     The certificate to give Apple Business Manager when adding mdm as a device management service; made
    on first request. mdm keeps its private key to decrypt the server token.

    Args:
        holder (UUID):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ADEPublicKey | Problem]
     """


    kwargs = _get_kwargs(
        holder=holder,
mdm_actor=mdm_actor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    holder: UUID,
    *,
    client: AuthenticatedClient,
    mdm_actor: str | Unset = UNSET,

) -> ADEPublicKey | Problem | None:
    """ The holder's public key for Apple Business Manager

     The certificate to give Apple Business Manager when adding mdm as a device management service; made
    on first request. mdm keeps its private key to decrypt the server token.

    Args:
        holder (UUID):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ADEPublicKey | Problem
     """


    return (await asyncio_detailed(
        holder=holder,
client=client,
mdm_actor=mdm_actor,

    )).parsed
