from typing import List

from pydantic import BaseModel


class ErrorCodeMsg(BaseModel):
    code: str
    msg: str


class ErrorResponse(BaseModel):
    detail: List[ErrorCodeMsg]

    # TODO: 必要であれば、例外サンプルを変更、追加する
    class Config:
        schema_extra = {
            "examples": {
                "400": {
                    "summary": "400 error",
                    "description": "this is 400 error sample",
                    "value": {"detail": [{"code": "E_INVALID_NAME_LENGH", "msg": "ユーザーの名前が不正です"}]},
                },
                "500": {
                    "summary": "500 error",
                    "description": "this is 500 error sample",
                    "value": {"detail": [{"code": "E_INTERNAL_ERROR", "msg": "内部エラーが発生しました"}]},
                },
            }
        }
