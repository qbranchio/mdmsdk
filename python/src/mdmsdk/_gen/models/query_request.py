from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.query_request_bucket import QueryRequestBucket
from ..models.query_request_dataset import QueryRequestDataset
from ..models.query_request_group_by_item import QueryRequestGroupByItem
from ..models.query_request_measure import QueryRequestMeasure
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.query_filters import QueryFilters





T = TypeVar("T", bound="QueryRequest")



@_attrs_define
class QueryRequest:
    """ 
        Attributes:
            dataset (QueryRequestDataset):
            measure (QueryRequestMeasure):
            bucket (QueryRequestBucket | Unset): For a query with a time dimension, in UTC. Left out: hour up to 2 days, day
                up to 90 days, week beyond. At most 1000 buckets.
            filters (QueryFilters | Unset): Each filter is a list the value must be in. activity takes `category` and
                `actor`; devices takes `state` and `supervised`.
            from_ (datetime.datetime | Unset): Start of the range (inclusive); `to` minus 7 days when left out. Bounds the
                events of activity, and the creation of the devices of a query grouped by time; a devices query without time is
                the state now.
            group_by (list[QueryRequestGroupByItem] | Unset):
            limit (int | Unset): Rows, or with a time dimension series; 100 when left out. With a time dimension every
                bucket has a row for every series, zero where nothing happened.
            series (bool | Unset): Group by time bucket first.
            to (datetime.datetime | Unset): End of the range (exclusive); now when left out.
     """

    dataset: QueryRequestDataset
    measure: QueryRequestMeasure
    bucket: QueryRequestBucket | Unset = UNSET
    filters: QueryFilters | Unset = UNSET
    from_: datetime.datetime | Unset = UNSET
    group_by: list[QueryRequestGroupByItem] | Unset = UNSET
    limit: int | Unset = UNSET
    series: bool | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.query_filters import QueryFilters # noqa: PLC0415
        dataset = self.dataset.value

        measure = self.measure.value

        bucket: str | Unset = UNSET
        if not isinstance(self.bucket, Unset):
            bucket = self.bucket.value


        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        group_by: list[str] | Unset = UNSET
        if not isinstance(self.group_by, Unset):
            group_by = []
            for group_by_item_data in self.group_by:
                group_by_item = group_by_item_data.value
                group_by.append(group_by_item)



        limit = self.limit

        series = self.series

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "dataset": dataset,
            "measure": measure,
        })
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if filters is not UNSET:
            field_dict["filters"] = filters
        if from_ is not UNSET:
            field_dict["from"] = from_
        if group_by is not UNSET:
            field_dict["group_by"] = group_by
        if limit is not UNSET:
            field_dict["limit"] = limit
        if series is not UNSET:
            field_dict["series"] = series
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_filters import QueryFilters # noqa: PLC0415
        d = dict(src_dict)
        dataset = QueryRequestDataset(d.pop("dataset"))




        measure = QueryRequestMeasure(d.pop("measure"))




        _bucket = d.pop("bucket", UNSET)
        bucket: QueryRequestBucket | Unset
        if isinstance(_bucket,  Unset):
            bucket = UNSET
        else:
            bucket = QueryRequestBucket(_bucket)




        _filters = d.pop("filters", UNSET)
        filters: QueryFilters | Unset
        if isinstance(_filters,  Unset):
            filters = UNSET
        else:
            filters = QueryFilters.from_dict(_filters)




        _from_ = d.pop("from", UNSET)
        from_: datetime.datetime | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = datetime.datetime.fromisoformat(_from_)




        _group_by = d.pop("group_by", UNSET)
        group_by: list[QueryRequestGroupByItem] | Unset = UNSET
        if _group_by is not UNSET:
            group_by = []
            for group_by_item_data in _group_by:
                group_by_item = QueryRequestGroupByItem(group_by_item_data)



                group_by.append(group_by_item)


        limit = d.pop("limit", UNSET)

        series = d.pop("series", UNSET)

        _to = d.pop("to", UNSET)
        to: datetime.datetime | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = datetime.datetime.fromisoformat(_to)




        query_request = cls(
            dataset=dataset,
            measure=measure,
            bucket=bucket,
            filters=filters,
            from_=from_,
            group_by=group_by,
            limit=limit,
            series=series,
            to=to,
        )


        query_request.additional_properties = d
        return query_request

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
