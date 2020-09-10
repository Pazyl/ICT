a = int(input('Enter the a: '))
b = int(input('Enter the b: '))
c = int(input('Enter the c: '))

max_v = max(a, b, c)
min_v = min(a, b, c)

middle = (a + b + c) - (max_v + min_v)

print("Sorted:", min_v, middle, max_v)
