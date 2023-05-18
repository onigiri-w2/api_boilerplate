from abc import ABCMeta, abstractmethod
from typing import Any, Generic, TypeVar

from src.model.interface.entity import Entity

TEntity = TypeVar("TEntity", bound="Entity")


class Repository(Generic[TEntity], metaclass=ABCMeta):
    @abstractmethod
    def save(self, entity: TEntity) -> TEntity:
        pass

    @abstractmethod
    def find(self, id: Any) -> TEntity:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass
