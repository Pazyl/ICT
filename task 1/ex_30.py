pressure = float(input("Enter the pressure in kilopascals (kPa): "))

psi = pressure / 6.895
mmHg = pressure * 7.501
atmospheres = pressure / 101
print("the equivalent pressure in pounds per square inch: %.2f psi" % psi)
print("the equivalent pressure in millimeters of mercury: %.2f mmHg" % mmHg)
print("the equivalent pressure in atmospheres: %.2f atm" % atmospheres)
