from pydantic import BaseModel

class Spot(BaseModel):
    name: str
    lat: float
    lng: float
    genre: str

