from enum import Enum

from src.utils.exception.error_info import ErrorInfo
from src.utils.exception.exception import RootException


class ErrorMessageForTest(Enum):
    """ErrorMessageがEnumであることが前提で使うスタブEnum"""

    E_FOR_TEST = "test error"
    E_FOR_TEST2 = "test error2"


def describe_Exception():
    def describe___init__():
        def test_初期化できる():
            error_info_list = [ErrorInfo(ErrorMessageForTest.E_FOR_TEST)]
            exception = RootException(error_info_list)
            assert exception.error_info_list == error_info_list

    def describe___str__():
        def test_文字列化できる():
            error_info_list = [ErrorInfo(ErrorMessageForTest.E_FOR_TEST)]
            exception = RootException(error_info_list)
            assert str(exception) == "[E_FOR_TEST:test error]"

        def test_複数のエラーを文字列化できる():
            error_info_list = [ErrorInfo(ErrorMessageForTest.E_FOR_TEST), ErrorInfo(ErrorMessageForTest.E_FOR_TEST2)]
            exception = RootException(error_info_list)
            assert str(exception) == "[E_FOR_TEST:test error, E_FOR_TEST2:test error2]"

    def describe_errors():
        def test_エラー情報を取得できる():
            error_info_list = [ErrorInfo(ErrorMessageForTest.E_FOR_TEST), ErrorInfo(ErrorMessageForTest.E_FOR_TEST2)]
            exception = RootException(error_info_list)
            assert exception.errors == error_info_list
