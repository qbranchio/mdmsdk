from enum import StrEnum

class QueryRequestDataset(StrEnum):
    ACTIVITY = "activity"
    DEVICES = "devices"

    def __str__(self) -> str:
        return str(self.value)
