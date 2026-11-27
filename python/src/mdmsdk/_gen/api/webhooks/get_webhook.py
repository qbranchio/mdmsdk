from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem import Problem
from ...models.webhook_endpoint import WebhookEndpoint
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    webhook: UUID,
    *,
    mdm_actor: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(mdm_actor, Unset):
        headers["Mdm-Actor"] = mdm_actor



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/account/webhooks/{webhook}".format(webhook=quote(str(webhook), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Problem | WebhookEndpoint | None:
    if response.status_code == 200:
        response_200 = WebhookEndpoint.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Problem | WebhookEndpoint]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook: UUID,
    *,
    client: AuthenticatedClient,
    mdm_actor: str | Unset = UNSET,

) -> Response[Problem | WebhookEndpoint]:
    """ Get a webhook endpoint

    Args:
        webhook (UUID):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEndpoint]
     """


    kwargs = _get_kwargs(
        webhook=webhook,
mdm_actor=mdm_actor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    webhook: UUID,
    *,
    client: AuthenticatedClient,
    mdm_actor: str | Unset = UNSET,

) -> Problem | WebhookEndpoint | None:
    """ Get a webhook endpoint

    Args:
        webhook (UUID):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEndpoint
     """


    return sync_detailed(
        webhook=webhook,
client=client,
mdm_actor=mdm_actor,

    ).parsed

async def asyncio_detailed(
    webhook: UUID,
    *,
    client: AuthenticatedClient,
    mdm_actor: str | Unset = UNSET,

) -> Response[Problem | WebhookEndpoint]:
    """ Get a webhook endpoint

    Args:
        webhook (UUID):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEndpoint]
     """


    kwargs = _get_kwargs(
        webhook=webhook,
mdm_actor=mdm_actor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    webhook: UUID,
    *,
    client: AuthenticatedClient,
    mdm_actor: str | Unset = UNSET,

) -> Problem | WebhookEndpoint | None:
    """ Get a webhook endpoint

    Args:
        webhook (UUID):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEndpoint
     """


    return (await asyncio_detailed(
        webhook=webhook,
client=client,
mdm_actor=mdm_actor,

    )).parsed
