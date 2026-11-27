from enum import StrEnum

class QueryRequestBucket(StrEnum):
    DAY = "day"
    HOUR = "hour"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
