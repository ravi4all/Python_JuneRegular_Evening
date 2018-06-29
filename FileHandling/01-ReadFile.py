# file = open('demo.txt', 'r')

# by default file opens in read mode
file = open('demo.txt')

# data = file.read()

# data = file.readline()

# data = file.readlines()

data = file.read(5)
print(data)

file.close()