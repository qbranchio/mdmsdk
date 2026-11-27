from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="TenantUpdate")



@_attrs_define
class TenantUpdate:
    """ 
        Attributes:
            holder_id (UUID | Unset): Moves the tenant to another credential holder of the account; enrolled devices keep
                their push topic.
            min_os (str | Unset): The iOS version its devices must reach (26.2); empty clears it. Without it a device is
                behind when Apple has a newer release for its model.
            name (str | Unset):
     """

    holder_id: UUID | Unset = UNSET
    min_os: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        holder_id: str | Unset = UNSET
        if not isinstance(self.holder_id, Unset):
            holder_id = str(self.holder_id)

        min_os = self.min_os

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if holder_id is not UNSET:
            field_dict["holder_id"] = holder_id
        if min_os is not UNSET:
            field_dict["min_os"] = min_os
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _holder_id = d.pop("holder_id", UNSET)
        holder_id: UUID | Unset
        if isinstance(_holder_id,  Unset):
            holder_id = UNSET
        else:
            holder_id = UUID(_holder_id)




        min_os = d.pop("min_os", UNSET)

        name = d.pop("name", UNSET)

        tenant_update = cls(
            holder_id=holder_id,
            min_os=min_os,
            name=name,
        )


        tenant_update.additional_properties = d
        return tenant_update

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
