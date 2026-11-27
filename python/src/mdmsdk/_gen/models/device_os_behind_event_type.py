from enum import StrEnum

class DeviceOSBehindEventType(StrEnum):
    DEVICE_OS_BEHIND = "device.os_behind"

    def __str__(self) -> str:
        return str(self.value)
