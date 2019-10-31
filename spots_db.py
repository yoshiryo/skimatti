import MySQLdb

from db import DB
from calculate_lat import get_min_lat, get_max_lat
from calculate_lng import get_min_lng, get_max_lng
from json_response import response_spots, spot_id, response_visited_spots, visited_spot_id


def get_spots(lat, lng, genre, skima_time, user_id, spots_amount):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,    
        host = DB.host,
        db = DB.name)
    
    min_lat = get_min_lat(lat, skima_time)
    max_lat = get_max_lat(lat, skima_time)
    min_lng = get_min_lng(lat, lng, skima_time)
    max_lng = get_max_lng(lat, lng, skima_time)
    
    cursor = connector.cursor()

    sql = "select * from visited_spots where user_id = '%s'" % (user_id)

    cursor.execute(sql)
    visited_spots = cursor.fetchall()
    
    if lat is None or lng is None:
        sql = "select * from spots;"
     
    elif genre is None:
        sql = "select * from spots where latitude >= '%s' and latitude <= '%s' and longitude >= '%s' and longitude <= '%s';" % (min_lat, max_lat, min_lng, max_lng)
    
    else:
        sql = "select * from spots where latitude >= '%s' and latitude <= '%s' and longitude >= '%s' and longitude <= '%s' and genre = '%s';" % (min_lat, max_lat, min_lng, max_lng, genre)

    cursor.execute(sql)
    spots = cursor.fetchall()
    
    cursor.close
    connector.close   

    return response_spots(spots, visited_spots, lat, lng, skima_time, spots_amount)


def add_spots(spot):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,    
        host = DB.host,
        db = DB.name)

    cursor = connector.cursor()
    sql = "insert into spots value (0, '%s', '%s', '%s', '%s');" % (spot.name, spot.lat, spot.lng, spot.genre)
    cursor.execute(sql)
    connector.commit()

    sql = "select * from spots;"
    cursor.execute(sql)
    spots = cursor.fetchall()

    cursor.close
    connector.close

    return spot_id(spots)


def get_visited_spots():
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,    
        host = DB.host,
        db = DB.name)

    cursor = connector.cursor()
    
    sql = "select * from visited_spots;"
    cursor.execute(sql)
    visited_spots = cursor.fetchall()
    
    cursor.close
    connector.close

    return response_visited_spots(visited_spots)


def add_visited_spots(user_id, spot_id):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,    
        host = DB.host,
        db = DB.name)

    cursor = connector.cursor()
    sql = "insert into visited_spots value ('%s', '%s');" % (user_id, spot_id)
    cursor.execute(sql)
    connector.commit()

    sql = "select * from visited_spots;"
    cursor.execute(sql)
    visited_spots = cursor.fetchall()

    cursor.close
    connector.close

    return visited_spot_id(visited_spots)
