import random

def spots(l1):
    """
    random_spots = tuple(random.sample(result, 2))
    """

    response_list = []

    for row in l1:
        store_id = row[0]
        name = row[1]
        latitude = row[2]
        longitude = row[3]
        genre = row[4]

        position = {
            "latitude": latitude,
            "longitude": longitude
        }

        response = {
            "store_id": store_id,
            "name": name,
            "position": position,
            "genre": genre
        }

        response_list.append(response)
    
    return {"spots": response_list } 


def spot_id(result):
    for row in result:
        store_id = row[0]
        response = {
            "store_id": store_id
        }
    
    return response


def users(result):
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
