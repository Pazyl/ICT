while True:
    try:
        choice = int(input('choice 1: the Height in [inches] and the Weight in [pounds]\n'
                           'choice 2: the Height in [meters] and the Weight in [kilograms]\n'
                           'Your choice: '))
        if choice < 1 or choice > 2:
            raise ValueError
    except ValueError:
        print("Invalid choice. The choice must be number [1] or [2]")
    else:
        break

height = float(input("Enter the height: "))
weight = float(input("Enter the weight: "))

if choice == 1:
    bmi = weight / height ** 2 * 703
    print("BMI is %.2f lb/in^2" % bmi)

elif choice == 2:
    bmi = weight / height ** 2
    print("BMI is %.2f kg/m^2" % bmi)
