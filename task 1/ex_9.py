balance = float(input('Enter the balance: '))

print('after 1 year: ${0}'.format(round(balance * (1 + (0.04 / 1)) ** (1 * 1), 2)))
print('after 2 year: ${0}'.format(round(balance * (1 + (0.04 / 1)) ** (1 * 2), 2)))
print('after 3 year: ${0}'.format(round(balance * (1 + (0.04 / 1)) ** (1 * 3), 2)))

# A = P (1 + [r / n]) ^ nt
