"""
API独自のエラークラスを定義する
内部のビジネスロジックで発生したエラーは、ビジネスロジック内部で定義したエラークラスを使用する
内部のエラーは最終的にこのクラスのインスタンスに変換される（converter.pyを参照）
"""
from fastapi import status


class HttpException(Exception):
    status_code: int

    def __init__(self, code_msgs: list[dict[str, str]] = []) -> None:
        self._code_msgs = code_msgs

    @property
    def dict_errors(self) -> list[dict[str, str]]:
        return self._code_msgs


class Http400Exception(HttpException):
    """HTTP 400 Bad Request"""

    status_code = status.HTTP_400_BAD_REQUEST


class Http403Exception(HttpException):
    """HTTP 403 Bad Request"""

    status_code = status.HTTP_403_FORBIDDEN


class Http404Exception(HttpException):
    """HTTP 404 Not Found"""

    status_code = status.HTTP_404_NOT_FOUND
