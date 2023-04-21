from firebase_admin import auth

from src.utils.exception.error_info import ErrorInfo, ErrorMessage
from src.utils.exception.exception import AuthenticationError


def verify_id_token(token: str) -> "DecodedToken":
    """Firebaseのトークンを検証する
    Usage:
        decoded_token = verify_id_token(token)
        decoded_token.uid
    Raises:
        AuthenticationError: auth.verify_id_token()で例外が発生した場合
    """
    try:
        decoded_token = auth.verify_id_token(token)
    except Exception:
        raise AuthenticationError([ErrorInfo(ErrorMessage.E_AUTH_ERROR)])
    return DecodedToken(decoded_token)


class DecodedToken:
    def __init__(self, decoded_token: dict):
        self._decoded_token = decoded_token

    @property
    def uid(self) -> str:
        return self._decoded_token["uid"]

    @property
    def email(self) -> str:
        return self._decoded_token["email"]
