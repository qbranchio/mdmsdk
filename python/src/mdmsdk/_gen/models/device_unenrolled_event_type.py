from enum import StrEnum

class DeviceUnenrolledEventType(StrEnum):
    DEVICE_UNENROLLED = "device.unenrolled"

    def __str__(self) -> str:
        return str(self.value)
