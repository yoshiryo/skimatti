from pydantic import BaseModel

class Spot(BaseModel):
    name: str
    latitude: float
    longitude: float
    genre: str
    stay_time: int
    comment: str
    plan: str


