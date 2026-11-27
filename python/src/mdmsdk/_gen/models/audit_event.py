from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="AuditEvent")



@_attrs_define
class AuditEvent:
    """ 
        Attributes:
            action (str): The operation id; filter with `action`.
            actor_display (str): A person's name (read from Auth0, else their subject), an account client's name or id,
                "Platform" (a platform admin's name for platform admins), "CLI", or an invitee's invited name.
            actor_kind (str): admin, console, account, delegated, platform_admin, cli, or invitee.
            actor_subject (str): The token's subject; filter with `actor`.
            at (datetime.datetime):
            id (str): The event's id, stable.
            scope (str): platform, account, or tenant.
            summary (str): What was done, without who ("Sent Lock to Front desk iPad 2").
            account_id (UUID | Unset):
            resource_id (str | Unset):
            resource_type (str | Unset):
            tenant_id (UUID | Unset):
     """

    action: str
    actor_display: str
    actor_kind: str
    actor_subject: str
    at: datetime.datetime
    id: str
    scope: str
    summary: str
    account_id: UUID | Unset = UNSET
    resource_id: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    tenant_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        action = self.action

        actor_display = self.actor_display

        actor_kind = self.actor_kind

        actor_subject = self.actor_subject

        at = self.at.isoformat()

        id = self.id

        scope = self.scope

        summary = self.summary

        account_id: str | Unset = UNSET
        if not isinstance(self.account_id, Unset):
            account_id = str(self.account_id)

        resource_id = self.resource_id

        resource_type = self.resource_type

        tenant_id: str | Unset = UNSET
        if not isinstance(self.tenant_id, Unset):
            tenant_id = str(self.tenant_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
            "actor_display": actor_display,
            "actor_kind": actor_kind,
            "actor_subject": actor_subject,
            "at": at,
            "id": id,
            "scope": scope,
            "summary": summary,
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        actor_display = d.pop("actor_display")

        actor_kind = d.pop("actor_kind")

        actor_subject = d.pop("actor_subject")

        at = datetime.datetime.fromisoformat(d.pop("at"))




        id = d.pop("id")

        scope = d.pop("scope")

        summary = d.pop("summary")

        _account_id = d.pop("account_id", UNSET)
        account_id: UUID | Unset
        if isinstance(_account_id,  Unset):
            account_id = UNSET
        else:
            account_id = UUID(_account_id)




        resource_id = d.pop("resource_id", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        _tenant_id = d.pop("tenant_id", UNSET)
        tenant_id: UUID | Unset
        if isinstance(_tenant_id,  Unset):
            tenant_id = UNSET
        else:
            tenant_id = UUID(_tenant_id)




        audit_event = cls(
            action=action,
            actor_display=actor_display,
            actor_kind=actor_kind,
            actor_subject=actor_subject,
            at=at,
            id=id,
            scope=scope,
            summary=summary,
            account_id=account_id,
            resource_id=resource_id,
            resource_type=resource_type,
            tenant_id=tenant_id,
        )


        audit_event.additional_properties = d
        return audit_event

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
