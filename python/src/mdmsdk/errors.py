"""API errors: RFC 9457 problems as exceptions. Branch on ``code``; quote ``instance``."""

from __future__ import annotations

import json
from dataclasses import dataclass
from dataclasses import field as dc_field
from typing import Any, cast

__all__ = [
    "BadRequest",
    "Conflict",
    "Error",
    "FieldError",
    "Forbidden",
    "NotFound",
    "RateLimited",
    "Server",
    "Unauthorized",
    "Unavailable",
    "Unexpected",
    "Validation",
    "decode_error",
]


@dataclass(frozen=True)
class FieldError:
    field: str
    detail: str


@dataclass
class Error(Exception):
    """An API error. ``kind`` is the class name; ``code`` names the problem."""

    status: int
    code: str = ""
    title: str = ""
    detail: str = ""
    instance: str = ""
    fields: list[FieldError] = dc_field(default_factory=lambda: list[FieldError]())
    body: bytes = b""

    @property
    def kind(self) -> str:
        return type(self).__name__

    def __str__(self) -> str:
        msg = f"mdm: {self.status}"
        if self.code:
            msg += f" {self.code}"
        if self.detail or self.title:
            msg += f": {self.detail or self.title}"
        if self.instance:
            msg += f" ({self.instance})"
        return msg


class BadRequest(Error): ...
class Unauthorized(Error): ...
class Forbidden(Error): ...
class NotFound(Error): ...
class Conflict(Error): ...
class Validation(Error): ...
class RateLimited(Error): ...
class Unavailable(Error): ...
class Server(Error): ...
class Unexpected(Error): ...


_BY_STATUS: dict[int, type[Error]] = {
    400: BadRequest, 401: Unauthorized, 403: Forbidden, 404: NotFound, 409: Conflict,
    422: Validation, 429: RateLimited, 503: Unavailable,
}


def kind_of(status: int) -> type[Error]:
    if status in _BY_STATUS:
        return _BY_STATUS[status]
    return Server if status >= 500 else Unexpected


def decode_error(status: int, content_type: str, body: bytes) -> Error:
    """The error for a non-success response. A body that is not problem+json
    (a proxy during a deploy) gives the class for its status with no code."""
    cls = kind_of(status)
    media = content_type.split(";")[0].strip().lower()
    if media in ("application/problem+json", "application/json"):
        try:
            raw: Any = json.loads(body)
        except ValueError:
            raw = None
        if isinstance(raw, dict):
            p = cast(dict[str, Any], raw)
            errs = cast(list[Any], p.get("errors") or [])
            fields = [FieldError(str(f.get("field", "")), str(f.get("detail", "")))
                      for f in (cast(dict[str, Any], e) for e in errs if isinstance(e, dict))]
            return cls(status=status, code=str(p.get("code", "")), title=str(p.get("title", "")),
                       detail=str(p.get("detail", "")), instance=str(p.get("instance", "")), fields=fields, body=body)
    return cls(status=status, body=body)
