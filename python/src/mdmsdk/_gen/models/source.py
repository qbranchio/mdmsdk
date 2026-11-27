from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.source_layer import SourceLayer
from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="Source")



@_attrs_define
class Source:
    """ 
        Attributes:
            layer (SourceLayer): Where the item came from; settings is the device's own items.
            group_id (UUID | Unset): The group the profile reached the device through, for the group layer.
            profile_id (UUID | Unset):
     """

    layer: SourceLayer
    group_id: UUID | Unset = UNSET
    profile_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        layer = self.layer.value

        group_id: str | Unset = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = str(self.group_id)

        profile_id: str | Unset = UNSET
        if not isinstance(self.profile_id, Unset):
            profile_id = str(self.profile_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "layer": layer,
        })
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if profile_id is not UNSET:
            field_dict["profile_id"] = profile_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        layer = SourceLayer(d.pop("layer"))




        _group_id = d.pop("group_id", UNSET)
        group_id: UUID | Unset
        if isinstance(_group_id,  Unset):
            group_id = UNSET
        else:
            group_id = UUID(_group_id)




        _profile_id = d.pop("profile_id", UNSET)
        profile_id: UUID | Unset
        if isinstance(_profile_id,  Unset):
            profile_id = UNSET
        else:
            profile_id = UUID(_profile_id)




        source = cls(
            layer=layer,
            group_id=group_id,
            profile_id=profile_id,
        )


        source.additional_properties = d
        return source

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
