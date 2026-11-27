from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.device_status import DeviceStatus
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.device_policy import DevicePolicy
  from ..models.item_status import ItemStatus





T = TypeVar("T", bound="Device")



@_attrs_define
class Device:
    """ 
        Attributes:
            created_at (datetime.datetime):
            enrollment_id (None | str): The enrollment ID bound to this device.
            id (UUID):
            last_seen_at (datetime.datetime | None):
            member_id (None | UUID): The member who owns the device. Null when it is the tenant's.
            model (None | str):
            name (str):
            os_behind (bool): Below its tenant's minimum, or below os_latest when the tenant sets none.
            os_latest (None | str): The newest iOS Apple publishes for its model, from the daily check.
            os_version (None | str):
            policy (DevicePolicy | None):
            serial_number (None | str):
            settings (list[ItemStatus]): One status per policy item, in policy order. Empty without a policy.
            status (DeviceStatus):
            supervised (bool | None): The level, from the current DeviceInformation IsSupervised. Null until reported, and
                again on each new enrollment until reported.
            udid (None | str):
     """

    created_at: datetime.datetime
    enrollment_id: None | str
    id: UUID
    last_seen_at: datetime.datetime | None
    member_id: None | UUID
    model: None | str
    name: str
    os_behind: bool
    os_latest: None | str
    os_version: None | str
    policy: DevicePolicy | None
    serial_number: None | str
    settings: list[ItemStatus]
    status: DeviceStatus
    supervised: bool | None
    udid: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.device_policy import DevicePolicy # noqa: PLC0415
        from ..models.item_status import ItemStatus # noqa: PLC0415
        created_at = self.created_at.isoformat()

        enrollment_id: None | str
        enrollment_id = self.enrollment_id

        id = str(self.id)

        last_seen_at: None | str
        if isinstance(self.last_seen_at, datetime.datetime):
            last_seen_at = self.last_seen_at.isoformat()
        else:
            last_seen_at = self.last_seen_at

        member_id: None | str
        if isinstance(self.member_id, UUID):
            member_id = str(self.member_id)
        else:
            member_id = self.member_id

        model: None | str
        model = self.model

        name = self.name

        os_behind = self.os_behind

        os_latest: None | str
        os_latest = self.os_latest

        os_version: None | str
        os_version = self.os_version

        policy: dict[str, Any] | None
        if isinstance(self.policy, DevicePolicy):
            policy = self.policy.to_dict()
        else:
            policy = self.policy

        serial_number: None | str
        serial_number = self.serial_number

        settings = []
        for settings_item_data in self.settings:
            settings_item = settings_item_data.to_dict()
            settings.append(settings_item)



        status = self.status.value

        supervised: bool | None
        supervised = self.supervised

        udid: None | str
        udid = self.udid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "enrollment_id": enrollment_id,
            "id": id,
            "last_seen_at": last_seen_at,
            "member_id": member_id,
            "model": model,
            "name": name,
            "os_behind": os_behind,
            "os_latest": os_latest,
            "os_version": os_version,
            "policy": policy,
            "serial_number": serial_number,
            "settings": settings,
            "status": status,
            "supervised": supervised,
            "udid": udid,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_policy import DevicePolicy # noqa: PLC0415
        from ..models.item_status import ItemStatus # noqa: PLC0415
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        def _parse_enrollment_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        enrollment_id = _parse_enrollment_id(d.pop("enrollment_id"))


        id = UUID(d.pop("id"))




        def _parse_last_seen_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_at_type_1 = datetime.datetime.fromisoformat(data)



                return last_seen_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_seen_at = _parse_last_seen_at(d.pop("last_seen_at"))


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


        def _parse_model(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        model = _parse_model(d.pop("model"))


        name = d.pop("name")

        os_behind = d.pop("os_behind")

        def _parse_os_latest(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        os_latest = _parse_os_latest(d.pop("os_latest"))


        def _parse_os_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        os_version = _parse_os_version(d.pop("os_version"))


        def _parse_policy(data: object) -> DevicePolicy | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                policy_type_0 = DevicePolicy.from_dict(data)



                return policy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DevicePolicy | None, data)

        policy = _parse_policy(d.pop("policy"))


        def _parse_serial_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        serial_number = _parse_serial_number(d.pop("serial_number"))


        settings = []
        _settings = d.pop("settings")
        for settings_item_data in (_settings):
            settings_item = ItemStatus.from_dict(settings_item_data)



            settings.append(settings_item)


        status = DeviceStatus(d.pop("status"))




        def _parse_supervised(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        supervised = _parse_supervised(d.pop("supervised"))


        def _parse_udid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        udid = _parse_udid(d.pop("udid"))


        device = cls(
            created_at=created_at,
            enrollment_id=enrollment_id,
            id=id,
            last_seen_at=last_seen_at,
            member_id=member_id,
            model=model,
            name=name,
            os_behind=os_behind,
            os_latest=os_latest,
            os_version=os_version,
            policy=policy,
            serial_number=serial_number,
            settings=settings,
            status=status,
            supervised=supervised,
            udid=udid,
        )


        device.additional_properties = d
        return device

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
