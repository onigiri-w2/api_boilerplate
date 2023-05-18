"""
このファイルは、Entityのサンプルです。
"""
from dataclasses import dataclass

from src.model.impl.entity.user.valueobject.age import Age
from src.model.impl.entity.user.valueobject.name import Name
from src.model.impl.valueobject.id.char_16_id import Char16Id
from src.model.impl.valueobject.phone_number import PhoneNumber
from src.model.interface.entity import Entity


@dataclass
class User(Entity[Char16Id]):
    name: Name
    age: Age
    phone_number: PhoneNumber

    @classmethod
    def new(cls, name: str, age: int, phone_number: str) -> "User":
        return cls(
            id=Char16Id.random(), name=Name.new(name), age=Age.new(age), phone_number=PhoneNumber.new(phone_number)
        )

    @classmethod
    def build(cls, id: str, name: str, age: int, phone_number: str) -> "User":
        return cls(
            id=Char16Id.new(id), name=Name.new(name), age=Age.new(age), phone_number=PhoneNumber.new(phone_number)
        )

    def updated(self, name: str | None = None, age: int | None = None, phone_number: str | None = None) -> "User":
        if name is None:
            name = self.name.name
        if age is None:
            age = self.age.age
        if phone_number is None:
            phone_number = self.phone_number.phone_number
        return type(self).build(self.id.id, name, age, phone_number)
