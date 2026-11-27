"""Python client for the mdm API. See the repository's AGENTS.md and skills/mdmsdk."""

__version__ = "0.1.0"

from . import errors, models
from ._transport import RetryPolicy
from .client import Client, idempotency_key
from .errors import Error

__all__ = ["Client", "Error", "RetryPolicy", "__version__", "errors", "idempotency_key", "models"]
