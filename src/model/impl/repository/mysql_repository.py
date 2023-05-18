from src.model.interface.repository import Repository, TEntity
from src.settings import Session


class MySQLRepository(Repository[TEntity]):
    def __init__(self, autocommit: bool = False):
        self._autocommit = autocommit
        self._session = Session()

    def commit(self) -> None:
        self._session.commit()

    def rollback(self) -> None:
        self._session.rollback()
