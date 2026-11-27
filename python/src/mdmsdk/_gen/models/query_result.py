from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.query_column import QueryColumn





T = TypeVar("T", bound="QueryResult")



@_attrs_define
class QueryResult:
    """ A table. Rows hold one value per column: a time as RFC 3339 UTC, text (null for no tenant), or a number.

        Attributes:
            columns (list[QueryColumn]):
            rows (list[list[Any]]):
     """

    columns: list[QueryColumn]
    rows: list[list[Any]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.query_column import QueryColumn # noqa: PLC0415
        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)



        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data


            rows.append(rows_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "columns": columns,
            "rows": rows,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_column import QueryColumn # noqa: PLC0415
        d = dict(src_dict)
        columns = []
        _columns = d.pop("columns")
        for columns_item_data in (_columns):
            columns_item = QueryColumn.from_dict(columns_item_data)



            columns.append(columns_item)


        rows = []
        _rows = d.pop("rows")
        for rows_item_data in (_rows):
            rows_item = cast(list[Any], rows_item_data)

            rows.append(rows_item)


        query_result = cls(
            columns=columns,
            rows=rows,
        )


        query_result.additional_properties = d
        return query_result

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
