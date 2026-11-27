from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem import Problem
from ...models.push_certificate_request import PushCertificateRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    holder: UUID,
    *,
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
        "url": "/api/v1/account/holders/{holder}/push-certificate/request".format(holder=quote(str(holder), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Problem | PushCertificateRequest | None:
    if response.status_code == 200:
        response_200 = PushCertificateRequest.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Problem | PushCertificateRequest]:
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
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Response[Problem | PushCertificateRequest]:
    """ Request a push certificate

     mdm makes a key (kept, never returned) and returns the request, signed with mdm's vendor
    certificate, to upload at Apple's Push Certificates Portal (identity.apple.com) signed in with the
    organization's Apple Account: Create for a first certificate, Renew on the existing one to renew.
    Then upload the certificate Apple issues with PUT .../push-certificate. 409 until mdm has its vendor
    certificate: upload a certificate with its key instead.

    Args:
        holder (UUID):
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | PushCertificateRequest]
     """


    kwargs = _get_kwargs(
        holder=holder,
idempotency_key=idempotency_key,
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
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Problem | PushCertificateRequest | None:
    """ Request a push certificate

     mdm makes a key (kept, never returned) and returns the request, signed with mdm's vendor
    certificate, to upload at Apple's Push Certificates Portal (identity.apple.com) signed in with the
    organization's Apple Account: Create for a first certificate, Renew on the existing one to renew.
    Then upload the certificate Apple issues with PUT .../push-certificate. 409 until mdm has its vendor
    certificate: upload a certificate with its key instead.

    Args:
        holder (UUID):
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | PushCertificateRequest
     """


    return sync_detailed(
        holder=holder,
client=client,
idempotency_key=idempotency_key,
mdm_actor=mdm_actor,

    ).parsed

async def asyncio_detailed(
    holder: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Response[Problem | PushCertificateRequest]:
    """ Request a push certificate

     mdm makes a key (kept, never returned) and returns the request, signed with mdm's vendor
    certificate, to upload at Apple's Push Certificates Portal (identity.apple.com) signed in with the
    organization's Apple Account: Create for a first certificate, Renew on the existing one to renew.
    Then upload the certificate Apple issues with PUT .../push-certificate. 409 until mdm has its vendor
    certificate: upload a certificate with its key instead.

    Args:
        holder (UUID):
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | PushCertificateRequest]
     """


    kwargs = _get_kwargs(
        holder=holder,
idempotency_key=idempotency_key,
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
    idempotency_key: str | Unset = UNSET,
    mdm_actor: str | Unset = UNSET,

) -> Problem | PushCertificateRequest | None:
    """ Request a push certificate

     mdm makes a key (kept, never returned) and returns the request, signed with mdm's vendor
    certificate, to upload at Apple's Push Certificates Portal (identity.apple.com) signed in with the
    organization's Apple Account: Create for a first certificate, Renew on the existing one to renew.
    Then upload the certificate Apple issues with PUT .../push-certificate. 409 until mdm has its vendor
    certificate: upload a certificate with its key instead.

    Args:
        holder (UUID):
        idempotency_key (str | Unset):
        mdm_actor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | PushCertificateRequest
     """


    return (await asyncio_detailed(
        holder=holder,
client=client,
idempotency_key=idempotency_key,
mdm_actor=mdm_actor,

    )).parsed
