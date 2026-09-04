from domain.exeptions.base import AppError
from domain.types import CategoryErrorsType


class baseFailedError(AppError):
    def __init__(self, message, details=None):
        super().__init__(
            message,
            "base_FAILED_ERROR",
            CategoryErrorsType.base_FAILED.value,
            details,
        )
