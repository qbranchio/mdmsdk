from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.effective_policy_status import EffectivePolicyStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.effective_item import EffectiveItem





T = TypeVar("T", bound="EffectivePolicy")



@_attrs_define
class EffectivePolicy:
    """ 
        Attributes:
            items (list[EffectiveItem]): Empty while the policy is being removed.
            revision (int | Unset): The effective policy's revision. Absent when the device has none.
            status (EffectivePolicyStatus | Unset): Absent when the device has no policy.
     """

    items: list[EffectiveItem]
    revision: int | Unset = UNSET
    status: EffectivePolicyStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.effective_item import EffectiveItem # noqa: PLC0415
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)



        revision = self.revision

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "items": items,
        })
        if revision is not UNSET:
            field_dict["revision"] = revision
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.effective_item import EffectiveItem # noqa: PLC0415
        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in (_items):
            items_item = EffectiveItem.from_dict(items_item_data)



            items.append(items_item)


        revision = d.pop("revision", UNSET)

        _status = d.pop("status", UNSET)
        status: EffectivePolicyStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = EffectivePolicyStatus(_status)




        effective_policy = cls(
            items=items,
            revision=revision,
            status=status,
        )


        effective_policy.additional_properties = d
        return effective_policy

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
