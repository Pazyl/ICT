num = int(input("enter a 4 digit numbers: "))

x1 = num // 1000

num = num - x1 * 1000
x2 = num // 100

num = num - x2 * 100
x3 = num // 10

num = num - x3 * 10
x4 = num // 1

print("The sum of digits is", x1 + x2 + x3 + x4)
