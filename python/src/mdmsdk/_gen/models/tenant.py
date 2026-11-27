from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tenant_role import TenantRole
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.licence import Licence





T = TypeVar("T", bound="Tenant")



@_attrs_define
class Tenant:
    """ 
        Attributes:
            created_at (datetime.datetime):
            id (UUID):
            name (str):
            deleting_since (datetime.datetime | None | Unset): When its deletion started; null otherwise.
            external_id (str | Unset):
            holder_id (None | Unset | UUID): The tenant's credential holder; null when it uses the account's default.
            licence (Licence | Unset):
            min_os (None | str | Unset): The iOS version its devices must reach; null when the latest for each model.
            role (TenantRole | Unset): The caller's role, for an admin app token only.
     """

    created_at: datetime.datetime
    id: UUID
    name: str
    deleting_since: datetime.datetime | None | Unset = UNSET
    external_id: str | Unset = UNSET
    holder_id: None | Unset | UUID = UNSET
    licence: Licence | Unset = UNSET
    min_os: None | str | Unset = UNSET
    role: TenantRole | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.licence import Licence # noqa: PLC0415
        created_at = self.created_at.isoformat()

        id = str(self.id)

        name = self.name

        deleting_since: None | str | Unset
        if isinstance(self.deleting_since, Unset):
            deleting_since = UNSET
        elif isinstance(self.deleting_since, datetime.datetime):
            deleting_since = self.deleting_since.isoformat()
        else:
            deleting_since = self.deleting_since

        external_id = self.external_id

        holder_id: None | str | Unset
        if isinstance(self.holder_id, Unset):
            holder_id = UNSET
        elif isinstance(self.holder_id, UUID):
            holder_id = str(self.holder_id)
        else:
            holder_id = self.holder_id

        licence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.licence, Unset):
            licence = self.licence.to_dict()

        min_os: None | str | Unset
        if isinstance(self.min_os, Unset):
            min_os = UNSET
        else:
            min_os = self.min_os

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "id": id,
            "name": name,
        })
        if deleting_since is not UNSET:
            field_dict["deleting_since"] = deleting_since
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if holder_id is not UNSET:
            field_dict["holder_id"] = holder_id
        if licence is not UNSET:
            field_dict["licence"] = licence
        if min_os is not UNSET:
            field_dict["min_os"] = min_os
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.licence import Licence # noqa: PLC0415
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = UUID(d.pop("id"))




        name = d.pop("name")

        def _parse_deleting_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleting_since_type_1 = datetime.datetime.fromisoformat(data)



                return deleting_since_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleting_since = _parse_deleting_since(d.pop("deleting_since", UNSET))


        external_id = d.pop("external_id", UNSET)

        def _parse_holder_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                holder_id_type_1 = UUID(data)



                return holder_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        holder_id = _parse_holder_id(d.pop("holder_id", UNSET))


        _licence = d.pop("licence", UNSET)
        licence: Licence | Unset
        if isinstance(_licence,  Unset):
            licence = UNSET
        else:
            licence = Licence.from_dict(_licence)




        def _parse_min_os(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        min_os = _parse_min_os(d.pop("min_os", UNSET))


        _role = d.pop("role", UNSET)
        role: TenantRole | Unset
        if isinstance(_role,  Unset):
            role = UNSET
        else:
            role = TenantRole(_role)




        tenant = cls(
            created_at=created_at,
            id=id,
            name=name,
            deleting_since=deleting_since,
            external_id=external_id,
            holder_id=holder_id,
            licence=licence,
            min_os=min_os,
            role=role,
        )


        tenant.additional_properties = d
        return tenant

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
