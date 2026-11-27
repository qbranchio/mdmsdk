from enum import StrEnum

class TokenRequestPermissionsItem(StrEnum):
    COMMANDSWRITE = "commands:write"
    DEVICESREAD = "devices:read"
    DEVICESWRITE = "devices:write"
    MEMBERSREAD = "members:read"
    PROFILESREAD = "profiles:read"
    PROFILESWRITE = "profiles:write"

    def __str__(self) -> str:
        return str(self.value)
