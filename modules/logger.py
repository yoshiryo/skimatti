import uuid

import MySQLdb

from schemas.db import DB

def get_session_id():
    return uuid.uuid4().hex

def logging(user_id, api_path, session_id = None):
    connector = MySQLdb.connect(
        user=DB.user,
        passwd=DB.password,
        host=DB.host,
        db=DB.name,
        charset=DB.charset)

    cursor = connector.cursor()
    sql = "insert into log values(0, %s, '%s', '%s', now());" % (user_id, session_id, api_path)
    cursor.execute(sql)
    connector.commit()
    connector.close()


def log_init():
    connector = MySQLdb.connect(
        user=DB.user,
        passwd=DB.password,
        host=DB.host,
        db=DB.name,
        charset=DB.charset)

    cursor = connector.cursor()
    sql = 'delete from log;'
    cursor.execute(sql)
    sql = 'alter table log auto_increment = 1;'
    cursor.execute(sql)
    connector.close()


def get_travel_time(session_id):
    connector = MySQLdb.connect(
        user=DB.user,
        passwd=DB.password,
        host=DB.host,
        db=DB.name,
        charset=DB.charset)

    cursor = connector.cursor()
    sql = 'select time_stamp from log where session_id = "%s";' % session_id
    cursor.execute(sql)

    result = cursor.fetchall()
    time1 = result[0][0]
    time2 = result[1][0]
    
    connector.close()
    
    time = time2 - time1
    print(time)
    return {"travel_time": time}
