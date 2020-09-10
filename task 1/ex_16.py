# math.pow(X, Y) - X^Y

from math import pi, pow

radius = int(input('Radius - r: '))

print('Area - S:', pi * pow(radius, 2))
print('Volume - V', (4 / 3) * pi * pow(radius, 3))
