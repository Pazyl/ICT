# 1 ft = 0.3048 m

print('Enter the width (x) and length (y) of a room')

while True:
    value = float(input('feet (1) or meters (2): '))
    if value == 1 or value == 2:
        break

if value == 1:
    width_ft = float(input('enter the width: '))
    length_ft = float(input('enter the length: '))
    print('Area of a Room =', width_ft * length_ft, 'ft^2')
else:
    width_m = float(input('enter the width: '))
    length_m = float(input('enter the length: '))
    print('Area of a Room =', width_m * length_m, 'm^2')
