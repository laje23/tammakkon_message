from domain.exeptions.base import AppError
from domain.types import CategoryErrorsType


class RateLimitError(AppError):
    def __init__(self, message, details=None):
        super().__init__(
            message, "RATE_LIMIT_ERROR", CategoryErrorsType.RATE_LIMIT.value, details
        )
