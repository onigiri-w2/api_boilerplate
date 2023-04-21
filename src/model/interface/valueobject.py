from abc import ABCMeta, abstractmethod
from dataclasses import asdict, dataclass
from typing import ClassVar, List, Tuple

from src.utils.exception.error_info import ErrorInfo
from src.utils.exception.exception import ValidationError
from src.utils.validation.validator import Evaluator, Validator


@dataclass(frozen=True)
class ValueObject(metaclass=ABCMeta):
    __class_vars__: ClassVar[dict] = {}
    VALID_SCHEMA: ClassVar[List[Tuple[Evaluator, ErrorInfo]]] = []

    @classmethod
    @abstractmethod
    # type: ignore
    def new(cls, *args, **kwargs) -> "ValueObject":
        raise NotImplementedError

    def asdict(self) -> dict:
        return asdict(self)

    def __post_init__(self) -> None:
        validator = Validator(self.VALID_SCHEMA)
        keys = asdict(self).keys()
        validator.validate({k: self.__dict__[k] for k in keys})
        if validator.errors:
            raise ValidationError(validator.errors)
