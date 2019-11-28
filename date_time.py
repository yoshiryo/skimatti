from pydantic import BaseModel

class Date_time(BaseModel):
    year: int
    month: int
    date: int
    hour: int
    minute: int
