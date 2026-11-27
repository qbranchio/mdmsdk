from enum import StrEnum

class TenantRole(StrEnum):
    ADMIN = "admin"
    OWNER = "owner"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
