from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HolderVPP")



@_attrs_define
class HolderVPP:
    """ 
        Attributes:
            token (bool):
            expires (datetime.datetime | Unset):
            org_name (str | Unset):
     """

    token: bool
    expires: datetime.datetime | Unset = UNSET
    org_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        token = self.token

        expires: str | Unset = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat()

        org_name = self.org_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "token": token,
        })
        if expires is not UNSET:
            field_dict["expires"] = expires
        if org_name is not UNSET:
            field_dict["org_name"] = org_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        _expires = d.pop("expires", UNSET)
        expires: datetime.datetime | Unset
        if isinstance(_expires,  Unset):
            expires = UNSET
        else:
            expires = datetime.datetime.fromisoformat(_expires)




        org_name = d.pop("org_name", UNSET)

        holder_vpp = cls(
            token=token,
            expires=expires,
            org_name=org_name,
        )


        holder_vpp.additional_properties = d
        return holder_vpp

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
