print("""
1. Add
2. Sub
3. Mul
4. Div
""")

user_choice = input("Enter your choice : ")

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

if user_choice == "1":
    result = num_1 + num_2
    print("Sum is",result)
elif user_choice == "2":
    result = num_1 - num_2
    print("Diff is", result)
