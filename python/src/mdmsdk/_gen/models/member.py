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






T = TypeVar("T", bound="Member")



@_attrs_define
class Member:
    """ 
        Attributes:
            created_at (datetime.datetime):
            groups (list[UUID]): The ids of the member's groups.
            id (UUID):
            name (str):
            updated_at (datetime.datetime):
            external_id (str | Unset):
     """

    created_at: datetime.datetime
    groups: list[UUID]
    id: UUID
    name: str
    updated_at: datetime.datetime
    external_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        groups = []
        for groups_item_data in self.groups:
            groups_item = str(groups_item_data)
            groups.append(groups_item)



        id = str(self.id)

        name = self.name

        updated_at = self.updated_at.isoformat()

        external_id = self.external_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "groups": groups,
            "id": id,
            "name": name,
            "updated_at": updated_at,
        })
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        groups = []
        _groups = d.pop("groups")
        for groups_item_data in (_groups):
            groups_item = UUID(groups_item_data)



            groups.append(groups_item)


        id = UUID(d.pop("id"))




        name = d.pop("name")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        external_id = d.pop("external_id", UNSET)

        member = cls(
            created_at=created_at,
            groups=groups,
            id=id,
            name=name,
            updated_at=updated_at,
            external_id=external_id,
        )


        member.additional_properties = d
        return member

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
