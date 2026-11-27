from enum import StrEnum

class DevicePolicyStatusDataStatus(StrEnum):
    APPLIED = "applied"
    FAILED = "failed"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)
