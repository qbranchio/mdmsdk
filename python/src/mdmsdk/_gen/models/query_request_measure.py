from enum import StrEnum

class QueryRequestMeasure(StrEnum):
    COUNT = "count"

    def __str__(self) -> str:
        return str(self.value)
