# file = open('demo.txt','r')
# file.read()
# file.close()

with open('demo.txt','r') as file:
    data = file.read()
    print(data)