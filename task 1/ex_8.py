while True:
    try:
        widget = int(input('Enter the number of widgets: '))
        if widget < 0 or widget == 0:
            raise ValueError
    except ValueError:
        print("Invalid integer. The number must be positive integer")
    else:
        break

while True:
    try:
        gizmo = int(input('Enter the number of gizmos: '))
        if gizmo < 0 or gizmo == 0:
            raise ValueError
    except ValueError:
        print("Invalid integer. The number must be positive integer")
    else:
        total = (widget * 0.075) + (gizmo * 0.112)
        print("The total weight of the order:", total, 'kg')
        break
