from enum import StrEnum

class CatalogEntryGroup(StrEnum):
    ACCOUNTS = "accounts"
    APPS = "apps"
    CAMERA = "camera"
    CONTENT = "content"
    DEVICE = "device"
    HOME = "home"
    MESSAGES = "messages"
    NETWORK = "network"
    PASSCODE = "passcode"

    def __str__(self) -> str:
        return str(self.value)
