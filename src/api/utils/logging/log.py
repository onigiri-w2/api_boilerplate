from fastapi import Request

from src.api.utils.exception.exception import HttpException


class RequestLog:
    DECODE = "utf-8"

    def __init__(self, request_id: str, request: Request) -> None:
        self._request_id = request_id
        self._request = request

    async def to_json(self) -> dict:
        return {
            "request_id": self._request_id,
            "body": (await self._request.body()).decode(self.DECODE),
            "headers": {k.decode(self.DECODE): v.decode(self.DECODE) for (k, v) in self._request.headers.raw},
            "remote_addr": self._request.client.host if self._request.client else "",
            "path": self._request.url.path,
            "method": self._request.method,
        }


class ErrorLevelLog:
    LEVEL = "error"

    def __init__(self, request_id: str, exception: HttpException) -> None:
        self.request_id = request_id
        self._exception = exception

    def to_json(self) -> dict:
        return {
            "request_id": self.request_id,
            "error": str(self._exception),
            "level": self.LEVEL,
            "original_error": str(self._exception.original_error),
        }


class CriticalLevelLog:
    LEVEL = "critical"

    def __init__(self, request_id: str, exception: Exception, traceback: str) -> None:
        self.request_id = request_id
        self._exception = exception
        self._traceback = traceback

    def to_json(self) -> dict:
        return {
            "request_id": self.request_id,
            "error": str(self._exception),
            "traceback": self._traceback,
            "level": self.LEVEL,
        }
