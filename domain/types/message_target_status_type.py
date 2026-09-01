from enum import Enum

class MessageTargetStatusType(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SENT = "sent"
    FAILED = "failed"
    CANCELED = "canceled"