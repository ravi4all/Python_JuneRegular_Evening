def calc():
    try:
        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))
        a = num_1 + num_2
        print("Sum is",a)

        b = num_1 - num_2
        print("Diff is",b)

        c = num_1 / num_2
        print("Div is",c)

        d = num_1 * num_2
        print("Mul is",d)

    except:
        print("Invalid Input")
        # recursion - when a function calls itself repeatedly
        calc()

calc()