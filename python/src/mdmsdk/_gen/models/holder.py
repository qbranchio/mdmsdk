from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.holder_ade import HolderADE
  from ..models.holder_push import HolderPush
  from ..models.holder_vpp import HolderVPP





T = TypeVar("T", bound="Holder")



@_attrs_define
class Holder:
    """ 
        Attributes:
            ade (HolderADE):
            created_at (datetime.datetime):
            id (UUID):
            is_default (bool):
            legal_name (str):
            name (str):
            push (HolderPush):
            updated_at (datetime.datetime):
            vpp (HolderVPP):
     """

    ade: HolderADE
    created_at: datetime.datetime
    id: UUID
    is_default: bool
    legal_name: str
    name: str
    push: HolderPush
    updated_at: datetime.datetime
    vpp: HolderVPP
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.holder_ade import HolderADE # noqa: PLC0415
        from ..models.holder_push import HolderPush # noqa: PLC0415
        from ..models.holder_vpp import HolderVPP # noqa: PLC0415
        ade = self.ade.to_dict()

        created_at = self.created_at.isoformat()

        id = str(self.id)

        is_default = self.is_default

        legal_name = self.legal_name

        name = self.name

        push = self.push.to_dict()

        updated_at = self.updated_at.isoformat()

        vpp = self.vpp.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ade": ade,
            "created_at": created_at,
            "id": id,
            "is_default": is_default,
            "legal_name": legal_name,
            "name": name,
            "push": push,
            "updated_at": updated_at,
            "vpp": vpp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.holder_ade import HolderADE # noqa: PLC0415
        from ..models.holder_push import HolderPush # noqa: PLC0415
        from ..models.holder_vpp import HolderVPP # noqa: PLC0415
        d = dict(src_dict)
        ade = HolderADE.from_dict(d.pop("ade"))




        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = UUID(d.pop("id"))




        is_default = d.pop("is_default")

        legal_name = d.pop("legal_name")

        name = d.pop("name")

        push = HolderPush.from_dict(d.pop("push"))




        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        vpp = HolderVPP.from_dict(d.pop("vpp"))




        holder = cls(
            ade=ade,
            created_at=created_at,
            id=id,
            is_default=is_default,
            legal_name=legal_name,
            name=name,
            push=push,
            updated_at=updated_at,
            vpp=vpp,
        )


        holder.additional_properties = d
        return holder

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
