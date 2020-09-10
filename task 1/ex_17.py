# 1 J = 2.777 * 10^-7 kW·h (/ 3 600 000)
# 1 kW·h = 8.9 cents
# 2.777 * 10^-7 == 2.777e-7

m = float(input('Enter the water - m: '))
d_t = float(input('Enter the temperature - ΔT: '))

q = m * d_t * 4.186

print('Energy - Q: %d' % q)

cost = (q / 3600000) * 8.9

print('Cost of boiling water: %.2f cents' % cost)
