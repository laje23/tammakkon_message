from domain.exeptions.base import AppError
from domain.types import CategoryErrorsType


class ConnectionFailedError(AppError):
    def __init__(self, message, details = None):
        super().__init__(
            message,
            "CONNECTION_FAILED_ERROR",
            CategoryErrorsType.CONNECTION_FAILED.value ,
            details
        )