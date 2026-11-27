from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.catalog_key_format import CatalogKeyFormat
from ..models.catalog_key_levels_item import CatalogKeyLevelsItem
from ..models.catalog_key_type import CatalogKeyType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.catalog_cond import CatalogCond
  from ..models.catalog_option import CatalogOption
  from ..models.catalog_range import CatalogRange





T = TypeVar("T", bound="CatalogKey")



@_attrs_define
class CatalogKey:
    """ 
        Attributes:
            name (str):
            type_ (CatalogKeyType):
            default (Any | Unset):
            deprecated_os (str | Unset):
            description (str | Unset):
            excludes (list[str] | Unset): Sibling keys this key cannot be set with.
            format_ (CatalogKeyFormat | Unset): Apple's subtype of a string key; the server checks values against it.
            items (CatalogKey | Unset):
            keys (list[CatalogKey] | Unset):
            levels (list[CatalogKeyLevelsItem] | Unset):
            min_os (str | Unset):
            options (list[CatalogOption] | Unset):
            range_ (CatalogRange | Unset):
            required (bool | Unset):
            required_when (list[CatalogCond] | Unset): The key is required while every condition holds.
            secret (bool | Unset):
            title (str | Unset):
            when (list[CatalogCond] | Unset): The key applies only while every condition holds; set otherwise, the server
                refuses it.
     """

    name: str
    type_: CatalogKeyType
    default: Any | Unset = UNSET
    deprecated_os: str | Unset = UNSET
    description: str | Unset = UNSET
    excludes: list[str] | Unset = UNSET
    format_: CatalogKeyFormat | Unset = UNSET
    items: CatalogKey | Unset = UNSET
    keys: list[CatalogKey] | Unset = UNSET
    levels: list[CatalogKeyLevelsItem] | Unset = UNSET
    min_os: str | Unset = UNSET
    options: list[CatalogOption] | Unset = UNSET
    range_: CatalogRange | Unset = UNSET
    required: bool | Unset = UNSET
    required_when: list[CatalogCond] | Unset = UNSET
    secret: bool | Unset = UNSET
    title: str | Unset = UNSET
    when: list[CatalogCond] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_cond import CatalogCond # noqa: PLC0415
        from ..models.catalog_option import CatalogOption # noqa: PLC0415
        from ..models.catalog_range import CatalogRange # noqa: PLC0415
        name = self.name

        type_ = self.type_.value

        default = self.default

        deprecated_os = self.deprecated_os

        description = self.description

        excludes: list[str] | Unset = UNSET
        if not isinstance(self.excludes, Unset):
            excludes = self.excludes



        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value


        items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = []
            for keys_item_data in self.keys:
                keys_item = keys_item_data.to_dict()
                keys.append(keys_item)



        levels: list[str] | Unset = UNSET
        if not isinstance(self.levels, Unset):
            levels = []
            for levels_item_data in self.levels:
                levels_item = levels_item_data.value
                levels.append(levels_item)



        min_os = self.min_os

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)



        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        required = self.required

        required_when: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.required_when, Unset):
            required_when = []
            for required_when_item_data in self.required_when:
                required_when_item = required_when_item_data.to_dict()
                required_when.append(required_when_item)



        secret = self.secret

        title = self.title

        when: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.when, Unset):
            when = []
            for when_item_data in self.when:
                when_item = when_item_data.to_dict()
                when.append(when_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "type": type_,
        })
        if default is not UNSET:
            field_dict["default"] = default
        if deprecated_os is not UNSET:
            field_dict["deprecated_os"] = deprecated_os
        if description is not UNSET:
            field_dict["description"] = description
        if excludes is not UNSET:
            field_dict["excludes"] = excludes
        if format_ is not UNSET:
            field_dict["format"] = format_
        if items is not UNSET:
            field_dict["items"] = items
        if keys is not UNSET:
            field_dict["keys"] = keys
        if levels is not UNSET:
            field_dict["levels"] = levels
        if min_os is not UNSET:
            field_dict["min_os"] = min_os
        if options is not UNSET:
            field_dict["options"] = options
        if range_ is not UNSET:
            field_dict["range"] = range_
        if required is not UNSET:
            field_dict["required"] = required
        if required_when is not UNSET:
            field_dict["required_when"] = required_when
        if secret is not UNSET:
            field_dict["secret"] = secret
        if title is not UNSET:
            field_dict["title"] = title
        if when is not UNSET:
            field_dict["when"] = when

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_cond import CatalogCond # noqa: PLC0415
        from ..models.catalog_option import CatalogOption # noqa: PLC0415
        from ..models.catalog_range import CatalogRange # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        type_ = CatalogKeyType(d.pop("type"))




        default = d.pop("default", UNSET)

        deprecated_os = d.pop("deprecated_os", UNSET)

        description = d.pop("description", UNSET)

        excludes = cast(list[str], d.pop("excludes", UNSET))


        _format_ = d.pop("format", UNSET)
        format_: CatalogKeyFormat | Unset
        if isinstance(_format_,  Unset):
            format_ = UNSET
        else:
            format_ = CatalogKeyFormat(_format_)




        _items = d.pop("items", UNSET)
        items: CatalogKey | Unset
        if isinstance(_items,  Unset):
            items = UNSET
        else:
            items = CatalogKey.from_dict(_items)




        _keys = d.pop("keys", UNSET)
        keys: list[CatalogKey] | Unset = UNSET
        if _keys is not UNSET:
            keys = []
            for keys_item_data in _keys:
                keys_item = CatalogKey.from_dict(keys_item_data)



                keys.append(keys_item)


        _levels = d.pop("levels", UNSET)
        levels: list[CatalogKeyLevelsItem] | Unset = UNSET
        if _levels is not UNSET:
            levels = []
            for levels_item_data in _levels:
                levels_item = CatalogKeyLevelsItem(levels_item_data)



                levels.append(levels_item)


        min_os = d.pop("min_os", UNSET)

        _options = d.pop("options", UNSET)
        options: list[CatalogOption] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = CatalogOption.from_dict(options_item_data)



                options.append(options_item)


        _range_ = d.pop("range", UNSET)
        range_: CatalogRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = CatalogRange.from_dict(_range_)




        required = d.pop("required", UNSET)

        _required_when = d.pop("required_when", UNSET)
        required_when: list[CatalogCond] | Unset = UNSET
        if _required_when is not UNSET:
            required_when = []
            for required_when_item_data in _required_when:
                required_when_item = CatalogCond.from_dict(required_when_item_data)



                required_when.append(required_when_item)


        secret = d.pop("secret", UNSET)

        title = d.pop("title", UNSET)

        _when = d.pop("when", UNSET)
        when: list[CatalogCond] | Unset = UNSET
        if _when is not UNSET:
            when = []
            for when_item_data in _when:
                when_item = CatalogCond.from_dict(when_item_data)



                when.append(when_item)


        catalog_key = cls(
            name=name,
            type_=type_,
            default=default,
            deprecated_os=deprecated_os,
            description=description,
            excludes=excludes,
            format_=format_,
            items=items,
            keys=keys,
            levels=levels,
            min_os=min_os,
            options=options,
            range_=range_,
            required=required,
            required_when=required_when,
            secret=secret,
            title=title,
            when=when,
        )


        catalog_key.additional_properties = d
        return catalog_key

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
