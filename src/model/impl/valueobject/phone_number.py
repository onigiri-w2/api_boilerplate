"""
このファイルは、ValueObjectのサンプルです。
"""
import re
from dataclasses import dataclass

from src.model.interface.valueobject import ValueObject
from src.utils.exception.error_info import ErrorInfo, ErrorMessage
from src.utils.validation.evaluator import Evaluator


@dataclass(frozen=True)
class PhoneNumber(ValueObject):
    phone_number: str

    # REGEXは、ValueObjectの属性から除外したいので、__class_vars__に定義する
    __class_vars__ = {
        "REGEX": re.compile(r"\d{3}-\d{4}-\d{4}"),
    }
    VALID_SCHEMA = [
        (
            Evaluator(lambda phone_number: PhoneNumber.__class_vars__["REGEX"].match(phone_number)),
            ErrorInfo(ErrorMessage.E_INVALID_PHONE_NUMBER),
        )
    ]

    @classmethod
    def new(cls, phone_number: str) -> "PhoneNumber":
        return cls(phone_number=phone_number)
