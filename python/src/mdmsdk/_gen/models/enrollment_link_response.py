from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.device import Device





T = TypeVar("T", bound="EnrollmentLinkResponse")



@_attrs_define
class EnrollmentLinkResponse:
    """ 
        Attributes:
            device (Device):
            enrollment_profile (str): The unsigned .mobileconfig the link serves, base64 encoded.
            expires_at (datetime.datetime):
            url (str): The public link. Treat it as a secret until it expires.
     """

    device: Device
    enrollment_profile: str
    expires_at: datetime.datetime
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.device import Device # noqa: PLC0415
        device = self.device.to_dict()

        enrollment_profile = self.enrollment_profile

        expires_at = self.expires_at.isoformat()

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "device": device,
            "enrollment_profile": enrollment_profile,
            "expires_at": expires_at,
            "url": url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device import Device # noqa: PLC0415
        d = dict(src_dict)
        device = Device.from_dict(d.pop("device"))




        enrollment_profile = d.pop("enrollment_profile")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))




        url = d.pop("url")

        enrollment_link_response = cls(
            device=device,
            enrollment_profile=enrollment_profile,
            expires_at=expires_at,
            url=url,
        )


        enrollment_link_response.additional_properties = d
        return enrollment_link_response

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
