from enum import StrEnum

class CommandCompletedEventType(StrEnum):
    COMMAND_COMPLETED = "command.completed"

    def __str__(self) -> str:
        return str(self.value)
