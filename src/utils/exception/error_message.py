from enum import Enum


class ErrorMessage(Enum):
    # 以下全て、サンプルメッセージなので、消去してよし。
    E_INVALID_NAME_LENGH = "不正な名前の長さです。"
    E_INVALID_AGE = "不正な年齢です。"
    E_INVALID_PHONE_NUMBER = "不正な電話番号です。"
    E_NOT_FOUND_USER = "ユーザーが見つかりません。"

    E_AUTH_ERROR = "認証エラーです。"
