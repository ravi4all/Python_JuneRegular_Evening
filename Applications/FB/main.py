from datetime import  datetime

users = []
userData = {}

posts = []
postData = {}

def postSomething(username):
    post = input("Enter your post : ")
    # [{'post':'Hello this is my post', 'date':6-29-2018, 'username':'Ram'}]
    postData['post'] = post
    postData['username'] = username
    postData['date'] = datetime.now().date()

    posts.append(postData.copy())
    for p in posts:
        print(p)

    loginSuccess(username)

def viewProfile(username):
    for user in users:
        if user['name'] == username:
            print("Email ID :",user['email'])
    for p in posts:
        if p['username'] == username:
            print("Post :",p['post'])
            print("Date :",p['date'])

    loginSuccess(username)

def updateProfile(username):
    toUpdate = input("What do you want to update ? ")
    updatedValue = input("Enter updated {}".format(toUpdate))

    for user in users:
        if user['name'] == username:
            user[toUpdate] = updatedValue

    loginSuccess(username)

def deleteProfile(username):
    pass

def logout(username):
    pass

def loginSuccess(username):
    print("""
    1. Post Something
    2. View Profile
    3. Update Profile
    4. Delete Profile
    5. Logout
    """)
    userinput = input("Enter your choice : ")
    operations = {
        "1" : postSomething,
        "2" : viewProfile,
        "3" : updateProfile,
        "4" : deleteProfile,
        "5" : logout
    }
    operations.get(userinput, errorHandler)(username)

def login():
    email = input("Enter your emailId : ")
    pwd = input("Enter your password : ")

    for user in users:
        if user['email'] == email and user['password'] == pwd:
            print("Login Success")
            loginSuccess(user['name'])
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

def errorHandler(*args):
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