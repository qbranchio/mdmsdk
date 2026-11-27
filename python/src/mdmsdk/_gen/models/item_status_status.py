from enum import StrEnum

class ItemStatusStatus(StrEnum):
    APPLIED = "applied"
    FAILED = "failed"
    PENDING = "pending"
    REMOVING = "removing"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
