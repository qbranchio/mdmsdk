from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.policy_item import PolicyItem





T = TypeVar("T", bound="Profile")



@_attrs_define
class Profile:
    """ 
        Attributes:
            created_at (datetime.datetime):
            id (UUID): A UUIDv7. Within one layer the lower id wins a conflict.
            items (list[PolicyItem]):
            name (str):
            updated_at (datetime.datetime):
     """

    created_at: datetime.datetime
    id: UUID
    items: list[PolicyItem]
    name: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_item import PolicyItem # noqa: PLC0415
        created_at = self.created_at.isoformat()

        id = str(self.id)

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)



        name = self.name

        updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "id": id,
            "items": items,
            "name": name,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_item import PolicyItem # noqa: PLC0415
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = UUID(d.pop("id"))




        items = []
        _items = d.pop("items")
        for items_item_data in (_items):
            items_item = PolicyItem.from_dict(items_item_data)



            items.append(items_item)


        name = d.pop("name")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        profile = cls(
            created_at=created_at,
            id=id,
            items=items,
            name=name,
            updated_at=updated_at,
        )


        profile.additional_properties = d
        return profile

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
