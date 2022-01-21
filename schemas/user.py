from pydantic import BaseModel

class User(BaseModel):
    age: int
    gender: str

