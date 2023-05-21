from sqlalchemy import text

from src.rdb.interface.query import MethodReturnListType, MethodReturnType
from src.settings import TABLE_NAME_USER, Engine
from src.utils.exception.error_info import ErrorInfo
from src.utils.exception.error_message import ErrorMessage
from src.utils.exception.exception import NotFoundError


class UserQuery:
    TABLE_NAME = TABLE_NAME_USER
    # TODO: Dict[str, Any]を返してるけど、ここは何かしらのクラスを定義して返したい。
    # TODO: どのクエリも返す形は同じなので、共通化できるかも。リストの辞書か単体の辞書かを返すだけ。

    @classmethod
    def all(cls) -> MethodReturnListType:
        """指定メンバーが持つ全単語成績を取得する"""
        with Engine.connect() as conn:
            resultproxy = conn.execute(text("SELECT * FROM user"))
            users = [rowproxy._asdict() for rowproxy in resultproxy]
            return users

    @classmethod
    def one_by_name(cls, name: str) -> MethodReturnType:
        """指定メンバーが持つ全単語成績を取得する"""
        with Engine.connect() as conn:
            resultproxy = conn.execute(
                text("SELECT * FROM {} WHERE name = :name".format(TABLE_NAME_USER)), {"name": name}
            )
            users = [rowproxy._asdict() for rowproxy in resultproxy]
            if len(users) == 0:
                raise NotFoundError([ErrorInfo(ErrorMessage.E_NOT_FOUND_USER)])
            return users[0]
