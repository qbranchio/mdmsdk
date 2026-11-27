from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="PushCertificateExpiringData")



@_attrs_define
class PushCertificateExpiringData:
    """ 
        Attributes:
            days_left (int): Whole days until it expires.
            holder_id (UUID): The credential holder whose push certificate is expiring.
            not_after (datetime.datetime): When the certificate expires.
            topic (str): The certificate's push topic.
     """

    days_left: int
    holder_id: UUID
    not_after: datetime.datetime
    topic: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        days_left = self.days_left

        holder_id = str(self.holder_id)

        not_after = self.not_after.isoformat()

        topic = self.topic


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "days_left": days_left,
            "holder_id": holder_id,
            "not_after": not_after,
            "topic": topic,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days_left = d.pop("days_left")

        holder_id = UUID(d.pop("holder_id"))




        not_after = datetime.datetime.fromisoformat(d.pop("not_after"))




        topic = d.pop("topic")

        push_certificate_expiring_data = cls(
            days_left=days_left,
            holder_id=holder_id,
            not_after=not_after,
            topic=topic,
        )


        push_certificate_expiring_data.additional_properties = d
        return push_certificate_expiring_data

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
