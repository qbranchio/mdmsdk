from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HolderADE")



@_attrs_define
class HolderADE:
    """ 
        Attributes:
            public_key_issued (bool):
            token (bool):
            token_expires (datetime.datetime | Unset):
     """

    public_key_issued: bool
    token: bool
    token_expires: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        public_key_issued = self.public_key_issued

        token = self.token

        token_expires: str | Unset = UNSET
        if not isinstance(self.token_expires, Unset):
            token_expires = self.token_expires.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "public_key_issued": public_key_issued,
            "token": token,
        })
        if token_expires is not UNSET:
            field_dict["token_expires"] = token_expires

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_key_issued = d.pop("public_key_issued")

        token = d.pop("token")

        _token_expires = d.pop("token_expires", UNSET)
        token_expires: datetime.datetime | Unset
        if isinstance(_token_expires,  Unset):
            token_expires = UNSET
        else:
            token_expires = datetime.datetime.fromisoformat(_token_expires)




        holder_ade = cls(
            public_key_issued=public_key_issued,
            token=token,
            token_expires=token_expires,
        )


        holder_ade.additional_properties = d
        return holder_ade

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
