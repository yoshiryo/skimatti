import MySQLdb

def get_user():
    connector = MySQLdb.connect(
        user='root',
        passwd='',
        host='localhost',
        db='skimatti_db',
        charset='utf8')

    cursor = connector.cursor()
    sql = "select * from users ;"
    cursor.execute(sql)
    result = cursor.fetchall()

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
    json_response = {"users": response_list }

    cursor.close
    connector.close

    return json_response

def add_user(name, gender):
    connector = MySQLdb.connect(
        user='root',
        passwd='',
        host='localhost',
        db='skimatti_db',
        charset='utf8')

    cursor = connector.cursor()
    sql = "insert into users value (0, '%s', '%s');" % (name , gender)
    cursor.execute(sql)
    connector.commit()

    sql = "select * from users;"
    result = cursor.execute(sql)
    result = cursor.fetchall()
    
    for row in result:
        user_id = row[0]
        response = {
            "user_id":user_id
        }

    cursor.close
    connector.close

    return response
