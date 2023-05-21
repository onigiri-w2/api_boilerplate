from functools import wraps
from typing import Callable, Tuple, Type

from src.api.utils.exception.exception import HttpException
from src.utils.exception.exception import RootException


def convert_exception(to_: Type[HttpException], from_: Tuple[Type[RootException], ...]) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        # type: ignore
        async def wrapper(*args, **kwargs) -> Callable:
            try:
                return await func(*args, **kwargs)
            except from_ as e:
                raise to_(e.dict_errors, e)

        return wrapper

    return decorator
