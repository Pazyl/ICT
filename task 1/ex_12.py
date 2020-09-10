from math import radians, cos, sin, acos


def distance(t1, g1, t2, g2):
    # latitude --> t1, t2
    # longitude --> g1, g2

    t1 = radians(t1)
    t2 = radians(t2)
    g1 = radians(g1)
    g2 = radians(g2)

    distance = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

    return distance


print(distance(float(input('Latitude 1: ')),
               float(input('Longitude 1: ')),
               float(input('Latitude 2: ')),
               float(input('Longitude 2: '))), 'km')
