from enum import StrEnum

class CatalogKeyType(StrEnum):
    ANY = "any"
    ARRAY = "array"
    BOOLEAN = "boolean"
    DATA = "data"
    DATE = "date"
    DICTIONARY = "dictionary"
    INTEGER = "integer"
    REAL = "real"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
