from domain.exeptions.base import AppError
from domain.types import CategoryErrorsType


class AuthorizationError(AppError):
    def __init__(self, message, details=None):
        super().__init__(
            message,
            "AUTHORIZATION_ERROR",
            CategoryErrorsType.AUTHORIZATION_ERROR,
            details,
        )
