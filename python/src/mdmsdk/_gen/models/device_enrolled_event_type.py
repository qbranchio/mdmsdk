from enum import StrEnum

class DeviceEnrolledEventType(StrEnum):
    DEVICE_ENROLLED = "device.enrolled"

    def __str__(self) -> str:
        return str(self.value)
