import MySQLdb
import random
from lat_calculate import get_min_lat, get_max_lat
from lng_calculate import get_min_lng, get_max_lng
from json_response import spots,spot_id

def get_spots(lat, lng, genre, skima_time):
    connector = MySQLdb.connect(
        user='root',
        passwd='hoseitaro',
        host='localhost',
        db='skimatti_db',
        charset='utf8')
    
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
    
    cursor.close
    connector.close

    return spots(result)


def add_spots(spot):
    connector = MySQLdb.connect(
        user='root',
        passwd='hoseitaro',
        host='localhost',
        db='skimatti_db',
        charset='utf8')

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
