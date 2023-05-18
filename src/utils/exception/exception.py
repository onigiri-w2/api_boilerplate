from abc import ABCMeta
from typing import List

from src.utils.exception.error_info import ErrorInfo


class RootException(Exception, metaclass=ABCMeta):
    """全ての例外の基底クラス"""

    def __init__(self, error_info_list: List[ErrorInfo]) -> None:
        self.error_info_list = error_info_list

    def __str__(self) -> str:
        return "[{}]".format(", ".join([str(e) for e in self.error_info_list]))

    @property
    def errors(self) -> list[ErrorInfo]:
        return self.error_info_list

    @property
    def dict_errors(self) -> list[dict[str, str]]:
        return [e.to_dict() for e in self.error_info_list]


class ValidationError(RootException):
    """バリデーションエラー"""


class NotFoundError(RootException):
    """データが見つからないエラー"""


class AuthenticationError(RootException):
    """認証エラー"""


class InvalidFromOrmError(RootException):
    """ORMからEntityへの変換エラー"""
