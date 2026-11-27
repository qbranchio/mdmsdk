from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID






T = TypeVar("T", bound="DeviceOSBehindData")



@_attrs_define
class DeviceOSBehindData:
    """ 
        Attributes:
            device_id (UUID):
            latest_version (None | str): The newest iOS Apple publishes for its model; null when unknown.
            member_id (None | UUID): The member who owns the device; null when it is the tenant's.
            minimum_version (None | str): The tenant's minimum iOS version; null when it sets none.
            os_version (str): The iOS version the device runs.
            tenant_external_id (None | str): The account's own id for the tenant; null when it has none.
            tenant_id (UUID):
     """

    device_id: UUID
    latest_version: None | str
    member_id: None | UUID
    minimum_version: None | str
    os_version: str
    tenant_external_id: None | str
    tenant_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        device_id = str(self.device_id)

        latest_version: None | str
        latest_version = self.latest_version

        member_id: None | str
        if isinstance(self.member_id, UUID):
            member_id = str(self.member_id)
        else:
            member_id = self.member_id

        minimum_version: None | str
        minimum_version = self.minimum_version

        os_version = self.os_version

        tenant_external_id: None | str
        tenant_external_id = self.tenant_external_id

        tenant_id = str(self.tenant_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "device_id": device_id,
            "latest_version": latest_version,
            "member_id": member_id,
            "minimum_version": minimum_version,
            "os_version": os_version,
            "tenant_external_id": tenant_external_id,
            "tenant_id": tenant_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_id = UUID(d.pop("device_id"))




        def _parse_latest_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latest_version = _parse_latest_version(d.pop("latest_version"))


        def _parse_member_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                member_id_type_1 = UUID(data)



                return member_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        member_id = _parse_member_id(d.pop("member_id"))


        def _parse_minimum_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        minimum_version = _parse_minimum_version(d.pop("minimum_version"))


        os_version = d.pop("os_version")

        def _parse_tenant_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tenant_external_id = _parse_tenant_external_id(d.pop("tenant_external_id"))


        tenant_id = UUID(d.pop("tenant_id"))




        device_os_behind_data = cls(
            device_id=device_id,
            latest_version=latest_version,
            member_id=member_id,
            minimum_version=minimum_version,
            os_version=os_version,
            tenant_external_id=tenant_external_id,
            tenant_id=tenant_id,
        )


        device_os_behind_data.additional_properties = d
        return device_os_behind_data

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
