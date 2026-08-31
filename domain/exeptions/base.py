class AppError(Exception):

    def __init__(
        self,
        message: str,
        code: str,
        category: str,
        details: dict | None = None,
    ):
        super().__init__(message)

        self.message = message
        self.code = code
        self.category = category
        self.details = details or {}
