from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.command_request_type import CommandRequestType
from ..types import UNSET, Unset






T = TypeVar("T", bound="CommandRequest")



@_attrs_define
class CommandRequest:
    """ 
        Attributes:
            type_ (CommandRequestType):
            message (str | Unset): DeviceLock only.
            phone_number (str | Unset): DeviceLock only.
     """

    type_: CommandRequestType
    message: str | Unset = UNSET
    phone_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        message = self.message

        phone_number = self.phone_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if message is not UNSET:
            field_dict["message"] = message
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = CommandRequestType(d.pop("type"))




        message = d.pop("message", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        command_request = cls(
            type_=type_,
            message=message,
            phone_number=phone_number,
        )


        command_request.additional_properties = d
        return command_request

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
