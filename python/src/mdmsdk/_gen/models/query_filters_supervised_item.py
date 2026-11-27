from enum import StrEnum

class QueryFiltersSupervisedItem(StrEnum):
    NO = "no"
    UNKNOWN = "unknown"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
