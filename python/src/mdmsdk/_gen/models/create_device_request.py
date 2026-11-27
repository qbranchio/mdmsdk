from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.policy import Policy





T = TypeVar("T", bound="CreateDeviceRequest")



@_attrs_define
class CreateDeviceRequest:
    """ 
        Attributes:
            name (str):
            member (str | Unset): The member who owns the device: a member id, or `ext:` and the account's id for the
                member. Without it the device is the tenant's.
            settings (Policy | Unset): Settings: items from the catalog (GET /api/v1/catalog). Items a device's level or OS
                cannot take are left out of its declarations and reported unsupported. Secret keys (marked in the catalog) are
                write-only: responses show {"secret": "set"}; a PUT that sends it keeps the stored value, a string replaces it,
                and leaving the key out clears it.
     """

    name: str
    member: str | Unset = UNSET
    settings: Policy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy import Policy # noqa: PLC0415
        name = self.name

        member = self.member

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if member is not UNSET:
            field_dict["member"] = member
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy import Policy # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        member = d.pop("member", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Policy | Unset
        if isinstance(_settings,  Unset):
            settings = UNSET
        else:
            settings = Policy.from_dict(_settings)




        create_device_request = cls(
            name=name,
            member=member,
            settings=settings,
        )


        create_device_request.additional_properties = d
        return create_device_request

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
