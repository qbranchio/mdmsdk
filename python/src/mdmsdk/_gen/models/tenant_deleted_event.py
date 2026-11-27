from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tenant_deleted_event_type import TenantDeletedEventType
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.tenant_deleted_data import TenantDeletedData





T = TypeVar("T", bound="TenantDeletedEvent")



@_attrs_define
class TenantDeletedEvent:
    """ 
        Attributes:
            data (TenantDeletedData):
            timestamp (datetime.datetime): When the event happened.
            type_ (TenantDeletedEventType):
     """

    data: TenantDeletedData
    timestamp: datetime.datetime
    type_: TenantDeletedEventType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tenant_deleted_data import TenantDeletedData # noqa: PLC0415
        data = self.data.to_dict()

        timestamp = self.timestamp.isoformat()

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
            "timestamp": timestamp,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_deleted_data import TenantDeletedData # noqa: PLC0415
        d = dict(src_dict)
        data = TenantDeletedData.from_dict(d.pop("data"))




        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))




        type_ = TenantDeletedEventType(d.pop("type"))




        tenant_deleted_event = cls(
            data=data,
            timestamp=timestamp,
            type_=type_,
        )


        tenant_deleted_event.additional_properties = d
        return tenant_deleted_event

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
