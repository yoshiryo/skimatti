import MySQLdb

from logger import get_session_id, logging
from db import DB
from json_response import response_users, response_user_id

def list_users():
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name,
        charset = DB.charset)

    cursor = connector.cursor()
    sql = "select * from users;"
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close
    connector.close

    logging('null', "GET /users", get_session_id())
    return response_users(result)


def get_user(user_id):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name,
        charset = DB.charset)

    cursor = connector.cursor()
    sql = "select * from users where user_id = '%s'" % (user_id)
    cursor.execute(sql)
    result = cursor.fetchall()
    
    cursor.close
    connector.close

    logging(user_id, "GET /users/{usre_id}", get_session_id())
    return response_users(result)

def add_user(user):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name,
        charset = DB.charset)

    cursor = connector.cursor()
    sql = "insert into users value (0, '%s', '%s');" % (user.age, user.gender)
    cursor.execute(sql)
    connector.commit()

    sql = "select * from users;"
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close
    connector.close

    logging('null', "POST /users", get_session_id())
    return response_user_id(result)


def update_user(user_id, user):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name,
        charset = DB.charset)

    cursor = connector.cursor()
    sql = "update users set age = '%s', gender = '%s' where user_id='%s';" % (user.age, user.gender, user_id)
    cursor.execute(sql)
    connector.commit()

    sql = "select * from users where user_id = '%s'" % (user_id);
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close
    connector.close

    logging(user_id, "POST /users/{usre_id}", get_session_id())
    return response_user_id(result)
