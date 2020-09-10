# 1 feet = 12 inches (in) *12
# 1 feet = 0,333333 yards (yd) /3
# 1 feet = 0,000189394 miles (mi) /5280

feet = int(input('Feet: '))
print('{0} ft --> {1} in'.format(feet, feet * 12))
print('{0} ft --> {1} yd'.format(feet, feet / 3))
print('{0} ft --> {1} mi'.format(feet, feet / 5280))

