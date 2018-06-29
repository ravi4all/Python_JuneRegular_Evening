users = []
userData = {}

def postSomething():
    post = input("Enter your post : ")
    # [{'post':'Hello this is my post', 'date':6-29-2018, 'username':'Ram'}]

def viewProfile():
    pass

def updateProfile():
    pass

def deleteProfile():
    pass

def logout():
    pass

def loginSuccess():
    print("""
    1. Post Something
    2. View Profile
    3. Update Profile
    4. Delete Profile
    5. Logout
    """)

def login():
    email = input("Enter your emailId : ")
    pwd = input("Enter your password : ")

    for user in users:
        if user['email'] == email and user['password'] == pwd:
            print("Login Success")
            loginSuccess()
            break
    else:
        print("Login Failed...")

def register():
    inputs = ['name','email','password']
    for i in range(len(inputs)):
        userData[inputs[i]] = input("Enter your {} ".format(inputs[i]))

    users.append(userData.copy())
    print("Registered Successfully...")
    for user in users:
        print(user)

def errorHandler():
    print("Wrong Choice...")

def main():
    while True:
        print("""
        1. Register
        2. Login
        """)

        userChoice = input("Enter your choice : ")

        todo = {
            "1" : register,
            "2" : login
        }

        todo.get(userChoice, errorHandler)()

main()