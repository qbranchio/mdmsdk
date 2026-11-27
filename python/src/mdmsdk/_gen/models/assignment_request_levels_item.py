from enum import StrEnum

class AssignmentRequestLevelsItem(StrEnum):
    SUPERVISED = "supervised"
    UNSUPERVISED = "unsupervised"

    def __str__(self) -> str:
        return str(self.value)
