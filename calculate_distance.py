from math import sqrt, acos, sin, cos, radians
from math import sin, cos, sqrt, atan2, radians


def get_distance(x1, y1, x2, y2):
        r = 6378.137
        distance = r * acos(sin(radians(y1))*sin(radians(y2)) + cos(radians(y1))*cos(radians(y2))*cos(radians(x2-x1)))
        distance *= 1000
        return distance

