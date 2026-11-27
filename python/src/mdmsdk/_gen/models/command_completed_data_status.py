from enum import StrEnum

class CommandCompletedDataStatus(StrEnum):
    ACKNOWLEDGED = "acknowledged"
    COMMAND_FORMAT_ERROR = "command_format_error"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
