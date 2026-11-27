from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.device_policy_status_data_status import DevicePolicyStatusDataStatus
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="DevicePolicyStatusData")



@_attrs_define
class DevicePolicyStatusData:
    """ 
        Attributes:
            device_id (UUID):
            member_id (None | UUID): The member who owns the device; null when it is the tenant's.
            revision (int): The effective policy's revision.
            status (DevicePolicyStatusDataStatus): applied: the device reported the revision active. failed: it reported a
                declaration invalid. removed: the policy is gone from the device.
            tenant_external_id (None | str): The account's own id for the tenant; null when it has none.
            tenant_id (UUID):
     """

    device_id: UUID
    member_id: None | UUID
    revision: int
    status: DevicePolicyStatusDataStatus
    tenant_external_id: None | str
    tenant_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        device_id = str(self.device_id)

        member_id: None | str
        if isinstance(self.member_id, UUID):
            member_id = str(self.member_id)
        else:
            member_id = self.member_id

        revision = self.revision

        status = self.status.value

        tenant_external_id: None | str
        tenant_external_id = self.tenant_external_id

        tenant_id = str(self.tenant_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "device_id": device_id,
            "member_id": member_id,
            "revision": revision,
            "status": status,
            "tenant_external_id": tenant_external_id,
            "tenant_id": tenant_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_id = UUID(d.pop("device_id"))




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


        revision = d.pop("revision")

        status = DevicePolicyStatusDataStatus(d.pop("status"))




        def _parse_tenant_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tenant_external_id = _parse_tenant_external_id(d.pop("tenant_external_id"))


        tenant_id = UUID(d.pop("tenant_id"))




        device_policy_status_data = cls(
            device_id=device_id,
            member_id=member_id,
            revision=revision,
            status=status,
            tenant_external_id=tenant_external_id,
            tenant_id=tenant_id,
        )


        device_policy_status_data.additional_properties = d
        return device_policy_status_data

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
