from abc import ABCMeta, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Generic, TypeVar

T = TypeVar("T")


@dataclass
class Entity(Generic[T], metaclass=ABCMeta):
    id: T

    @classmethod
    @abstractmethod
    # type: ignore
    def new(cls, *args, **kwargs) -> "Entity":
        """単語検索された時に初めてインスタンス生成される"""
        pass

    @classmethod
    @abstractmethod
    # type: ignore
    def build(cls, *args, **kwargs) -> "Entity":
        """DBから取得した時にインスタンス生成される"""
        pass

    @abstractmethod
    # type: ignore
    def updated(self, *args, **kwargs) -> "Entity":
        """インスタンスの更新"""
        pass

    def asdict(self) -> dict:
        return asdict(self)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(f"{self.__class__.__name__}:{self.id}")
