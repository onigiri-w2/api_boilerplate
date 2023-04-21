import secrets
from abc import ABCMeta, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any

from src.model.interface.valueobject import ValueObject
from src.utils.validation.evaluator import Evaluator


@dataclass
class Entity(metaclass=ABCMeta):
    id: "Id"

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

    @classmethod
    def _generate_id(cls) -> "Id":
        return Id.new(secrets.token_hex(8))

    @classmethod
    def _build_id(cls, id: str) -> "Id":
        return Id.new(id)

    def asdict(self) -> dict:
        return asdict(self)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(f"{self.__class__.__name__}:{self.id}")


@dataclass(frozen=True)
class Id(ValueObject):
    id: str
    __class_vars__ = {
        "LENGTH": 16,
    }
    VALID_SCHEMA = [
        (Evaluator(lambda id: len(id) == Id.__class_vars__["LENGTH"]), "IDの長さが不正です。"),
    ]

    @classmethod
    def new(cls, id: str) -> "Id":
        return cls(id=id)
