from domain.exeptions.base import AppError
from domain.types import CategoryErrorsType


class InvalidStateError(AppError):
    def __init__(self, message, details=None):
        super().__init__(
            message,
            "INVALID_STATE_ERROR",
            CategoryErrorsType.INVALID_STATE,
            details,
        )
