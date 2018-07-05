# assert and raise

# def register():
#     name = input("Enter your name : ")
#     email = input("Enter your email : ")
#     age = int(input("Enter your age : "))
#     try:
#         if age > 18:
#             print("Welcome")
#         elif age < 18:
#             raise ValueError("You are not allowed...")
#     except ValueError as err:
#         print(err)
#
#     print("Hello {}".format(name))
#     print("Register successfully...")

# def register():
#     name = input("Enter your name : ")
#     email = input("Enter your email : ")
#     age = int(input("Enter your age : "))
#     if age > 18:
#         print("Welcome")
#     elif age < 18:
#         # print("Not allowed...")
#         raise ValueError("You are not allowed...")
#
#     print("Hello {}".format(name))
#     print("Register successfully...")

def register():
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    age = int(input("Enter your age : "))

    assert (age > 18), "You are not allowed"

    print("Welcome")
    print("Hello {}".format(name))
    print("Register successfully...")

try:
    register()
except AssertionError as err:
    print(err)
