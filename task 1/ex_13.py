cents = int(input('Cents: '))

print(cents // 200, "toonies [200]")
cents = cents % 200

print(cents // 100, "loonies [100]")
cents = cents % 100

print(cents // 25, "quarters [25]")
cents = cents % 25

print(cents // 10, "dimes [10]")
cents = cents % 10

print(cents // 5, "nickels [5]")
cents = cents % 5

print(cents, "pennies [1]")
