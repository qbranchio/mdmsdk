from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem import Problem
from ...models.webhook_endpoint import WebhookEndpoint
from ...models.webhook_request import WebhookRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: WebhookRequest,
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
        "url": "/api/v1/account/webhooks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Problem | WebhookEndpoint | None:
    if response.status_code == 201:
        response_201 = WebhookEndpoint.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Problem | WebhookEndpoint]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Response[Problem | WebhookEndpoint]:
    """ Add a webhook endpoint

     An https URL that receives the account's events, signed per Standard Webhooks 1.0 (webhook-id,
    webhook-timestamp, webhook-signature v1 HMAC-SHA256 over id.timestamp.body) with the secret in this
    response, shown only here. events limits the subscription; empty takes every event. Deliveries go
    one at a time per endpoint, in order, retried at 5 s, 5 m, 30 m, 2 h, 5 h, 10 h, 14 h, 20 h, and 24
    h; after the last, or on 410, the endpoint is disabled. Receivers dedupe on webhook-id. The address
    must resolve to a public IP; redirects are not followed.

    Args:
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):
        body (WebhookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEndpoint]
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
    body: WebhookRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Problem | WebhookEndpoint | None:
    """ Add a webhook endpoint

     An https URL that receives the account's events, signed per Standard Webhooks 1.0 (webhook-id,
    webhook-timestamp, webhook-signature v1 HMAC-SHA256 over id.timestamp.body) with the secret in this
    response, shown only here. events limits the subscription; empty takes every event. Deliveries go
    one at a time per endpoint, in order, retried at 5 s, 5 m, 30 m, 2 h, 5 h, 10 h, 14 h, 20 h, and 24
    h; after the last, or on 410, the endpoint is disabled. Receivers dedupe on webhook-id. The address
    must resolve to a public IP; redirects are not followed.

    Args:
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):
        body (WebhookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEndpoint
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
    body: WebhookRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Response[Problem | WebhookEndpoint]:
    """ Add a webhook endpoint

     An https URL that receives the account's events, signed per Standard Webhooks 1.0 (webhook-id,
    webhook-timestamp, webhook-signature v1 HMAC-SHA256 over id.timestamp.body) with the secret in this
    response, shown only here. events limits the subscription; empty takes every event. Deliveries go
    one at a time per endpoint, in order, retried at 5 s, 5 m, 30 m, 2 h, 5 h, 10 h, 14 h, 20 h, and 24
    h; after the last, or on 410, the endpoint is disabled. Receivers dedupe on webhook-id. The address
    must resolve to a public IP; redirects are not followed.

    Args:
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):
        body (WebhookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEndpoint]
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
    body: WebhookRequest,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Problem | WebhookEndpoint | None:
    """ Add a webhook endpoint

     An https URL that receives the account's events, signed per Standard Webhooks 1.0 (webhook-id,
    webhook-timestamp, webhook-signature v1 HMAC-SHA256 over id.timestamp.body) with the secret in this
    response, shown only here. events limits the subscription; empty takes every event. Deliveries go
    one at a time per endpoint, in order, retried at 5 s, 5 m, 30 m, 2 h, 5 h, 10 h, 14 h, 20 h, and 24
    h; after the last, or on 410, the endpoint is disabled. Receivers dedupe on webhook-id. The address
    must resolve to a public IP; redirects are not followed.

    Args:
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):
        body (WebhookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEndpoint
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,
mdm_actor=mdm_actor,

    )).parsed
