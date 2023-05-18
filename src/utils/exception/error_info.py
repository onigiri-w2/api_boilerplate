from typing import Any, Dict

from src.utils.exception.error_message import ErrorMessage


class ErrorInfo:
    def __init__(self, error_message: ErrorMessage, msg_kwargs: Dict[str, Any] = {}) -> None:
        self._error_message = error_message
        self._kwargs = msg_kwargs

    def __str__(self) -> str:
        return f"{self.code}:{self.msg}"

    @property
    def code(self) -> str:
        return self._error_message.name

    @property
    def msg(self) -> str:
        return self._error_message.value.format(**self._kwargs)

    def to_dict(self) -> dict[str, str]:
        return {"code": self.code, "msg": self.msg}
