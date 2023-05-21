"""
API関連のエラーメッセージを定義する
ビジネスロジック内部に関するエラーメッセージは、ビジネスロジック内部(src/utils/exception/error_message.py)に定義する
"""
from enum import Enum


class HttpErrorMessage(Enum):
    E_H_AUTH_INVALID = "認証系のエラーです"
    E_H_INVALID_REQUEST = "リクエストの形式が不正です"
    E_H_SERVER_INTERNAL_ERROR = "サーバー内部でエラーが発生しました"
    E_H_NOT_FOUND_PATH = "存在しないパスにアクセスしました"
