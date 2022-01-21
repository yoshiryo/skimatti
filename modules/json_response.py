import random
import numpy as np

from  logger import logging, get_session_id
from calculate_distance import get_distance
from calculate_weight import weights_list


def response_spots(spots, visited_spots, lat, lng, skima_time, spots_amount):

    response_list = []

    visited_list = []

    plan_list = []

    for row in visited_spots:
        spot_id = row[1]
        visited_list.append(spot_id)

    for row in spots:
        spot_id = row[0]
        name = row[1]
        spot_lng = row[2]
        spot_lat = row[3]
        genre = row[4]
        stay_time = row[5]
        comment = row[6]
        plan = row[7]

        if spot_id in visited_list:
            continue

        else:
            if lat is None or lng is None:
                position = {
                    "latitude": spot_lat,
                    "longitude": spot_lng
                }

                response = {
                    "spot_id": spot_id,
                    "name": name,
                    "position": position,
                    "genre": genre,
                    "stay_time": stay_time,
                    "comment": comment,
                    "plan": plan
                }

                response_list.append(response)
                plan_list.append(plan)

            elif ( (skima_time - stay_time) / 2 * 60 ) >= get_distance(lat, lng, spot_lat, spot_lng):
                position = {
                    "latitude": spot_lat,
                    "longitude": spot_lng
                }

                response = {
                    "spot_id": spot_id,
                    "name": name,
                    "position": position,
                    "genre": genre,
                    "stay_time": stay_time,
                    "comment": comment,
                    "plan": plan
                }

                response_list.append(response)
                plan_list.append(plan)

    if len(response_list) == 0:
        return {"spots": response_list }
    

    elif spots_amount is None:
        if len(response_list) < 4:
            random_list = tuple(np.random.choice(response_list, size = len(response_list), replace=False, p = weights_list(plan_list)))
            return {"spots": random_list }

        else:
            random_list = tuple(np.random.choice(response_list, size = 4, replace=False, p = weights_list(plan_list)))
            return {"spots": random_list }

    else:
        if len(response_list) < spots_amount:
            random_list = tuple(np.random.choice(response_list, size = len(response_list), replace=False, p = weights_list(plan_list)))
            return {"spots": random_list }

        else:
            random_list = tuple(np.random.choice(response_list, size = spots_amount, replace=False, p = weights_list(plan_list)))
            return {"spots": random_list }

def response_visited_spots(visited_spots):
    response_list = []

    for row in visited_spots:
        user_id = row[0]
        spots_id = row[1]

        response = {
            "user_id" : user_id,
            "spots_id": spots_id
        }

        response_list.append(response)

    return {"visited_spots": response_list }


def spot_id(spots):
    for row in spots:
        spot_id = row[0]
        response = {
            "spot_id": spot_id
        }

    return response


def visited_spot_id(visited_spots):
    for row in visited_spots:
        spot_id = row[1]
        response = {
            "spot_id": spot_id
        }

    return response


def response_users(result):
    response_list = []

    for row in result:
        user_id = row[0]
        age = row[1]
        gender = row[2]

        response = {
            "user_id" : user_id,
            "age" : age,
            "gender" : gender
        }

        response_list.append(response)
    return {"users": response_list }


def response_user_id(result):
    for row in result:
        user_id = row[0]
        response = {
            "user_id":user_id
        }

    return response


def response_plan(result):
    for row in result:
        plan = row[7]
        response = {
            "plan":plan
        }

    return response

    
