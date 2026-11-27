from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.field_error import FieldError





T = TypeVar("T", bound="Problem")



@_attrs_define
class Problem:
    """ RFC 9457 problem detail.

        Attributes:
            status (int):
            title (str):
            type_ (str):
            code (str | Unset): Names the problem; branch on it, not on status or title.
            detail (str | Unset):
            errors (list[FieldError] | Unset):
            instance (str | Unset): urn:request:<id>, the request's id; quote it when reporting a problem.
     """

    status: int
    title: str
    type_: str
    code: str | Unset = UNSET
    detail: str | Unset = UNSET
    errors: list[FieldError] | Unset = UNSET
    instance: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.field_error import FieldError # noqa: PLC0415
        status = self.status

        title = self.title

        type_ = self.type_

        code = self.code

        detail = self.detail

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)



        instance = self.instance


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "title": title,
            "type": type_,
        })
        if code is not UNSET:
            field_dict["code"] = code
        if detail is not UNSET:
            field_dict["detail"] = detail
        if errors is not UNSET:
            field_dict["errors"] = errors
        if instance is not UNSET:
            field_dict["instance"] = instance

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_error import FieldError # noqa: PLC0415
        d = dict(src_dict)
        status = d.pop("status")

        title = d.pop("title")

        type_ = d.pop("type")

        code = d.pop("code", UNSET)

        detail = d.pop("detail", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[FieldError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = FieldError.from_dict(errors_item_data)



                errors.append(errors_item)


        instance = d.pop("instance", UNSET)

        problem = cls(
            status=status,
            title=title,
            type_=type_,
            code=code,
            detail=detail,
            errors=errors,
            instance=instance,
        )


        problem.additional_properties = d
        return problem

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
