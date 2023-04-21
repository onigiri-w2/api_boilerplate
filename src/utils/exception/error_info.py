from src.utils.exception.error_message import ErrorMessage


class ErrorInfo:
    def __init__(self, error_message: ErrorMessage) -> None:
        self._error_message = error_message

    def __str__(self) -> str:
        return f"{self._error_message.name}:{self._error_message.value}"

    @property
    def code(self) -> str:
        return self._error_message.name

    @property
    def msg(self) -> str:
        return self._error_message.value

    def to_dict(self) -> dict[str, str]:
        return {"code": self.code, "msg": self.msg}
