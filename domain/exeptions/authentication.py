from domain.exeptions.base import AppError
from domain.types import CategoryErrorsType


class AuthenticationError(AppError):
    def __init__(self, message, details=None):
        super().__init__(
            message,
            "AUTHENTICATION_ERROR",
            CategoryErrorsType.AUTHENTICATION,
            details,
        )
