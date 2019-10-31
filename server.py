from fastapi import FastAPI
import uvicorn

from spots_db import get_spots, add_spots, get_visited_spots, add_visited_spots
from users_db import get_user, add_user
from spot import Spot
from user import User


app=FastAPI()

@app.get("/spots")
def get_Spots(lat: float = None, lng: float = None, genre: str = None, skima_time: int = 999, user_id: int = None ,spots_amount: int = None ):
    return get_spots(lat, lng, genre, skima_time, user_id, spots_amount)

@app.post("/spots")
def add_Spots(spot: Spot):
    return add_spots(spot)

@app.get("/users")
def get_User():
    return get_user()

@app.post("/users")
def add_User(user: User):
    return add_user(user)

@app.get("/visited_spots")
def get_visited_Spots():
    return get_visited_spots()

@app.post("/visited_spots")
def add_visited_Spots(user_id: int, spot_id: int):
    return add_visited_spots(user_id, spot_id)


if __name__ == "__main__":
   uvicorn.run(app, host = "0.0.0.0", port = 80)
