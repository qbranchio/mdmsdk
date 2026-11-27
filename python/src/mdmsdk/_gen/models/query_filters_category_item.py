from enum import StrEnum

class QueryFiltersCategoryItem(StrEnum):
    COMMANDS = "commands"
    DEVICES = "devices"
    OTHER = "other"
    SETTINGS = "settings"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
