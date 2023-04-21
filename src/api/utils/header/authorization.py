"""
認証系のヘッダーを取得する関数を定義する
Usage:
    # firebaseを使う場合
    from src.external.firebase.auth import verify_id_token
    from src.api.utils.header.authorization import bearer_token

    @app.post("/profile")
    async def quiz(auth_token: str = Depends(bearer_token)):
        decoded_token = verify_id_token(auth_token)
        uid = decoded_token.uid
"""
from fastapi import Header

from src.api.utils.exception.error_message import HttpErrorMessage
from src.api.utils.exception.exception import Http403Exception


def bearer_token(authorization: str = Header(None)) -> str:
    """AuthorizationヘッダーからBearerトークンを取得する

    Args:
        authorization (str, optional): authorizationヘッダーの値。デフォルトはNone。

    Raises:
        Http403Exception: authorizationヘッダーがNoneの場合
        Http403Exception: authorizationヘッダーがBearerトークンでない場合

    Returns:
        str: Bearerトークン
    """
    exception = Http403Exception(
        [{"code": HttpErrorMessage.E_H_AUTH_INVALID.name, "msg": HttpErrorMessage.E_H_AUTH_INVALID.value}]
    )
    if authorization is None:
        raise exception
    if not authorization.startswith("Bearer "):
        raise exception
    return authorization[7:]
