"""
これはサンプルです。
"""
from sqlalchemy import Column, Integer, String

from src.model.impl.entity.user.user import User as UserEntity
from src.rdb.interface.orm import OrmBase
from src.settings import TABLE_NAME_USER
from src.utils.exception.error_info import ErrorInfo, ErrorMessage
from src.utils.exception.exception import InvalidFromOrmError


class User(OrmBase[UserEntity]):
    __tablename__ = TABLE_NAME_USER

    id = Column("id", String(16), primary_key=True, index=True)
    name = Column("name", String(100), nullable=False, unique=True)
    age = Column("age", Integer, nullable=False)
    phone_number = Column("phone_number", String(20), nullable=True, unique=True)

    @classmethod
    def new_from_entity(cls, entity: UserEntity) -> "User":
        return cls(
            id=entity.id.id,
            name=entity.name.name,
            age=entity.age.age,
            phone_number=entity.phone_number.phone_number,
        )

    def to_entity(self) -> UserEntity:
        if self.age is None:
            raise InvalidFromOrmError([ErrorInfo(ErrorMessage.E_INVALID_FROM_ORM)])
        return UserEntity.build(str(self.id), str(self.name), int(self.age), str(self.phone_number))

    def update_with_entity(self, entity: UserEntity) -> "User":
        self.name = entity.name.name
        self.age = entity.age.age
        self.phone_number = entity.phone_number.phone_number
        return self
