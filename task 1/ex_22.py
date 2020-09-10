from math import sqrt

s1 = float(input("Enter s1: "))
s2 = float(input("Enter s2: "))
s3 = float(input("Enter s3: "))

s = (s1 + s2 + s3) / 2
area = sqrt(s * (s - s1) * (s - s2) * (s - s3))

print("Area of the Triangle: %.2f" % area)
