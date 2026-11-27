from enum import StrEnum

class CatalogEntryKind(StrEnum):
    DECLARATION = "declaration"
    PROFILE = "profile"
    RESTRICTION = "restriction"

    def __str__(self) -> str:
        return str(self.value)
