from fastapi import FastAPI
import uvicorn
from spots_db import get_spots, add_spots
from users_db import get_user, add_user
from spot import Spot
from user import User

app=FastAPI()

@app.get("/spots")
def get_Spots(lat: float, lng: float, genre: str = None, skima_time: int = 999):
    return get_spots(lat, lng, genre, skima_time)

@app.post("/spots")
def add_Spots(spot: Spot):
    return add_spots(spot)

@app.get("/users")
def get_User():
    return get_user()

@app.post("/users")
def add_User(user: User):
    return add_user(user)

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port = 80)
