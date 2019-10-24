import MySQLdb
import random
from db import DB
from calculate_lat import get_min_lat, get_max_lat
from calculate_lng import get_min_lng, get_max_lng
from json_response import spots,spot_id
from calculate_distance import get_distance


def get_spots(lat, lng, genre, skima_time):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,    
        host = DB.host,
        db = DB.name,
        charset = DB.charset)
    
    min_lat = get_min_lat(lat, skima_time)
    max_lat = get_max_lat(lat, skima_time)
    min_lng = get_min_lng(lat, lng, skima_time)
    max_lng = get_max_lng(lat, lng, skima_time)
    
    cursor = connector.cursor()
    
    if genre is None:
        sql = "select * from spots where latitude >= '%s' and latitude <= '%s' and longitude >= '%s' and longitude <= '%s';" % (min_lat, max_lat, min_lng, max_lng)
    
    else:
        sql = "select * from spots where latitude >= '%s' and latitude <= '%s' and longitude >= '%s' and longitude <= '%s' and genre = '%s';" % (min_lat, max_lat, min_lng, max_lng, genre)
    
    cursor.execute(sql)
    result = cursor.fetchall()
    
    response_list = []

    for row in result:
        store_id = row[0]
        name = row[1]
        latitude = row[2]
        longitude = row[3]
        genre = row[4]
        
        if ( skima_time * 80 ) >= get_distance(lat, lng, latitude, longitude):

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

    cursor.close
    connector.close
   
    return {"spots": response_list }


def add_spots(spot):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name,
        charset = DB.charset)

    cursor = connector.cursor()
    sql = "insert into spots value (0, '%s', '%s', '%s', '%s');" % (spot.name, spot.lat, spot.lng, spot.genre)
    cursor.execute(sql)
    connector.commit()

    sql = "select * from spots;"
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close
    connector.close

    return spot_id(result)
