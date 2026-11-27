from enum import StrEnum

class MeRole(StrEnum):
    ADMIN = "admin"
    OWNER = "owner"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
