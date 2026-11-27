from enum import StrEnum

class SourceLayer(StrEnum):
    DEVICE = "device"
    GROUP = "group"
    MEMBER = "member"
    SETTINGS = "settings"
    TENANT = "tenant"

    def __str__(self) -> str:
        return str(self.value)
