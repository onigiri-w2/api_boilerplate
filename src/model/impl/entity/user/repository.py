"""
このファイルは、Repositoryのサンプルです。
"""
from sqlalchemy.exc import IntegrityError

from src.model.impl.entity.user.user import User
from src.model.impl.repository.mysql_repository import MySQLRepository
from src.model.impl.valueobject.id.char_16_id import Char16Id
from src.rdb.orm.user import User as UserORM
from src.utils.exception.error_info import ErrorInfo, ErrorMessage
from src.utils.exception.exception import NotFoundError


class UserMySQLRepository(MySQLRepository[User, Char16Id]):
    # TODO: エラー処理周りのコードを綺麗にしたい。
    def create(self, entity: User) -> User:
        try:
            orm = UserORM.new_from_entity(entity)
            self._session.add(orm)
            if self._autocommit:
                self._session.commit()
        except IntegrityError as e:
            # TODO: カスタムエラーに変換する
            self._session.rollback()
            raise e
        except Exception as e:
            self._session.rollback()
            raise e
        return entity

    def update(self, entity: User) -> User:
        try:
            # 対象のMemberが存在するか確認する
            orm = self._find_orm(entity.id.id)
            orm.update_with_entity(entity)
            if self._autocommit:
                self._session.commit()
        except IntegrityError as e:
            # TODO: カスタムエラーに変換する
            self._session.rollback()
            raise e
        except Exception as e:
            self._session.rollback()
            raise e
        return entity

    def find(self, id: Char16Id) -> User:
        orm = self._find_orm(id.id)
        return orm.to_entity()

    def _find_orm(self, id: str) -> UserORM:
        member_orm: UserORM | None = self._session.query(UserORM).filter(UserORM.id == id).first()
        if member_orm is None:
            raise NotFoundError([ErrorInfo(ErrorMessage.E_NOT_FOUND_USER)])
        return member_orm
