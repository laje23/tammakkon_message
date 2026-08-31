from domain.exeptions.base import AppError
from domain.types import CategoryErrorsType


class ConflictError(AppError):
    def __init__(self, message, details = None):
        super().__init__(
            message,
            "CONFLICT_ERROR",
            CategoryErrorsType.CONFLICT.value ,
            details
        )