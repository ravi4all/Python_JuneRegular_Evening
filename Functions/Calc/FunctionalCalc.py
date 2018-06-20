def add(x,y):
    result = x + y
    print("Add called...",result)

def sub(x,y):
    result = x - y
    print("Sub called...",result)

def mul(x,y):
    result = x * y
    print("Mul called...",result)

def div(x,y):
    result = x / y
    print("Div called...",result)

while True:
    
    print("""
    1. Add
    2. Sub
    3. Mul
    4. Div
    """)

    user_choice = input("Enter your choice : ")
    num_1 = float(input("Enter first number : "))
    num_2 = float(input("Enter second number : "))
    operations = {
        "1" : add,
        "2" : sub,
        "3" : mul,
        "4" : div
    }
    opr = operations.get(user_choice)
    # print(opr)
    opr(num_1, num_2)