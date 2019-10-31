import random

from calculate_distance import get_distance


def response_spots(spots, visited_spots, lat, lng, skima_time, spots_amount):

    response_list = []

    visited_list = []

    for row in visited_spots:
        spot_id = row[1]
        visited_list.append(spot_id)

    for row in spots:
        spot_id = row[0]
        name = row[1]
        spot_lat = row[2]
        spot_lng = row[3]
        genre = row[4]
        
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
                    "genre": genre
                }

                response_list.append(response)
                
            elif ( skima_time * 80 ) >= get_distance(lat, lng, spot_lat, spot_lng):
                position = {
                    "latitude": spot_lat,
                    "longitude": spot_lng
                }

                response = {
                    "spot_id": spot_id,
                    "name": name,
                    "position": position,
                    "genre": genre
                }

                response_list.append(response)

    if spots_amount is None or len(response_list) < spots_amount:
        random_list = tuple(random.sample(response_list, len(response_list)))
        return {"spots": random_list }
    
    else:
        random_list = tuple(random.sample(response_list, spots_amount))
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
        name = row[1]
        gender = row[2]

        response = {
            "user_id" : user_id,
            "name" : name,
            "gender" : gender
        }

        response_list.append(response)
    return {"users": response_list }


def user_id(result):
    for row in result:
        user_id = row[0]
        response = {
            "user_id":user_id
        }
    
    return response    
