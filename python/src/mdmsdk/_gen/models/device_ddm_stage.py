from enum import StrEnum

class DeviceDDMStage(StrEnum):
    ENABLED = "enabled"
    ENABLING = "enabling"
    NONE = "none"
    TAKING_OVER = "taking_over"

    def __str__(self) -> str:
        return str(self.value)
