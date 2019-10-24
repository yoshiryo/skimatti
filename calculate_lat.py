from math import  pi, cos

def get_min_lat(lat, skima_time):
    skima_distance = skima_time * 80
    r = 6356752.314
    lat_degree = ( 360 * skima_distance ) / ( 2 * pi * r )
    min_lat = lat - lat_degree
    return min_lat

def get_max_lat(lat, skima_time):
    skima_distance = skima_time * 80
    r = 6356752.314
    lat_degree = ( 360 * skima_distance ) / ( 2 * pi * r )
    max_lat = lat + lat_degree
    return max_lat
 
