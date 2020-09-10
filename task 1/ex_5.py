print('// Bottle Deposits //')

bottle_0_10 = int(input('drink containers holding 1 liter or less: '))
bottle_0_25 = int(input('drink containers holding more than 1 liter: '))

print('sum for bottle of $0.10 :--> $', round(bottle_0_10 * 0.10, 2))
print('sum for bottle of $0.25 :--> $', round(bottle_0_25 * 0.25, 2))

print('total sum :--> ${0}'.format(round(bottle_0_10 * 0.10, 2) + round(bottle_0_25 * 0.25, 2)))