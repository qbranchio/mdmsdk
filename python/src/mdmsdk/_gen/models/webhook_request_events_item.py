from enum import StrEnum

class WebhookRequestEventsItem(StrEnum):
    COMMAND_COMPLETED = "command.completed"
    DEVICE_ENROLLED = "device.enrolled"
    DEVICE_OS_BEHIND = "device.os_behind"
    DEVICE_POLICY_STATUS = "device.policy_status"
    DEVICE_UNENROLLED = "device.unenrolled"
    PUSH_CERTIFICATE_EXPIRING = "push_certificate.expiring"
    TENANT_DELETED = "tenant.deleted"
    TENANT_DELETING = "tenant.deleting"

    def __str__(self) -> str:
        return str(self.value)
