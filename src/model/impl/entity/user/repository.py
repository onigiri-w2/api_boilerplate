"""
このファイルは、Repositoryのサンプルです。
"""
from src.model.impl.entity.user.user import User
from src.model.impl.repository.mysql_repository import MySQLRepository
from src.rdb.orm.user import User as UserORM
from src.utils.exception.error_info import ErrorInfo, ErrorMessage
from src.utils.exception.exception import NotFoundError


class UserMySQLRepository(MySQLRepository):
    def save(self, entity: User) -> User:
        user_orm: UserORM = UserORM.from_entity(entity)
        self._session.add(user_orm)
        if self._autocommit:
            self._session.commit()
        return entity

    def find(self, id: str) -> User:
        user_orm: UserORM | None = self._session.query(UserORM).filter(UserORM.id == id).first()
        if user_orm is None:
            raise NotFoundError([ErrorInfo(ErrorMessage.E_NOT_FOUND_USER)])
        return user_orm.to_entity()
