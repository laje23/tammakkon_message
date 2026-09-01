from domain.exeptions.base import AppError
from domain.types import CategoryErrorsType


class SendError(AppError):
    def __init__(self, message, details=None):
        super().__init__(message, "SEND_ERROR", CategoryErrorsType.SEND, details)
