from enum import StrEnum

class AssignmentRequestTarget(StrEnum):
    DEVICE = "device"
    GROUP = "group"
    MEMBER = "member"
    TENANT = "tenant"

    def __str__(self) -> str:
        return str(self.value)
