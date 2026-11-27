from enum import StrEnum

class CommandStatus(StrEnum):
    ACKNOWLEDGED = "acknowledged"
    CANCELLED = "cancelled"
    COMMAND_FORMAT_ERROR = "command_format_error"
    ERROR = "error"
    NOTNOW = "notnow"
    OUTBOX = "outbox"
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
