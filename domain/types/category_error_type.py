from enum import Enum


class CategoryErrorsType(Enum):
    CONNECTION_FAILED = "connection_failed"
    OPERATION_FAILED = "operation_failde"
    EXTERNAL_SERVICE = "external_service"
    AUTHORIZATION_ERROR = "authorization"
    AUTHENTICATION = "authentication"
    INVALID_STATE = "invalid_state"
    VALIDATION = "validation"
    RATE_LIMIT = "rate_limit"
    NOT_FOUND = "not_found"
    CONFLICT = "conflict"
    SEND = "send"