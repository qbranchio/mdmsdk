from enum import StrEnum

class CatalogKeyFormat(StrEnum):
    HOSTNAME = "hostname"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
