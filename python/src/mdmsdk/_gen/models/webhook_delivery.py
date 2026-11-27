from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.webhook_delivery_status import WebhookDeliveryStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="WebhookDelivery")



@_attrs_define
class WebhookDelivery:
    """ 
        Attributes:
            attempts (int):
            created_at (datetime.datetime):
            event_id (UUID): The webhook-id header.
            id (UUID):
            next_attempt_at (datetime.datetime):
            status (WebhookDeliveryStatus):
            type_ (str):
            finished_at (datetime.datetime | Unset):
            last_error (str | Unset):
            last_status (int | Unset):
     """

    attempts: int
    created_at: datetime.datetime
    event_id: UUID
    id: UUID
    next_attempt_at: datetime.datetime
    status: WebhookDeliveryStatus
    type_: str
    finished_at: datetime.datetime | Unset = UNSET
    last_error: str | Unset = UNSET
    last_status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        created_at = self.created_at.isoformat()

        event_id = str(self.event_id)

        id = str(self.id)

        next_attempt_at = self.next_attempt_at.isoformat()

        status = self.status.value

        type_ = self.type_

        finished_at: str | Unset = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        last_error = self.last_error

        last_status = self.last_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "attempts": attempts,
            "created_at": created_at,
            "event_id": event_id,
            "id": id,
            "next_attempt_at": next_attempt_at,
            "status": status,
            "type": type_,
        })
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if last_status is not UNSET:
            field_dict["last_status"] = last_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempts = d.pop("attempts")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        event_id = UUID(d.pop("event_id"))




        id = UUID(d.pop("id"))




        next_attempt_at = datetime.datetime.fromisoformat(d.pop("next_attempt_at"))




        status = WebhookDeliveryStatus(d.pop("status"))




        type_ = d.pop("type")

        _finished_at = d.pop("finished_at", UNSET)
        finished_at: datetime.datetime | Unset
        if isinstance(_finished_at,  Unset):
            finished_at = UNSET
        else:
            finished_at = datetime.datetime.fromisoformat(_finished_at)




        last_error = d.pop("last_error", UNSET)

        last_status = d.pop("last_status", UNSET)

        webhook_delivery = cls(
            attempts=attempts,
            created_at=created_at,
            event_id=event_id,
            id=id,
            next_attempt_at=next_attempt_at,
            status=status,
            type_=type_,
            finished_at=finished_at,
            last_error=last_error,
            last_status=last_status,
        )


        webhook_delivery.additional_properties = d
        return webhook_delivery

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
