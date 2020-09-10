total_s = int(input("Enter the total number of seconds: "))

d = total_s / (3600 * 24)
total_s = total_s % (3600 * 24)

h = total_s / 3600
total_s = total_s % 3600

m = total_s / 60
total_s = total_s % 60

s = total_s

print("D:HH:MM:SS: ", "%d:%02d:%02d:%02d" % (d, h, m, s))
