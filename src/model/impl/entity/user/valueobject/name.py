"""
注意：このファイルは、ValueObjectのサンプルです。
"""
from dataclasses import dataclass

from src.model.interface.valueobject import ValueObject
from src.utils.exception.error_info import ErrorInfo, ErrorMessage
from src.utils.validation.evaluator import Evaluator


@dataclass(frozen=True)
class Name(ValueObject):
    name: str
    __class_vars__ = {
        "MAX_LENGTH": 10,
    }
    VALID_SCHEMA = [
        (
            Evaluator(lambda name: 0 < len(name) <= Name.__class_vars__["MAX_LENGTH"]),
            ErrorInfo(ErrorMessage.E_INVALID_NAME_LENGH),
        )
    ]

    @classmethod
    def new(cls, name: str) -> "Name":
        return cls(name=name)
