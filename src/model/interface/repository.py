from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from src.model.interface.entity import Entity, TId

TEntity = TypeVar("TEntity", bound="Entity")


class Repository(Generic[TEntity, TId], metaclass=ABCMeta):
    @abstractmethod
    def create(self, entity: TEntity) -> TEntity:
        pass

    @abstractmethod
    def update(self, entity: TEntity) -> TEntity:
        pass

    @abstractmethod
    def find(self, id: TId) -> TEntity:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass
