import MySQLdb
from db import DB
from json_response import response_users, user_id

def get_user():
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name)

    cursor = connector.cursor()
    sql = "select * from users;"
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close
    connector.close

    return response_users(result)


def add_user(user):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name)

    cursor = connector.cursor()
    sql = "insert into users value (0, '%s', '%s');" % (user.name , user.gender)
    cursor.execute(sql)
    connector.commit()

    sql = "select * from users;"
    cursor.execute(sql)
    result = cursor.fetchall()
   
    cursor.close
    connector.close

    return user_id(result)
