from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="TenantRequest")



@_attrs_define
class TenantRequest:
    """ 
        Attributes:
            name (str):
            external_id (str | Unset): The account's own id for the tenant: letters, digits, and the characters . _ ~ @ : -
            holder_id (UUID | Unset): The credential holder whose Apple credentials the tenant uses; the account's default
                when absent.
     """

    name: str
    external_id: str | Unset = UNSET
    holder_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        external_id = self.external_id

        holder_id: str | Unset = UNSET
        if not isinstance(self.holder_id, Unset):
            holder_id = str(self.holder_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if holder_id is not UNSET:
            field_dict["holder_id"] = holder_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        external_id = d.pop("external_id", UNSET)

        _holder_id = d.pop("holder_id", UNSET)
        holder_id: UUID | Unset
        if isinstance(_holder_id,  Unset):
            holder_id = UNSET
        else:
            holder_id = UUID(_holder_id)




        tenant_request = cls(
            name=name,
            external_id=external_id,
            holder_id=holder_id,
        )


        tenant_request.additional_properties = d
        return tenant_request

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
