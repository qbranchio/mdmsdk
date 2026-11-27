from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.item_status_reason_type_1 import ItemStatusReasonType1
from ..models.item_status_reason_type_2_type_1 import ItemStatusReasonType2Type1
from ..models.item_status_reason_type_3_type_1 import ItemStatusReasonType3Type1
from ..models.item_status_status import ItemStatusStatus
from typing import cast






T = TypeVar("T", bound="ItemStatus")



@_attrs_define
class ItemStatus:
    """ 
        Attributes:
            id (str):
            key (None | str):
            min_os (None | str): The iOS version the item needs, with reason requires_os.
            reason (ItemStatusReasonType1 | ItemStatusReasonType2Type1 | ItemStatusReasonType3Type1 | None): Set when status
                is unsupported.
            ref (str): The item's id, or id#key for an item added more than once.
            status (ItemStatusStatus): Derived, first match wins: level or OS unknown, pending; OS below 17, unsupported;
                the item needs supervision or a newer OS, or every key it sets does, unsupported; policy removing, removing; the
                device's capabilities lack its declaration type, unsupported; the item's declarations reported for this
                revision, their state; policy applied for this revision and level, applied; otherwise pending.
     """

    id: str
    key: None | str
    min_os: None | str
    reason: ItemStatusReasonType1 | ItemStatusReasonType2Type1 | ItemStatusReasonType3Type1 | None
    ref: str
    status: ItemStatusStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key: None | str
        key = self.key

        min_os: None | str
        min_os = self.min_os

        reason: None | str
        if isinstance(self.reason, ItemStatusReasonType1):
            reason = self.reason.value
        elif isinstance(self.reason, ItemStatusReasonType2Type1):
            reason = self.reason.value
        elif isinstance(self.reason, ItemStatusReasonType3Type1):
            reason = self.reason.value
        else:
            reason = self.reason

        ref = self.ref

        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "key": key,
            "min_os": min_os,
            "reason": reason,
            "ref": ref,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key = _parse_key(d.pop("key"))


        def _parse_min_os(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        min_os = _parse_min_os(d.pop("min_os"))


        def _parse_reason(data: object) -> ItemStatusReasonType1 | ItemStatusReasonType2Type1 | ItemStatusReasonType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_1 = ItemStatusReasonType1(data)



                return reason_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_2_type_1 = ItemStatusReasonType2Type1(data)



                return reason_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_3_type_1 = ItemStatusReasonType3Type1(data)



                return reason_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ItemStatusReasonType1 | ItemStatusReasonType2Type1 | ItemStatusReasonType3Type1 | None, data)

        reason = _parse_reason(d.pop("reason"))


        ref = d.pop("ref")

        status = ItemStatusStatus(d.pop("status"))




        item_status = cls(
            id=id,
            key=key,
            min_os=min_os,
            reason=reason,
            ref=ref,
            status=status,
        )


        item_status.additional_properties = d
        return item_status

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
