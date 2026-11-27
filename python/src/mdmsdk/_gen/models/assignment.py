from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.assignment_levels_item import AssignmentLevelsItem
from ..models.assignment_target import AssignmentTarget
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="Assignment")



@_attrs_define
class Assignment:
    """ 
        Attributes:
            created_at (datetime.datetime):
            id (UUID):
            levels (list[AssignmentLevelsItem]):
            profile_id (UUID):
            target (AssignmentTarget):
            target_id (None | UUID): The group, member, or device id. Null for the tenant.
     """

    created_at: datetime.datetime
    id: UUID
    levels: list[AssignmentLevelsItem]
    profile_id: UUID
    target: AssignmentTarget
    target_id: None | UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = str(self.id)

        levels = []
        for levels_item_data in self.levels:
            levels_item = levels_item_data.value
            levels.append(levels_item)



        profile_id = str(self.profile_id)

        target = self.target.value

        target_id: None | str
        if isinstance(self.target_id, UUID):
            target_id = str(self.target_id)
        else:
            target_id = self.target_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "id": id,
            "levels": levels,
            "profile_id": profile_id,
            "target": target,
            "target_id": target_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = UUID(d.pop("id"))




        levels = []
        _levels = d.pop("levels")
        for levels_item_data in (_levels):
            levels_item = AssignmentLevelsItem(levels_item_data)



            levels.append(levels_item)


        profile_id = UUID(d.pop("profile_id"))




        target = AssignmentTarget(d.pop("target"))




        def _parse_target_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_id_type_1 = UUID(data)



                return target_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        target_id = _parse_target_id(d.pop("target_id"))


        assignment = cls(
            created_at=created_at,
            id=id,
            levels=levels,
            profile_id=profile_id,
            target=target,
            target_id=target_id,
        )


        assignment.additional_properties = d
        return assignment

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
