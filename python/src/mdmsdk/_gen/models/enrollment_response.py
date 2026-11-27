from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.device import Device





T = TypeVar("T", bound="EnrollmentResponse")



@_attrs_define
class EnrollmentResponse:
    """ 
        Attributes:
            device (Device):
            enrollment_profile (str): The unsigned .mobileconfig, base64 encoded.
     """

    device: Device
    enrollment_profile: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.device import Device # noqa: PLC0415
        device = self.device.to_dict()

        enrollment_profile = self.enrollment_profile


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "device": device,
            "enrollment_profile": enrollment_profile,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device import Device # noqa: PLC0415
        d = dict(src_dict)
        device = Device.from_dict(d.pop("device"))




        enrollment_profile = d.pop("enrollment_profile")

        enrollment_response = cls(
            device=device,
            enrollment_profile=enrollment_profile,
        )


        enrollment_response.additional_properties = d
        return enrollment_response

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
