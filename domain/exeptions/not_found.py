from domain.exeptions.base import AppError
from domain.types import CategoryErrorsType


class NotFoundError(AppError):
    def __init__(self, message, details=None):
        super().__init__(
            message, "NOT_FOUND_ERROR", CategoryErrorsType.NOT_FOUND.value, details
        )
