from fastapi import FastAPI
import uvicorn

from spots_db import get_spots, add_spots, get_visited_spots, add_visited_spots, get_plan
from users_db import get_user, add_user, list_users, update_user
from calculate_distance import get_distance
from spot import Spot
from user import User
from identity import Identity
from date_time import Date_time
import change_plan


app=FastAPI()

@app.get("/spots")
def List_Spots(latitude: float = None, longitude: float = None, genre: str = None, skima_time: int = 90, user_id: int = None ,spots_amount: int = None ):
    return get_spots(latitude, longitude, genre, skima_time, user_id, spots_amount)

@app.post("/spots")
def Create_Spot(spot: Spot):
    return add_spots(spot)

@app.get("/users")
def List_Users():
    return list_users()

@app.post("/users")
def Create_User(user: User):
    return add_user(user)

@app.get("/users/{user_id}")
def Get_User(user_id: int):
    return get_user(user_id)

@app.post("/users/{user_id}")
def Update_User(user_id: int, user: User):
    return update_user(user_id, user)

@app.get("/users/{user_id}/visited")
def List_Visited_Spots(user_id: int):
    return get_visited_spots(user_id)

@app.post("/users/{user_id}/visited")
def Update_Visited_Spot(user_id: int, identity: Identity):
    return add_visited_spots(user_id, identity)

@app.get("/spots/{spot_id}/plan")
def Get_Plan(spot_id: int):
    return get_plan(spot_id)

@app.post("/spots/{spot_id}/plan")
def Change_Plan(spot_id: int, date_time: Date_time):
    return change_plan.plan(spot_id, date_time)

@app.get("/calc")
def Calculate_Distance(latitude1: float, longitude1: float, latitude2: float, longitude2: float):
    return { "distance":  get_distance(latitude1, longitude1, latitude2, longitude2) }


if __name__ == "__main__":
   uvicorn.run(app, host = "0.0.0.0", port = 80)
