from enum import StrEnum

class ItemStatusReasonType3Type1(StrEnum):
    NOT_SUPPORTED_BY_DEVICE = "not_supported_by_device"
    REQUIRES_OS = "requires_os"
    REQUIRES_SUPERVISION = "requires_supervision"

    def __str__(self) -> str:
        return str(self.value)
