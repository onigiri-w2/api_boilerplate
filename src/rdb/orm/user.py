"""
これはサンプルです。
"""
from sqlalchemy import Column, Integer, String

from src.model.impl.entity.user.user import User as UserEntity
from src.rdb.interface.orm import OrmBase
from src.settings import TABLE_NAME_USER


class User(OrmBase):
    __tablename__ = TABLE_NAME_USER

    id = Column("id", String(16), primary_key=True, index=True)
    name = Column("name", String(100), nullable=False, unique=True)
    age = Column("age", Integer, nullable=False)
    phone_number = Column("phone_number", String(20), nullable=True, unique=True)

    @classmethod
    def from_entity(cls, entity: UserEntity) -> "User":
        return cls(
            id=entity.id.id,
            name=entity.name.name,
            age=entity.age.age,
            phone_number=entity.phone_number.phone_number,
        )

    def to_entity(self) -> UserEntity:
        return UserEntity.build(str(self.id), str(self.name), int(self.age), str(self.phone_number))
