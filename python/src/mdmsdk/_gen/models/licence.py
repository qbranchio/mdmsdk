from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime






T = TypeVar("T", bound="Licence")



@_attrs_define
class Licence:
    """ 
        Attributes:
            devices_used (int):
            ends_at (datetime.datetime | None): When the licence expires; null is never. After it, adding devices, profiles,
                settings, assignments, members, and groups answers 409 licence_expired. Reads, removals, and DeviceLock keep
                working.
            expired (bool):
            max_devices (int | None): Registered and enrolled devices allowed; null is no limit. Adding one over it answers
                409 licence_exceeded.
            max_people (int | None): Organization members plus open invitations allowed; null is no limit.
            people_used (int | None): Members of the tenant's organization and open invitations; null when the members could
                not be counted (Auth0 failed or timed out), so the use is unknown rather than understated.
     """

    devices_used: int
    ends_at: datetime.datetime | None
    expired: bool
    max_devices: int | None
    max_people: int | None
    people_used: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        devices_used = self.devices_used

        ends_at: None | str
        if isinstance(self.ends_at, datetime.datetime):
            ends_at = self.ends_at.isoformat()
        else:
            ends_at = self.ends_at

        expired = self.expired

        max_devices: int | None
        max_devices = self.max_devices

        max_people: int | None
        max_people = self.max_people

        people_used: int | None
        people_used = self.people_used


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "devices_used": devices_used,
            "ends_at": ends_at,
            "expired": expired,
            "max_devices": max_devices,
            "max_people": max_people,
            "people_used": people_used,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        devices_used = d.pop("devices_used")

        def _parse_ends_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ends_at_type_1 = datetime.datetime.fromisoformat(data)



                return ends_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        ends_at = _parse_ends_at(d.pop("ends_at"))


        expired = d.pop("expired")

        def _parse_max_devices(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_devices = _parse_max_devices(d.pop("max_devices"))


        def _parse_max_people(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_people = _parse_max_people(d.pop("max_people"))


        def _parse_people_used(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        people_used = _parse_people_used(d.pop("people_used"))


        licence = cls(
            devices_used=devices_used,
            ends_at=ends_at,
            expired=expired,
            max_devices=max_devices,
            max_people=max_people,
            people_used=people_used,
        )


        licence.additional_properties = d
        return licence

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
