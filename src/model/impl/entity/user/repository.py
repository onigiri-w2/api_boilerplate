"""
このファイルは、Repositoryのサンプルです。
"""
from src.model.impl.entity.user.user import User
from src.model.impl.repository.mysql_repository import MySQLRepository
from src.model.impl.valueobject.id.char_16_id import Char16Id
from src.rdb.orm.user import User as UserORM
from src.utils.exception.error_info import ErrorInfo, ErrorMessage
from src.utils.exception.exception import NotFoundError


class UserMySQLRepository(MySQLRepository[User, Char16Id]):
    def create(self, entity: User) -> User:
        orm = UserORM.from_entity(entity)
        self._save(orm)
        return entity

    def update(self, entity: User) -> User:
        # 対象のMemberが存在するか確認する
        self._find_orm(entity.id.id)
        orm = UserORM.from_entity(entity)
        self._save(orm)
        return entity

    def find(self, id: Char16Id) -> User:
        orm = self._find_orm(id.id)
        return orm.to_entity()

    def _find_orm(self, id: str) -> UserORM:
        member_orm: UserORM | None = self._session.query(UserORM).filter(UserORM.id == id).first()
        if member_orm is None:
            raise NotFoundError([ErrorInfo(ErrorMessage.E_NOT_FOUND_USER)])
        return member_orm
