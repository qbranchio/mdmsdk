from enum import StrEnum

class DevicePolicyStatusEventType(StrEnum):
    DEVICE_POLICY_STATUS = "device.policy_status"

    def __str__(self) -> str:
        return str(self.value)
