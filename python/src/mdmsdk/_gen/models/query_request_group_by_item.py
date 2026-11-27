from enum import StrEnum

class QueryRequestGroupByItem(StrEnum):
    ACTOR = "actor"
    CATEGORY = "category"
    MODEL = "model"
    OS_BEHIND = "os_behind"
    OS_VERSION = "os_version"
    STATE = "state"
    SUPERVISED = "supervised"
    TENANT = "tenant"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
