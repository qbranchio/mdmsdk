from enum import StrEnum

class TenantDeletedEventType(StrEnum):
    TENANT_DELETED = "tenant.deleted"

    def __str__(self) -> str:
        return str(self.value)
