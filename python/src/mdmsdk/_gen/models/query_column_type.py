from enum import StrEnum

class QueryColumnType(StrEnum):
    NUMBER = "number"
    STRING = "string"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
