"""
注意：このファイルは、ValueObjectのサンプルです。
"""
from dataclasses import dataclass

from src.model.interface.valueobject import ValueObject
from src.utils.exception.error_info import ErrorInfo, ErrorMessage
from src.utils.validation.evaluator import Evaluator


@dataclass(frozen=True)
class Age(ValueObject):
    age: int
    __class_vars__ = {
        "MAX": 100,
    }
    VALID_SCHEMA = [
        (
            Evaluator(lambda age: 0 < age <= Age.__class_vars__["MAX"]),
            ErrorInfo(ErrorMessage.E_INVALID_AGE),
        )
    ]

    @classmethod
    def new(cls, age: int) -> "Age":
        return cls(age=age)
