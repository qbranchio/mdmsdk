from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.declaration_reason import DeclarationReason





T = TypeVar("T", bound="DeclarationState")



@_attrs_define
class DeclarationState:
    """ 
        Attributes:
            active (bool):
            identifier (str):
            reasons (list[DeclarationReason]):
            reported_token (None | str): The version the device last reported. Null before it reports.
            server_token (str): The current version.
            valid (str): Apple's value (valid, invalid, unknown), or unknown before a report.
     """

    active: bool
    identifier: str
    reasons: list[DeclarationReason]
    reported_token: None | str
    server_token: str
    valid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.declaration_reason import DeclarationReason # noqa: PLC0415
        active = self.active

        identifier = self.identifier

        reasons = []
        for reasons_item_data in self.reasons:
            reasons_item = reasons_item_data.to_dict()
            reasons.append(reasons_item)



        reported_token: None | str
        reported_token = self.reported_token

        server_token = self.server_token

        valid = self.valid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "active": active,
            "identifier": identifier,
            "reasons": reasons,
            "reported_token": reported_token,
            "server_token": server_token,
            "valid": valid,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.declaration_reason import DeclarationReason # noqa: PLC0415
        d = dict(src_dict)
        active = d.pop("active")

        identifier = d.pop("identifier")

        reasons = []
        _reasons = d.pop("reasons")
        for reasons_item_data in (_reasons):
            reasons_item = DeclarationReason.from_dict(reasons_item_data)



            reasons.append(reasons_item)


        def _parse_reported_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reported_token = _parse_reported_token(d.pop("reported_token"))


        server_token = d.pop("server_token")

        valid = d.pop("valid")

        declaration_state = cls(
            active=active,
            identifier=identifier,
            reasons=reasons,
            reported_token=reported_token,
            server_token=server_token,
            valid=valid,
        )


        declaration_state.additional_properties = d
        return declaration_state

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
