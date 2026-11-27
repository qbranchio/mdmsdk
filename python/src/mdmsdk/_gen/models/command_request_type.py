from enum import StrEnum

class CommandRequestType(StrEnum):
    DEVICEINFORMATION = "DeviceInformation"
    DEVICELOCK = "DeviceLock"

    def __str__(self) -> str:
        return str(self.value)
