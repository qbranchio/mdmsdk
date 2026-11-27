from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.policy_item import PolicyItem
  from ..models.source import Source





T = TypeVar("T", bound="EffectiveItem")



@_attrs_define
class EffectiveItem:
    """ 
        Attributes:
            conflicts (list[Source]): Sources in the same layer that set the same item and lost to the lower profile id.
            item (PolicyItem):
            overridden (list[Source]): Less specific sources (or lower priority groups) that set the same item.
            source (Source):
     """

    conflicts: list[Source]
    item: PolicyItem
    overridden: list[Source]
    source: Source
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_item import PolicyItem # noqa: PLC0415
        from ..models.source import Source # noqa: PLC0415
        conflicts = []
        for conflicts_item_data in self.conflicts:
            conflicts_item = conflicts_item_data.to_dict()
            conflicts.append(conflicts_item)



        item = self.item.to_dict()

        overridden = []
        for overridden_item_data in self.overridden:
            overridden_item = overridden_item_data.to_dict()
            overridden.append(overridden_item)



        source = self.source.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "conflicts": conflicts,
            "item": item,
            "overridden": overridden,
            "source": source,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_item import PolicyItem # noqa: PLC0415
        from ..models.source import Source # noqa: PLC0415
        d = dict(src_dict)
        conflicts = []
        _conflicts = d.pop("conflicts")
        for conflicts_item_data in (_conflicts):
            conflicts_item = Source.from_dict(conflicts_item_data)



            conflicts.append(conflicts_item)


        item = PolicyItem.from_dict(d.pop("item"))




        overridden = []
        _overridden = d.pop("overridden")
        for overridden_item_data in (_overridden):
            overridden_item = Source.from_dict(overridden_item_data)



            overridden.append(overridden_item)


        source = Source.from_dict(d.pop("source"))




        effective_item = cls(
            conflicts=conflicts,
            item=item,
            overridden=overridden,
            source=source,
        )


        effective_item.additional_properties = d
        return effective_item

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
