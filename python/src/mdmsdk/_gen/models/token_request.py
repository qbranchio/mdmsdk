from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.token_request_permissions_item import TokenRequestPermissionsItem
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="TokenRequest")



@_attrs_define
class TokenRequest:
    """ 
        Attributes:
            permissions (list[TokenRequestPermissionsItem]):
            subject (str): The account's id for its user; recorded, never interpreted.
            tenant (str): The tenant id, or `ext:` and the account's external id for it.
            all_ (bool | Unset):
            groups (list[UUID] | Unset):
            members (list[str] | Unset): Member ids or `ext:` references. Exactly one of members, groups, and all.
            ttl (int | Unset): Seconds; 900 when absent.
     """

    permissions: list[TokenRequestPermissionsItem]
    subject: str
    tenant: str
    all_: bool | Unset = UNSET
    groups: list[UUID] | Unset = UNSET
    members: list[str] | Unset = UNSET
    ttl: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.value
            permissions.append(permissions_item)



        subject = self.subject

        tenant = self.tenant

        all_ = self.all_

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = str(groups_item_data)
                groups.append(groups_item)



        members: list[str] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members



        ttl = self.ttl


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "permissions": permissions,
            "subject": subject,
            "tenant": tenant,
        })
        if all_ is not UNSET:
            field_dict["all"] = all_
        if groups is not UNSET:
            field_dict["groups"] = groups
        if members is not UNSET:
            field_dict["members"] = members
        if ttl is not UNSET:
            field_dict["ttl"] = ttl

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in (_permissions):
            permissions_item = TokenRequestPermissionsItem(permissions_item_data)



            permissions.append(permissions_item)


        subject = d.pop("subject")

        tenant = d.pop("tenant")

        all_ = d.pop("all", UNSET)

        _groups = d.pop("groups", UNSET)
        groups: list[UUID] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = UUID(groups_item_data)



                groups.append(groups_item)


        members = cast(list[str], d.pop("members", UNSET))


        ttl = d.pop("ttl", UNSET)

        token_request = cls(
            permissions=permissions,
            subject=subject,
            tenant=tenant,
            all_=all_,
            groups=groups,
            members=members,
            ttl=ttl,
        )


        token_request.additional_properties = d
        return token_request

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
