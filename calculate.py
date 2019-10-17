from math import  pi, sin, cos, radians, floor

def get_min_lat(lat, skima_time):
    skima_distance = skimatime *
    r = 6356752.314
    lat_distance = ( 360 * skima_distance ) / ( 2 * pi * r )
    min_lat = lat - lat_distance
    return min_lat

def get_max_lat(lat, skima_time):
    skima_distance = skimatime *
    r = 6356752.314
    lat_distance = ( 360 * skima_distance ) / ( 2 * pi * r )
    max_lat = lat + lat_distance
    return max_lat

def get_min_lng(lng, skima_time):
    skima_distance = skima_sime *
    r=6378137
    lng_distance = ( 360 * skima_distance ) / ( 2 * pi * ( r * cos( radians( lat ) )
    min_lng = lng - lng_distance
    return min_lng

def get_min_lng(lng, skima_time):
    skima_distance = skima_sime *
    r=6378137
    lng_distance = ( 360 * skima_distance ) / ( 2 * pi * ( r * cos( radians( lat ) )
    max_lng = lng + lng_distance
    return max_lng
