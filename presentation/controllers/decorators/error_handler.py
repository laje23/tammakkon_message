from functools import wraps
from infrastructure.dependency_Injection import container


def log(message, src):
    with container.unit_of_work:
        container.logger.log(
            message, container.logger.category.SYSTEM, container.logger.level.ERROR, src
        )


def safe_method(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except Exception as e:
            log(str(e), func.__class__.__name__)
            return {
                "success": False,
                "message": str(e),
                "error": {"type": type(e).__name__},
            }

    return wrapper


def safe_class(cls):

    for name, method in cls.__dict__.items():

        if callable(method):
            setattr(cls, name, safe_method(method))

    return cls
