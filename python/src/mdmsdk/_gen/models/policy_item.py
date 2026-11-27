from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.policy_item_payload import PolicyItemPayload





T = TypeVar("T", bound="PolicyItem")



@_attrs_define
class PolicyItem:
    """ 
        Attributes:
            id (str): A catalog entry id, such as restriction:allowCamera.
            key (str | Unset): Names the instance of an entry that can be added more than once (multiple), such as one Wi-Fi
                network.
            payload (PolicyItemPayload | Unset): A profile payload's or declaration's keys, as the catalog describes them.
                Data keys are base64.
            value (Any | Unset): A restriction's value.
     """

    id: str
    key: str | Unset = UNSET
    payload: PolicyItemPayload | Unset = UNSET
    value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_item_payload import PolicyItemPayload # noqa: PLC0415
        id = self.id

        key = self.key

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
        })
        if key is not UNSET:
            field_dict["key"] = key
        if payload is not UNSET:
            field_dict["payload"] = payload
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_item_payload import PolicyItemPayload # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        key = d.pop("key", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: PolicyItemPayload | Unset
        if isinstance(_payload,  Unset):
            payload = UNSET
        else:
            payload = PolicyItemPayload.from_dict(_payload)




        value = d.pop("value", UNSET)

        policy_item = cls(
            id=id,
            key=key,
            payload=payload,
            value=value,
        )


        policy_item.additional_properties = d
        return policy_item

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
