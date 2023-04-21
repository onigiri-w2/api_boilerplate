import logging
import secrets
import traceback
from typing import Callable

from fastapi import Request, Response
from fastapi.routing import APIRoute

from src.api.context import request_id_context
from src.api.utils.logging.log import CriticalLevelLog, ErrorLevelLog, RequestLog
from src.utils.exception.exception import RootException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LoggingRoute(APIRoute):
    """エラー発生時にログを出力するためのカスタムRouteクラス

    Note:
        RootExceptionの場合でもcriticalレベルでログを出力することあるかもなぁ。
        その時は、RootExceptionを継承したクラスを作って、そこでログレベルを変えるようにするか？
    """

    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            # リクエストIDを作成
            request_id_context.set(secrets.token_hex(16))

            try:
                response = await original_route_handler(request)
                return response
            except Exception as e:
                # ログ量が増えないように、エラー時だけリクエストパラメータを記録しておく。
                logger.info(await RequestLog(request_id_context.get(), request).to_json())
                if isinstance(e, RootException):
                    logger.error(ErrorLevelLog(request_id_context.get(), e).to_json())
                else:
                    logger.critical(CriticalLevelLog(request_id_context.get(), e, traceback.format_exc()).to_json())
                raise e

        return custom_route_handler
