from pydantic import BaseModel


class UserResponse(BaseModel):
    id: str
    name: str
    age: int
    phone_number: str

    class Config:
        schema_extra = {
            "examples": {
                "base": {
                    "summary": "base pattern",
                    "description": "base pattern",
                    "value": {
                        "id": "0123456789" + "a" * 6,
                        "name": "hoge",
                        "age": 20,
                        "phone_number": "000-0000-0000",
                    },
                },
            }
        }
