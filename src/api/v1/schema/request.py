from pydantic import BaseModel


class RegisterMember(BaseModel):
    name: str


class CreateUserRequest(BaseModel):
    name: str
    age: int
    phone_number: str


class UpdateUserRequest(BaseModel):
    id: str
    name: str | None
    age: int | None
    phone_number: str | None
