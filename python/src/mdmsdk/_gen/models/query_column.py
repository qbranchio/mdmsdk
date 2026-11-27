from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.query_column_type import QueryColumnType






T = TypeVar("T", bound="QueryColumn")



@_attrs_define
class QueryColumn:
    """ 
        Attributes:
            name (str): The dimension (`time`, `category`, `actor`, `tenant`, ...), then `actor_name` after `actor` and
                `tenant_name` after `tenant`, and last the measure (`count`).
            type_ (QueryColumnType):
     """

    name: str
    type_: QueryColumnType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = QueryColumnType(d.pop("type"))




        query_column = cls(
            name=name,
            type_=type_,
        )


        query_column.additional_properties = d
        return query_column

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
