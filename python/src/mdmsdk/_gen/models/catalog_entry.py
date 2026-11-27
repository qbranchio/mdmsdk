from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.catalog_entry_group import CatalogEntryGroup
from ..models.catalog_entry_kind import CatalogEntryKind
from ..models.catalog_entry_levels_item import CatalogEntryLevelsItem
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.catalog_key import CatalogKey





T = TypeVar("T", bound="CatalogEntry")



@_attrs_define
class CatalogEntry:
    """ 
        Attributes:
            description (str):
            group (CatalogEntryGroup):
            id (str):
            keys (list[CatalogKey]):
            kind (CatalogEntryKind):
            levels (list[CatalogEntryLevelsItem]):
            title (str):
            type_ (str):
            deprecated_os (str | Unset):
            min_os (str | Unset):
            multiple (bool | Unset):
     """

    description: str
    group: CatalogEntryGroup
    id: str
    keys: list[CatalogKey]
    kind: CatalogEntryKind
    levels: list[CatalogEntryLevelsItem]
    title: str
    type_: str
    deprecated_os: str | Unset = UNSET
    min_os: str | Unset = UNSET
    multiple: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_key import CatalogKey # noqa: PLC0415
        description = self.description

        group = self.group.value

        id = self.id

        keys = []
        for keys_item_data in self.keys:
            keys_item = keys_item_data.to_dict()
            keys.append(keys_item)



        kind = self.kind.value

        levels = []
        for levels_item_data in self.levels:
            levels_item = levels_item_data.value
            levels.append(levels_item)



        title = self.title

        type_ = self.type_

        deprecated_os = self.deprecated_os

        min_os = self.min_os

        multiple = self.multiple


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "description": description,
            "group": group,
            "id": id,
            "keys": keys,
            "kind": kind,
            "levels": levels,
            "title": title,
            "type": type_,
        })
        if deprecated_os is not UNSET:
            field_dict["deprecated_os"] = deprecated_os
        if min_os is not UNSET:
            field_dict["min_os"] = min_os
        if multiple is not UNSET:
            field_dict["multiple"] = multiple

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_key import CatalogKey # noqa: PLC0415
        d = dict(src_dict)
        description = d.pop("description")

        group = CatalogEntryGroup(d.pop("group"))




        id = d.pop("id")

        keys = []
        _keys = d.pop("keys")
        for keys_item_data in (_keys):
            keys_item = CatalogKey.from_dict(keys_item_data)



            keys.append(keys_item)


        kind = CatalogEntryKind(d.pop("kind"))




        levels = []
        _levels = d.pop("levels")
        for levels_item_data in (_levels):
            levels_item = CatalogEntryLevelsItem(levels_item_data)



            levels.append(levels_item)


        title = d.pop("title")

        type_ = d.pop("type")

        deprecated_os = d.pop("deprecated_os", UNSET)

        min_os = d.pop("min_os", UNSET)

        multiple = d.pop("multiple", UNSET)

        catalog_entry = cls(
            description=description,
            group=group,
            id=id,
            keys=keys,
            kind=kind,
            levels=levels,
            title=title,
            type_=type_,
            deprecated_os=deprecated_os,
            min_os=min_os,
            multiple=multiple,
        )


        catalog_entry.additional_properties = d
        return catalog_entry

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
