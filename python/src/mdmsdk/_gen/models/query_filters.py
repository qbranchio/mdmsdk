from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.query_filters_category_item import QueryFiltersCategoryItem
from ..models.query_filters_state_item import QueryFiltersStateItem
from ..models.query_filters_supervised_item import QueryFiltersSupervisedItem
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="QueryFilters")



@_attrs_define
class QueryFilters:
    """ Each filter is a list the value must be in. activity takes `category` and `actor`; devices takes `state` and
    `supervised`.

        Attributes:
            actor (list[str] | Unset): Actor subjects.
            category (list[QueryFiltersCategoryItem] | Unset):
            state (list[QueryFiltersStateItem] | Unset):
            supervised (list[QueryFiltersSupervisedItem] | Unset):
     """

    actor: list[str] | Unset = UNSET
    category: list[QueryFiltersCategoryItem] | Unset = UNSET
    state: list[QueryFiltersStateItem] | Unset = UNSET
    supervised: list[QueryFiltersSupervisedItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        actor: list[str] | Unset = UNSET
        if not isinstance(self.actor, Unset):
            actor = self.actor



        category: list[str] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item = category_item_data.value
                category.append(category_item)



        state: list[str] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = []
            for state_item_data in self.state:
                state_item = state_item_data.value
                state.append(state_item)



        supervised: list[str] | Unset = UNSET
        if not isinstance(self.supervised, Unset):
            supervised = []
            for supervised_item_data in self.supervised:
                supervised_item = supervised_item_data.value
                supervised.append(supervised_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if actor is not UNSET:
            field_dict["actor"] = actor
        if category is not UNSET:
            field_dict["category"] = category
        if state is not UNSET:
            field_dict["state"] = state
        if supervised is not UNSET:
            field_dict["supervised"] = supervised

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        actor = cast(list[str], d.pop("actor", UNSET))


        _category = d.pop("category", UNSET)
        category: list[QueryFiltersCategoryItem] | Unset = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = QueryFiltersCategoryItem(category_item_data)



                category.append(category_item)


        _state = d.pop("state", UNSET)
        state: list[QueryFiltersStateItem] | Unset = UNSET
        if _state is not UNSET:
            state = []
            for state_item_data in _state:
                state_item = QueryFiltersStateItem(state_item_data)



                state.append(state_item)


        _supervised = d.pop("supervised", UNSET)
        supervised: list[QueryFiltersSupervisedItem] | Unset = UNSET
        if _supervised is not UNSET:
            supervised = []
            for supervised_item_data in _supervised:
                supervised_item = QueryFiltersSupervisedItem(supervised_item_data)



                supervised.append(supervised_item)


        query_filters = cls(
            actor=actor,
            category=category,
            state=state,
            supervised=supervised,
        )


        query_filters.additional_properties = d
        return query_filters

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
