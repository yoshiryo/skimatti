from math import  pi, cos, radians

def get_min_lng(lat, lng, skima_time):
    skima_distance = skima_time * 80
    r = 6378137 * cos(radians(lat))
    lng_distance = ( 360 * skima_distance ) / ( 2 * pi * r )
    min_lng = lng + lng_distance
    return min_lng


def get_max_lng(lat, lng, skima_time):
    skima_distance = skima_time * 80
    r = 6378137 * cos(radians(lat))
    lng_distance = ( 360 * skima_distance ) / ( 2 * pi * r )
    max_lng = lng - lng_distance
    return max_lng
