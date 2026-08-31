from domain.exeptions.base import AppError
from domain.types import CategoryErrorsType


class ValidationError(AppError):
    def __init__(self, message, details=None):
        super().__init__(
            message, "VALIDATION_ERROR", CategoryErrorsType.VALIDATION.value, details
        )
