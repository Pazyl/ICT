# 1 квадратный фут = 0.000022959 акров.
# 1 акр = 43 560 квадратных футов.
from math import trunc

print('Enter the length (y) and width (x) of a farmer’s ﬁeld in feet')

width_ft = float(input('enter the width: '))
length_ft = float(input('enter the length: '))

print('Area of the field in acres =', (width_ft * length_ft) / 43560, 'ac')
print('Area of the field in acres =', format((width_ft * length_ft) / 43560, '.12f'), 'ac')
