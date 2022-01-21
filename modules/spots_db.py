import MySQLdb
import sys

from logger import get_session_id, logging
from schemas.db import DB
from json_response import response_spots, spot_id, response_visited_spots, visited_spot_id, response_plan


def get_spots(lat, lng, genre, skima_time, user_id, spots_amount):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name,
        charset = DB.charset)

    cursor = connector.cursor()

    sql = "select * from visited_spots where user_id = '%s'" % (user_id)

    cursor.execute(sql)
    visited_spots = cursor.fetchall()

    if lat is None or lng is None:
        sql = "select * from spots;"

        cursor.execute(sql)
        spots = cursor.fetchall()

        cursor.close
        connector.close

        return response_spots(spots, visited_spots, lat, lng, skima_time, spots_amount)
        sys.exit()
        

    if genre is None:
        sql = "select * from spots;"

    else:
        sql = "select * from spots where genre = '%s';" % (genre)


    cursor.execute(sql)
    spots = cursor.fetchall()

    cursor.close
    connector.close

    response = response_spots(spots, visited_spots, lat, lng, skima_time, spots_amount)
    if user_id is not None:
        session_id = get_session_id()
        response.update({"session_id": session_id})
        logging(user_id, "GET /spots", session_id)

    return response    


def add_spots(spot):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name,
        charset = DB.charset)

    cursor = connector.cursor()
    sql = "insert into spots value (0, '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (spot.name, spot.longitude, spot.latitude, spot.genre, spot.stay_time, spot.comment, spot.plan)
    cursor.execute(sql)
    connector.commit()

    sql = "select * from spots;"
    cursor.execute(sql)
    spots = cursor.fetchall()

    cursor.close
    connector.close

    logging('null', "POST /spots", get_session_id())
    return spot_id(spots)


def get_visited_spots(user_id):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name,
        charset = DB.charset)

    cursor = connector.cursor()

    sql = "select * from visited_spots where user_id = '%s';" % (user_id)
    cursor.execute(sql)
    visited_spots = cursor.fetchall()

    cursor.close
    connector.close
    
    logging(user_id, "GET /users/{user_id}/visited", get_session_id())

    return response_visited_spots(visited_spots)


def add_visited_spots(user_id, number):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name,
        charset = DB.charset)

    cursor = connector.cursor()
    sql = "insert into visited_spots value ('%s', '%s');" % (user_id, number.spot_id)
    cursor.execute(sql)
    connector.commit()

    sql = "select * from visited_spots;"
    cursor.execute(sql)
    visited_spots = cursor.fetchall()

    cursor.close
    connector.close

    logging(user_id, "POST /users/{user_id}/visited", number.session_id)

    return visited_spot_id(visited_spots)


def get_plan(spot_id):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name,
        charset = DB.charset)

    cursor = connector.cursor()
    sql = "select * from spots where spot_id = '%s'" % (spot_id)
    cursor.execute(sql)
    result = cursor.fetchall()
    
    cursor.close
    connector.close

    return response_plan(result)

    
