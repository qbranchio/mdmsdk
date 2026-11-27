from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.command_status import CommandStatus
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.command_error_type_0_item import CommandErrorType0Item
  from ..models.command_result_type_1 import CommandResultType1





T = TypeVar("T", bound="Command")



@_attrs_define
class Command:
    """ 
        Attributes:
            command_uuid (UUID):
            created_at (datetime.datetime):
            error (list[CommandErrorType0Item] | None): The device's ErrorChain.
            request_type (str):
            result (CommandResultType1 | None): The device's report without UDID, Status, CommandUUID, and ErrorChain. For
                DeviceInformation it carries QueryResponses, for DeviceLock MessageResult when present.
            status (CommandStatus): A command starts in the first status listed and stays there until it is handed to the
                MDM server. cancelled: it was dropped without being sent, because its enrollment ended or a newer decision
                replaced it. It never reached the device.
            updated_at (datetime.datetime):
     """

    command_uuid: UUID
    created_at: datetime.datetime
    error: list[CommandErrorType0Item] | None
    request_type: str
    result: CommandResultType1 | None
    status: CommandStatus
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.command_error_type_0_item import CommandErrorType0Item # noqa: PLC0415
        from ..models.command_result_type_1 import CommandResultType1 # noqa: PLC0415
        command_uuid = str(self.command_uuid)

        created_at = self.created_at.isoformat()

        error: list[dict[str, Any]] | None
        if isinstance(self.error, list):
            error = []
            for error_type_0_item_data in self.error:
                error_type_0_item = error_type_0_item_data.to_dict()
                error.append(error_type_0_item)


        else:
            error = self.error

        request_type = self.request_type

        result: dict[str, Any] | None
        if isinstance(self.result, CommandResultType1):
            result = self.result.to_dict()
        else:
            result = self.result

        status = self.status.value

        updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "command_uuid": command_uuid,
            "created_at": created_at,
            "error": error,
            "request_type": request_type,
            "result": result,
            "status": status,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.command_error_type_0_item import CommandErrorType0Item # noqa: PLC0415
        from ..models.command_result_type_1 import CommandResultType1 # noqa: PLC0415
        d = dict(src_dict)
        command_uuid = UUID(d.pop("command_uuid"))




        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        def _parse_error(data: object) -> list[CommandErrorType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                error_type_0 = []
                _error_type_0 = data
                for error_type_0_item_data in (_error_type_0):
                    error_type_0_item = CommandErrorType0Item.from_dict(error_type_0_item_data)



                    error_type_0.append(error_type_0_item)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CommandErrorType0Item] | None, data)

        error = _parse_error(d.pop("error"))


        request_type = d.pop("request_type")

        def _parse_result(data: object) -> CommandResultType1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_1 = CommandResultType1.from_dict(data)



                return result_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CommandResultType1 | None, data)

        result = _parse_result(d.pop("result"))


        status = CommandStatus(d.pop("status"))




        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        command = cls(
            command_uuid=command_uuid,
            created_at=created_at,
            error=error,
            request_type=request_type,
            result=result,
            status=status,
            updated_at=updated_at,
        )


        command.additional_properties = d
        return command

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
