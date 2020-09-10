while True:
    try:
        n = int(input('Enter a positive integer: '))
        if n < 0 or n == 0:
            raise ValueError
    except ValueError:
        print("Invalid integer. The number must be positive integer")
    else:
        sum = (n * (n + 1)) / 2
        print("The sum of the first", n, "positive integers:", sum)
        break
