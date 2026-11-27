from enum import StrEnum

class TenantDeletingEventType(StrEnum):
    TENANT_DELETING = "tenant.deleting"

    def __str__(self) -> str:
        return str(self.value)
