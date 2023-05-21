"""
Note1: fastapiのRequestValidationError（status_code=422）をハンドリングしたいなら、ここでハンドリングする。
```
from fastapi.exceptions import RequestValidationError

def handle_request_validation_exception(request: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(...)

def add_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(RequestValidationError, handle_request_validation_exception)
```

Note2: 存在しなpathにアクセスした場合のレスポンスを変えたい場合は、例外ではなく404を指定してハンドリングすると変更可能。
参考：https://fastapi.tiangolo.com/tutorial/handling-errors/#override-the-httpexception-error-handler
```
def add_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(404, handle_not_found_path)
```
"""
from typing import Any

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.api.utils.exception.error_message import HttpErrorMessage
from src.api.utils.exception.exception import HttpException
from src.api.utils.exception.schema import ErrorCodeMsg, ErrorResponse


def handle_invalid_request(request: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=ErrorResponse(
            detail=[
                ErrorCodeMsg(
                    code=HttpErrorMessage.E_H_INVALID_REQUEST.name, msg=HttpErrorMessage.E_H_INVALID_REQUEST.value
                )
            ]
        ).dict(),
    )


def handle_custom_exception(request: Request, exc: HttpException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(detail=[ErrorCodeMsg(**e) for e in exc.dict_errors]).dict(),
    )


def add_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(HttpException, handle_custom_exception)
    app.add_exception_handler(RequestValidationError, handle_invalid_request)

    @app.exception_handler(404)
    def custom_404_handler(_: Any, __: Any) -> JSONResponse:
        return JSONResponse(
            status_code=404,
            content=ErrorResponse(
                detail=[
                    ErrorCodeMsg(
                        code=HttpErrorMessage.E_H_NOT_FOUND_PATH.name, msg=HttpErrorMessage.E_H_NOT_FOUND_PATH.value
                    )
                ]
            ).dict(),
        )
