import MySQLdb
from calculate import get_min_lat, get_max_lat, get_min_lng, get_max_lng
import random
def get_spots(lat, lng, genre, skima_time):
    connector = MySQLdb.connect(
        user='root',
        passwd='',
        host='localhost',
        db='skimatti_db',
        charset='utf8')
    
    min_lat = get_min_lat(lat, skima_time)
    max_lat = get_max_lat(lat, skima_time)
    min_lng = get_min_lng(lng, skima_time)
    max_lng = get_max_lng(lng, skima_time)
    
    cursor = connector.cursor()
    sql = "select * from spots where latitude >= '%s' and latitude <= '%s' and longitude >= '%s' and longitude <= '%s' and genre = '%s';" % (min_lat, max_lat, min_lng, max_lng, genre)
    cursor.execute(sql)
    
    result = cursor.fetchall()
    
    r = tuple(random.sample(result, 2)) 
    
    response_list = []

    for row in r:
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
    json_response = {"spots": response_list }

    cursor.close
    connector.close

    return json_response

def add_spots(spot):
    connector = MySQLdb.connect(
        user='root',
        passwd='',
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

    for row in result:
        store_id = row[0]
        response = {
            "store_id": store_id
        }

    cursor.close
    connector.close

    return response
