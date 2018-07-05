def calc():
    try:
        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))
        a = num_1 + num_2
        b = num_1 - num_2
        c = num_1 / num_2
        d = num_1 * num_2

    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid input")

    else:
        print("Sum is", a)
        print("Diff is", b)
        print("Div is", c)
        print("Mul is", d)

    finally:
        print("I will always execute...")

calc()