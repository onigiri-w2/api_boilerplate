import secrets
from dataclasses import dataclass

from src.model.interface.valueobject import ValueObject
from src.utils.exception.error_info import ErrorInfo, ErrorMessage
from src.utils.validation.evaluator import Evaluator


@dataclass(frozen=True)
class Char16Id(ValueObject):
    """16文字のランダムなID"""

    id: str
    __class_vars__ = {
        "MAX_LENGTH": 16,
    }
    VALID_SCHEMA = [
        (Evaluator(lambda id: len(id) == Char16Id.__class_vars__["MAX_LENGTH"]), ErrorInfo(ErrorMessage.E_AUTH_ERROR)),
    ]

    @classmethod
    def new(cls, id: str) -> "Char16Id":
        return cls(id=id)

    @classmethod
    def random(cls) -> "Char16Id":
        return cls(id=secrets.token_hex(8))
