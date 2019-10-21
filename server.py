from fastapi import FastAPI
import uvicorn
from spots_db import get_spots, add_spots
from users_db import get_user, add_user
from spot import Spot

app=FastAPI()

@app.get("/spots")
def get_Spots(lat: float = None, lng: float = None, genre: str = None, skima_time: int = None):
    return get_spots(lat, lng, genre, skima_time)

@app.post("/spots")
def add_Spots(spot: Spot):
    return add_spots(spot)

@app.get("/users")
def get_user():
    return get_user()

@app.post("/users")
def add_user(name: str = None, gender: str = None):
    return add_user(name, gender)

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port = 80)
