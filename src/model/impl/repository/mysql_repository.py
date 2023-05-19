from src.model.interface.repository import Repository, TEntity, TId
from src.rdb.interface.orm import OrmBase
from src.settings import Session


class MySQLRepository(Repository[TEntity, TId]):
    def __init__(self, autocommit: bool = False):
        self._autocommit = autocommit
        self._session = Session()

    def _save(self, orm: OrmBase[TEntity]) -> TEntity:
        self._session.add(orm)
        if self._autocommit:
            self._session.commit()
        return orm.to_entity()

    def commit(self) -> None:
        self._session.commit()

    def rollback(self) -> None:
        self._session.rollback()
