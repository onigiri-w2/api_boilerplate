from fastapi import status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.api.utils.exception.error_message import HttpErrorMessage
from src.api.utils.exception.schema import ErrorCodeMsg, ErrorResponse


class CustomServerErrorHandler(BaseHTTPMiddleware):
    """`Exception`をキャッチして、固定のレスポンスを返すためのミドルウェア

    通常、例外はapp.exception_handlerでハンドリングする。
    ただ、それらは開発者が意図的にraiseした例外に対してのみのハンドリング。
    それ以外の例外（開発者が意図していなかったもの）は、ここでハンドリングする。

    なお、本来であればデフォルトで存在するStartletの`ServerErrorsMiddleware`に処理を任せるべき。
    ただ、スタックトレースが自動で出力されるのが嫌なので、ここでハンドリングすることにした。
    # noqa
    - 参考：https://scrapbox.io/onigiri-it-tips/FastAPI_Exception%E3%82%AF%E3%83%A9%E3%82%B9%E3%81%AE%E4%BE%8B%E5%A4%96%E3%83%8F%E3%83%B3%E3%83%89%E3%83%AA%E3%83%B3%E3%82%B0%E3%82%92%E3%81%99%E3%82%8B%E9%9A%9B%E3%81%AE%E6%8C%99%E5%8B%95

    Note:
        Startletの`ServerErrorsMiddleware`により似せたい場合は、`startlet.middleware.errors.ServerErrorsMiddleware`を継承して__call__をオーバーライドするといい。
    """

    async def dispatch(self, request, call_next):  # type: ignore
        try:
            response = await call_next(request)
            return response
        except Exception:
            res = ErrorResponse(
                detail=[
                    ErrorCodeMsg(
                        code=HttpErrorMessage.E_H_SERVER_INTERNAL_ERROR.name,
                        msg=HttpErrorMessage.E_H_SERVER_INTERNAL_ERROR.value,
                    )
                ]
            )
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=res.dict(),
            )
