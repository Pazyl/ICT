p = float(input("Enter the pressure in pascals: "))
v = float(input("Enter the volume in liters: "))

choice = input("Choose Fahrenheit, Celsius, or Kelvin (F / C / K): ")

if choice.lower() == "f":
    temp = float(input("Enter the temperature: "))
    kelvin = (temp - 32) * 5 / 9 + 273.15
    n = p * v / (8.314 * kelvin)
    print("There are %.2f moles of gas." % n)

elif choice.lower() == "c":
    temp = float(input("Enter the temperature: "))
    kelvin = temp + 273.15
    n = p * v / (8.314 * kelvin)
    print("There are %.2f moles of gas." % n)

elif choice.lower() == "k":
    kelvin = float(input("Enter the temperature: "))
    n = p * v / (8.314 * kelvin)
    print("There are %.2f moles of gas." % n)
