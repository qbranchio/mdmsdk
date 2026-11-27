from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.me_kind import MeKind
from ..models.me_role import MeRole
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.account_ref import AccountRef
  from ..models.tenant import Tenant





T = TypeVar("T", bound="Me")



@_attrs_define
class Me:
    """ 
        Attributes:
            kind (MeKind):
            account (AccountRef | Unset):
            role (MeRole | Unset): For tenant_admin and account_admin.
            signed_in_at (datetime.datetime | Unset): For platform_admin, when the second-factor sign-in happened.
            tenant (Tenant | Unset):
     """

    kind: MeKind
    account: AccountRef | Unset = UNSET
    role: MeRole | Unset = UNSET
    signed_in_at: datetime.datetime | Unset = UNSET
    tenant: Tenant | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_ref import AccountRef # noqa: PLC0415
        from ..models.tenant import Tenant # noqa: PLC0415
        kind = self.kind.value

        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value


        signed_in_at: str | Unset = UNSET
        if not isinstance(self.signed_in_at, Unset):
            signed_in_at = self.signed_in_at.isoformat()

        tenant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tenant, Unset):
            tenant = self.tenant.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kind": kind,
        })
        if account is not UNSET:
            field_dict["account"] = account
        if role is not UNSET:
            field_dict["role"] = role
        if signed_in_at is not UNSET:
            field_dict["signed_in_at"] = signed_in_at
        if tenant is not UNSET:
            field_dict["tenant"] = tenant

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_ref import AccountRef # noqa: PLC0415
        from ..models.tenant import Tenant # noqa: PLC0415
        d = dict(src_dict)
        kind = MeKind(d.pop("kind"))




        _account = d.pop("account", UNSET)
        account: AccountRef | Unset
        if isinstance(_account,  Unset):
            account = UNSET
        else:
            account = AccountRef.from_dict(_account)




        _role = d.pop("role", UNSET)
        role: MeRole | Unset
        if isinstance(_role,  Unset):
            role = UNSET
        else:
            role = MeRole(_role)




        _signed_in_at = d.pop("signed_in_at", UNSET)
        signed_in_at: datetime.datetime | Unset
        if isinstance(_signed_in_at,  Unset):
            signed_in_at = UNSET
        else:
            signed_in_at = datetime.datetime.fromisoformat(_signed_in_at)




        _tenant = d.pop("tenant", UNSET)
        tenant: Tenant | Unset
        if isinstance(_tenant,  Unset):
            tenant = UNSET
        else:
            tenant = Tenant.from_dict(_tenant)




        me = cls(
            kind=kind,
            account=account,
            role=role,
            signed_in_at=signed_in_at,
            tenant=tenant,
        )


        me.additional_properties = d
        return me

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
