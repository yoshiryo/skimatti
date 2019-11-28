import MySQLdb
import sched, time, datetime

from db import DB


def change_plan_on(spot_id):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name,
        charset = DB.charset)

    cursor = connector.cursor()
    sql = "update spots set plan = 'A' where spot_id='%s';" % (spot_id)
    cursor.execute(sql)
    connector.commit()

    sql = "select * from spots where spot_id = '%s'" % (spot_id);
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close
    connector.close
    
    return spot_id


def change_plan_off(spot_id):
    connector = MySQLdb.connect(
        user = DB.user,
        passwd = DB.password,
        host = DB.host,
        db = DB.name,
        charset = DB.charset)

    cursor = connector.cursor()
    sql = "update spots set plan = 'None' where spot_id='%s';" % (spot_id)
    cursor.execute(sql)
    connector.commit()

    sql = "select * from spots where spot_id = '%s'" % (spot_id);
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close
    connector.close

    return spot_id

def plan(spot_id, date_time):

    s = sched.scheduler(time.time, time.sleep)
 
    et1 = datetime.datetime(date_time.year, date_time.month, date_time.date, date_time.hour, date_time.minute) 
    et1 = int(time.mktime(et1.timetuple()))  
 
    et2 = datetime.datetime(date_time.year, date_time.month, date_time.date, date_time.hour + 3, date_time.minute)
    et2 = int(time.mktime(et2.timetuple()))

    s.enterabs(et1, 1, change_plan_on, argument=(spot_id,))
    s.enterabs(et2, 1, change_plan_off, argument=(spot_id,))
    s.run()
