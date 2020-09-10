from math import tan, pi

s = float(input('Enter the length of a side: '))
n = float(input('Enter the number of sides'))

area = (n * s ** 2) / (4 * tan(pi / n))

print('Area of a Regular Polygon: ', area)