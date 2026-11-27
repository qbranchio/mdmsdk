from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.device_policy_applied_level_type_1 import DevicePolicyAppliedLevelType1
from ..models.device_policy_applied_level_type_2_type_1 import DevicePolicyAppliedLevelType2Type1
from ..models.device_policy_applied_level_type_3_type_1 import DevicePolicyAppliedLevelType3Type1
from ..models.device_policy_install_level_type_1 import DevicePolicyInstallLevelType1
from ..models.device_policy_install_level_type_2_type_1 import DevicePolicyInstallLevelType2Type1
from ..models.device_policy_install_level_type_3_type_1 import DevicePolicyInstallLevelType3Type1
from ..models.device_policy_status import DevicePolicyStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.device_policy_error_type_0_item import DevicePolicyErrorType0Item





T = TypeVar("T", bound="DevicePolicy")



@_attrs_define
class DevicePolicy:
    """ The deployment of the device's effective policy. Its items are read with profiles:read: GET .../effective-policy
    (with provenance) and GET .../settings (the device's own).

        Attributes:
            applied_level (DevicePolicyAppliedLevelType1 | DevicePolicyAppliedLevelType2Type1 |
                DevicePolicyAppliedLevelType3Type1 | None): The level of the declarations the device last reported active.
            applied_revision (int | None): The revision the device last reported active. Null before that.
            error (list[DevicePolicyErrorType0Item] | None): The declarations the device reported invalid, with Apple's
                reason, when status is failed.
            install_generation (int): Increments on every deploy, including a rebuild for a changed level.
            install_level (DevicePolicyInstallLevelType1 | DevicePolicyInstallLevelType2Type1 |
                DevicePolicyInstallLevelType3Type1 | None): The level the current declarations were built for. Null before the
                first deploy.
            revision (int): The effective policy's revision. Increments whenever the merged result changes.
            status (DevicePolicyStatus):
     """

    applied_level: DevicePolicyAppliedLevelType1 | DevicePolicyAppliedLevelType2Type1 | DevicePolicyAppliedLevelType3Type1 | None
    applied_revision: int | None
    error: list[DevicePolicyErrorType0Item] | None
    install_generation: int
    install_level: DevicePolicyInstallLevelType1 | DevicePolicyInstallLevelType2Type1 | DevicePolicyInstallLevelType3Type1 | None
    revision: int
    status: DevicePolicyStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.device_policy_error_type_0_item import DevicePolicyErrorType0Item # noqa: PLC0415
        applied_level: None | str
        if isinstance(self.applied_level, DevicePolicyAppliedLevelType1):
            applied_level = self.applied_level.value
        elif isinstance(self.applied_level, DevicePolicyAppliedLevelType2Type1):
            applied_level = self.applied_level.value
        elif isinstance(self.applied_level, DevicePolicyAppliedLevelType3Type1):
            applied_level = self.applied_level.value
        else:
            applied_level = self.applied_level

        applied_revision: int | None
        applied_revision = self.applied_revision

        error: list[dict[str, Any]] | None
        if isinstance(self.error, list):
            error = []
            for error_type_0_item_data in self.error:
                error_type_0_item = error_type_0_item_data.to_dict()
                error.append(error_type_0_item)


        else:
            error = self.error

        install_generation = self.install_generation

        install_level: None | str
        if isinstance(self.install_level, DevicePolicyInstallLevelType1):
            install_level = self.install_level.value
        elif isinstance(self.install_level, DevicePolicyInstallLevelType2Type1):
            install_level = self.install_level.value
        elif isinstance(self.install_level, DevicePolicyInstallLevelType3Type1):
            install_level = self.install_level.value
        else:
            install_level = self.install_level

        revision = self.revision

        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "applied_level": applied_level,
            "applied_revision": applied_revision,
            "error": error,
            "install_generation": install_generation,
            "install_level": install_level,
            "revision": revision,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_policy_error_type_0_item import DevicePolicyErrorType0Item # noqa: PLC0415
        d = dict(src_dict)
        def _parse_applied_level(data: object) -> DevicePolicyAppliedLevelType1 | DevicePolicyAppliedLevelType2Type1 | DevicePolicyAppliedLevelType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applied_level_type_1 = DevicePolicyAppliedLevelType1(data)



                return applied_level_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applied_level_type_2_type_1 = DevicePolicyAppliedLevelType2Type1(data)



                return applied_level_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applied_level_type_3_type_1 = DevicePolicyAppliedLevelType3Type1(data)



                return applied_level_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DevicePolicyAppliedLevelType1 | DevicePolicyAppliedLevelType2Type1 | DevicePolicyAppliedLevelType3Type1 | None, data)

        applied_level = _parse_applied_level(d.pop("applied_level"))


        def _parse_applied_revision(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        applied_revision = _parse_applied_revision(d.pop("applied_revision"))


        def _parse_error(data: object) -> list[DevicePolicyErrorType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                error_type_0 = []
                _error_type_0 = data
                for error_type_0_item_data in (_error_type_0):
                    error_type_0_item = DevicePolicyErrorType0Item.from_dict(error_type_0_item_data)



                    error_type_0.append(error_type_0_item)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DevicePolicyErrorType0Item] | None, data)

        error = _parse_error(d.pop("error"))


        install_generation = d.pop("install_generation")

        def _parse_install_level(data: object) -> DevicePolicyInstallLevelType1 | DevicePolicyInstallLevelType2Type1 | DevicePolicyInstallLevelType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                install_level_type_1 = DevicePolicyInstallLevelType1(data)



                return install_level_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                install_level_type_2_type_1 = DevicePolicyInstallLevelType2Type1(data)



                return install_level_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                install_level_type_3_type_1 = DevicePolicyInstallLevelType3Type1(data)



                return install_level_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DevicePolicyInstallLevelType1 | DevicePolicyInstallLevelType2Type1 | DevicePolicyInstallLevelType3Type1 | None, data)

        install_level = _parse_install_level(d.pop("install_level"))


        revision = d.pop("revision")

        status = DevicePolicyStatus(d.pop("status"))




        device_policy = cls(
            applied_level=applied_level,
            applied_revision=applied_revision,
            error=error,
            install_generation=install_generation,
            install_level=install_level,
            revision=revision,
            status=status,
        )


        device_policy.additional_properties = d
        return device_policy

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
