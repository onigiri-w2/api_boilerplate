from abc import ABC, ABCMeta, abstractmethod
from typing import Generic, TypeVar

# from src.config import Base
from sqlalchemy.ext.declarative import DeclarativeMeta

from src.model.interface.entity import Entity
from src.settings import Base

TEntity = TypeVar("TEntity", bound=Entity)


class DeclarativeABCMeta(ABCMeta, DeclarativeMeta):
    pass


# type: ignore
class OrmBase(Generic[TEntity], ABC, Base, metaclass=DeclarativeABCMeta):
    __abstract__ = True

    @classmethod
    @abstractmethod
    def from_entity(cls, entity: TEntity) -> "OrmBase[TEntity]":
        pass

    @abstractmethod
    def to_entity(self) -> TEntity:
        pass
