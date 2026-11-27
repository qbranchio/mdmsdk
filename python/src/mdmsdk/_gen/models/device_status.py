from enum import StrEnum

class DeviceStatus(StrEnum):
    ENROLLED = "enrolled"
    ENROLLING = "enrolling"
    PENDING = "pending"
    UNENROLLED = "unenrolled"

    def __str__(self) -> str:
        return str(self.value)
