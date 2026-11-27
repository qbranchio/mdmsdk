from enum import StrEnum

class CatalogKeyLevelsItem(StrEnum):
    SUPERVISED = "supervised"
    UNSUPERVISED = "unsupervised"

    def __str__(self) -> str:
        return str(self.value)
