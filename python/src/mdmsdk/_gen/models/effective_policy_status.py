from enum import StrEnum

class EffectivePolicyStatus(StrEnum):
    APPLIED = "applied"
    FAILED = "failed"
    PENDING = "pending"
    REMOVING = "removing"

    def __str__(self) -> str:
        return str(self.value)
