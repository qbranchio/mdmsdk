from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HolderPush")



@_attrs_define
class HolderPush:
    """ 
        Attributes:
            request_pending (bool): A request awaits the certificate Apple issues for it.
            not_after (datetime.datetime | Unset):
            topic (str | Unset):
     """

    request_pending: bool
    not_after: datetime.datetime | Unset = UNSET
    topic: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        request_pending = self.request_pending

        not_after: str | Unset = UNSET
        if not isinstance(self.not_after, Unset):
            not_after = self.not_after.isoformat()

        topic = self.topic


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "request_pending": request_pending,
        })
        if not_after is not UNSET:
            field_dict["not_after"] = not_after
        if topic is not UNSET:
            field_dict["topic"] = topic

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        request_pending = d.pop("request_pending")

        _not_after = d.pop("not_after", UNSET)
        not_after: datetime.datetime | Unset
        if isinstance(_not_after,  Unset):
            not_after = UNSET
        else:
            not_after = datetime.datetime.fromisoformat(_not_after)




        topic = d.pop("topic", UNSET)

        holder_push = cls(
            request_pending=request_pending,
            not_after=not_after,
            topic=topic,
        )


        holder_push.additional_properties = d
        return holder_push

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
