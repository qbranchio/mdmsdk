from enum import StrEnum

class PushCertificateExpiringEventType(StrEnum):
    PUSH_CERTIFICATE_EXPIRING = "push_certificate.expiring"

    def __str__(self) -> str:
        return str(self.value)
