from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.assignment_request_levels_item import AssignmentRequestLevelsItem
from ..models.assignment_request_target import AssignmentRequestTarget
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AssignmentRequest")



@_attrs_define
class AssignmentRequest:
    """ 
        Attributes:
            levels (list[AssignmentRequestLevelsItem]):
            target (AssignmentRequestTarget):
            target_id (str | Unset): The group or device id, or the member id or `ext:` and the account's id for the member.
                Not set for the tenant.
     """

    levels: list[AssignmentRequestLevelsItem]
    target: AssignmentRequestTarget
    target_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        levels = []
        for levels_item_data in self.levels:
            levels_item = levels_item_data.value
            levels.append(levels_item)



        target = self.target.value

        target_id = self.target_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "levels": levels,
            "target": target,
        })
        if target_id is not UNSET:
            field_dict["target_id"] = target_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        levels = []
        _levels = d.pop("levels")
        for levels_item_data in (_levels):
            levels_item = AssignmentRequestLevelsItem(levels_item_data)



            levels.append(levels_item)


        target = AssignmentRequestTarget(d.pop("target"))




        target_id = d.pop("target_id", UNSET)

        assignment_request = cls(
            levels=levels,
            target=target,
            target_id=target_id,
        )


        assignment_request.additional_properties = d
        return assignment_request

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
