from enum import StrEnum

class DevicePolicyInstallLevelType2Type1(StrEnum):
    SUPERVISED = "supervised"
    UNSUPERVISED = "unsupervised"

    def __str__(self) -> str:
        return str(self.value)
