from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CatalogCond")



@_attrs_define
class CatalogCond:
    """ A condition on another key of the payload. key is relative to the constrained key's dictionary: "Name", "../Name"
    one level up, or "/Name" at the payload root. An unset key is compared by its default. Every field present must
    hold.

        Attributes:
            key (str):
            title (str):
            in_ (list[Any] | Unset):
            not_in (list[Any] | Unset):
            set_ (bool | Unset):
     """

    key: str
    title: str
    in_: list[Any] | Unset = UNSET
    not_in: list[Any] | Unset = UNSET
    set_: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        title = self.title

        in_: list[Any] | Unset = UNSET
        if not isinstance(self.in_, Unset):
            in_ = self.in_



        not_in: list[Any] | Unset = UNSET
        if not isinstance(self.not_in, Unset):
            not_in = self.not_in



        set_ = self.set_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "title": title,
        })
        if in_ is not UNSET:
            field_dict["in"] = in_
        if not_in is not UNSET:
            field_dict["not_in"] = not_in
        if set_ is not UNSET:
            field_dict["set"] = set_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        title = d.pop("title")

        in_ = cast(list[Any], d.pop("in", UNSET))


        not_in = cast(list[Any], d.pop("not_in", UNSET))


        set_ = d.pop("set", UNSET)

        catalog_cond = cls(
            key=key,
            title=title,
            in_=in_,
            not_in=not_in,
            set_=set_,
        )


        catalog_cond.additional_properties = d
        return catalog_cond

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
