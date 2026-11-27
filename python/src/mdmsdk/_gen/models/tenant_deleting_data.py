from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID






T = TypeVar("T", bound="TenantDeletingData")



@_attrs_define
class TenantDeletingData:
    """ 
        Attributes:
            tenant_external_id (None | str): The account's own id for the tenant; null when it has none.
            tenant_id (UUID):
     """

    tenant_external_id: None | str
    tenant_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tenant_external_id: None | str
        tenant_external_id = self.tenant_external_id

        tenant_id = str(self.tenant_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tenant_external_id": tenant_external_id,
            "tenant_id": tenant_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_tenant_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tenant_external_id = _parse_tenant_external_id(d.pop("tenant_external_id"))


        tenant_id = UUID(d.pop("tenant_id"))




        tenant_deleting_data = cls(
            tenant_external_id=tenant_external_id,
            tenant_id=tenant_id,
        )


        tenant_deleting_data.additional_properties = d
        return tenant_deleting_data

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
