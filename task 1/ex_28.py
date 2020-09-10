temperature_C = float(input("Enter the air temperature (C): "))
velocity_km_h = float(input("Enter the wind speed (km/h): "))

wci = 13.12 + 0.6215 * temperature_C - 11.37 * pow(velocity_km_h, 0.16) + 0.3965 * temperature_C * pow(velocity_km_h,
                                                                                                       0.16)
print('The wind chill index is', round(wci))

