from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="WebhookEndpoint")



@_attrs_define
class WebhookEndpoint:
    """ 
        Attributes:
            created_at (datetime.datetime):
            enabled (bool):
            events (list[str]): Empty takes every event.
            id (UUID):
            updated_at (datetime.datetime):
            url (str):
            disabled_reason (str | Unset):
            previous_secret_until (datetime.datetime | Unset): Until when deliveries are also signed with the previous
                secret.
            secret (str | Unset): The signing secret (whsec_...). Only on create and rotate.
     """

    created_at: datetime.datetime
    enabled: bool
    events: list[str]
    id: UUID
    updated_at: datetime.datetime
    url: str
    disabled_reason: str | Unset = UNSET
    previous_secret_until: datetime.datetime | Unset = UNSET
    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        enabled = self.enabled

        events = self.events



        id = str(self.id)

        updated_at = self.updated_at.isoformat()

        url = self.url

        disabled_reason = self.disabled_reason

        previous_secret_until: str | Unset = UNSET
        if not isinstance(self.previous_secret_until, Unset):
            previous_secret_until = self.previous_secret_until.isoformat()

        secret = self.secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "enabled": enabled,
            "events": events,
            "id": id,
            "updated_at": updated_at,
            "url": url,
        })
        if disabled_reason is not UNSET:
            field_dict["disabled_reason"] = disabled_reason
        if previous_secret_until is not UNSET:
            field_dict["previous_secret_until"] = previous_secret_until
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        enabled = d.pop("enabled")

        events = cast(list[str], d.pop("events"))


        id = UUID(d.pop("id"))




        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        url = d.pop("url")

        disabled_reason = d.pop("disabled_reason", UNSET)

        _previous_secret_until = d.pop("previous_secret_until", UNSET)
        previous_secret_until: datetime.datetime | Unset
        if isinstance(_previous_secret_until,  Unset):
            previous_secret_until = UNSET
        else:
            previous_secret_until = datetime.datetime.fromisoformat(_previous_secret_until)




        secret = d.pop("secret", UNSET)

        webhook_endpoint = cls(
            created_at=created_at,
            enabled=enabled,
            events=events,
            id=id,
            updated_at=updated_at,
            url=url,
            disabled_reason=disabled_reason,
            previous_secret_until=previous_secret_until,
            secret=secret,
        )


        webhook_endpoint.additional_properties = d
        return webhook_endpoint

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
