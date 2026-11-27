from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem import Problem
from ...models.query_request import QueryRequest
from ...models.query_result import QueryResult
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    tenant: str,
    *,
    body: QueryRequest,
    mdm_actor: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(mdm_actor, Unset):
        headers["Mdm-Actor"] = mdm_actor



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tenants/{tenant}/query".format(tenant=quote(str(tenant), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Problem | QueryResult | None:
    if response.status_code == 200:
        response_200 = QueryResult.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Problem | QueryResult]:
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
    body: QueryRequest,
    mdm_actor: str | Unset = UNSET,

) -> Response[Problem | QueryResult]:
    """ Query a tenant's data

     A read, though a POST because the query is its body. Admin app owners, admins, and viewers (the
    activity dataset for owners and admins only) and account clients with `devices:read` (activity also
    needs `tenants:read`); never delegated tokens. The query names a dataset (`activity` or `devices`),
    the measure `count`, what to group by (at most two dimensions; `series` adds time first), and
    filters, all from fixed allow-lists: no free SQL, and the caller's scope is always in the statement.
    The answer is a table.

    Args:
        tenant (str):
        mdm_actor (str | Unset):
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | QueryResult]
     """


    kwargs = _get_kwargs(
        tenant=tenant,
body=body,
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
    body: QueryRequest,
    mdm_actor: str | Unset = UNSET,

) -> Problem | QueryResult | None:
    """ Query a tenant's data

     A read, though a POST because the query is its body. Admin app owners, admins, and viewers (the
    activity dataset for owners and admins only) and account clients with `devices:read` (activity also
    needs `tenants:read`); never delegated tokens. The query names a dataset (`activity` or `devices`),
    the measure `count`, what to group by (at most two dimensions; `series` adds time first), and
    filters, all from fixed allow-lists: no free SQL, and the caller's scope is always in the statement.
    The answer is a table.

    Args:
        tenant (str):
        mdm_actor (str | Unset):
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | QueryResult
     """


    return sync_detailed(
        tenant=tenant,
client=client,
body=body,
mdm_actor=mdm_actor,

    ).parsed

async def asyncio_detailed(
    tenant: str,
    *,
    client: AuthenticatedClient,
    body: QueryRequest,
    mdm_actor: str | Unset = UNSET,

) -> Response[Problem | QueryResult]:
    """ Query a tenant's data

     A read, though a POST because the query is its body. Admin app owners, admins, and viewers (the
    activity dataset for owners and admins only) and account clients with `devices:read` (activity also
    needs `tenants:read`); never delegated tokens. The query names a dataset (`activity` or `devices`),
    the measure `count`, what to group by (at most two dimensions; `series` adds time first), and
    filters, all from fixed allow-lists: no free SQL, and the caller's scope is always in the statement.
    The answer is a table.

    Args:
        tenant (str):
        mdm_actor (str | Unset):
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | QueryResult]
     """


    kwargs = _get_kwargs(
        tenant=tenant,
body=body,
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
    body: QueryRequest,
    mdm_actor: str | Unset = UNSET,

) -> Problem | QueryResult | None:
    """ Query a tenant's data

     A read, though a POST because the query is its body. Admin app owners, admins, and viewers (the
    activity dataset for owners and admins only) and account clients with `devices:read` (activity also
    needs `tenants:read`); never delegated tokens. The query names a dataset (`activity` or `devices`),
    the measure `count`, what to group by (at most two dimensions; `series` adds time first), and
    filters, all from fixed allow-lists: no free SQL, and the caller's scope is always in the statement.
    The answer is a table.

    Args:
        tenant (str):
        mdm_actor (str | Unset):
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | QueryResult
     """


    return (await asyncio_detailed(
        tenant=tenant,
client=client,
body=body,
mdm_actor=mdm_actor,

    )).parsed
