from dataclasses import dataclass
from enum import Enum

import pytest

from src.model.interface.valueobject import ValueObject
from src.utils.exception.error_info import ErrorInfo
from src.utils.exception.exception import ValidationError
from src.utils.validation.evaluator import Evaluator


class ErrorMessageTest(Enum):
    E_TEST_ERROR = "test error"
    E_TEST_ERROR2 = "test_erro2"


ERROR_INFO = ErrorInfo(ErrorMessageTest.E_TEST_ERROR)
ERROR_INFO2 = ErrorInfo(ErrorMessageTest.E_TEST_ERROR2)


@dataclass(frozen=True)
class Hoge(ValueObject):
    hoge: int

    @classmethod
    def new(cls, hoge: int) -> "Hoge":
        return cls(hoge=hoge)


@dataclass(frozen=True)
class ValueObjectTest(ValueObject):
    test: str
    hoge: Hoge

    __class_vars__ = {"MAX_LENGTH": 10, "MAX_HOGE": 10}
    VALID_SCHEMA = [
        (Evaluator(lambda test: 0 < len(test) <= ValueObjectTest.__class_vars__["MAX_LENGTH"]), ERROR_INFO),
        (Evaluator(lambda hoge: hoge.hoge <= ValueObjectTest.__class_vars__["MAX_HOGE"]), ERROR_INFO2),
    ]

    @classmethod
    def new(cls, test: str, hoge: int) -> "ValueObjectTest":
        return cls(test=test, hoge=Hoge.new(hoge))


def describe_ValueObject():
    def describe_new():
        def test_正常に初期化できることを確認():
            sut = ValueObjectTest.new("test", 1)
            assert sut.test == "test"
            assert sut.hoge.hoge == 1

        def test_事前条件を満たさない値が入力された場合はValidationErrorr発生():
            with pytest.raises(ValidationError):
                ValueObjectTest.new("", 1)

        def test_事前条件を満たさない値が入力された場合はValidationErrorr発生_hoge_11():
            with pytest.raises(ValidationError):
                ValueObjectTest.new("", 11)

    def describe_asdict():
        def test_testとhogeの値がdictで出力される():
            sut = ValueObjectTest.new("test", 1)
            assert sut.asdict() == {"test": "test", "hoge": {"hoge": 1}}
