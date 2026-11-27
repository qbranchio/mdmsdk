from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID






T = TypeVar("T", bound="Account")



@_attrs_define
class Account:
    """ 
        Attributes:
            clients (list[str]): Its Auth0 API client ids.
            contact_email (str):
            id (UUID):
            name (str):
            origins (list[str]): Browser origins its users call the API from with delegated tokens.
     """

    clients: list[str]
    contact_email: str
    id: UUID
    name: str
    origins: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        clients = self.clients



        contact_email = self.contact_email

        id = str(self.id)

        name = self.name

        origins = self.origins




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "clients": clients,
            "contact_email": contact_email,
            "id": id,
            "name": name,
            "origins": origins,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        clients = cast(list[str], d.pop("clients"))


        contact_email = d.pop("contact_email")

        id = UUID(d.pop("id"))




        name = d.pop("name")

        origins = cast(list[str], d.pop("origins"))


        account = cls(
            clients=clients,
            contact_email=contact_email,
            id=id,
            name=name,
            origins=origins,
        )


        account.additional_properties = d
        return account

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
