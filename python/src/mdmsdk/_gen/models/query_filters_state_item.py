from enum import StrEnum

class QueryFiltersStateItem(StrEnum):
    ENROLLED = "enrolled"
    REMOVED = "removed"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
