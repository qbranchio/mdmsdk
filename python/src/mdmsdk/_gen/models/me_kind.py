from enum import StrEnum

class MeKind(StrEnum):
    ACCOUNT_ADMIN = "account_admin"
    ACCOUNT_CLIENT = "account_client"
    DELEGATED = "delegated"
    PLATFORM_ADMIN = "platform_admin"
    TENANT_ADMIN = "tenant_admin"

    def __str__(self) -> str:
        return str(self.value)
