from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from src.model.interface.entity import Entity

T = TypeVar("T", bound="Entity")


class Repository(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def save(self, entity: T) -> T:
        pass

    @abstractmethod
    def find(self, id: str) -> T:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass
