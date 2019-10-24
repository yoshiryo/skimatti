from math import sin, cos, sqrt, atan2, radians

def get_distance(lat1, lng1, lat2, lng2):
    r = 6373

    dlng = radians(lng2) - radians(lng1)
    dlat = radians(lat2) - radians(lat1)
    
    a = (sin(dlat / 2)) ** 2 + cos(lat1) * cos(lat2) * (sin(dlng / 2)) ** 2
    c = 2 * atan2( sqrt(a), sqrt(1-a))
    
    distance = r * c
    
    return distance
