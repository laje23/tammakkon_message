from domain.exeptions.base import AppError
from domain.types import CategoryErrorsType


class OperationFailedError(AppError):
    def __init__(self, message, details = None):
        super().__init__(
            message,
            "OPERATION_FAILED_ERROR",
            CategoryErrorsType.OPERATION_FAILED.value ,
            details
        )