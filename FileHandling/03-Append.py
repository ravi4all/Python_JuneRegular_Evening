# append - it do not overwrite the previous data
# it will insert new data after previous data
file = open('demo_1.txt', 'a')

data = "\nThis script is written in python"

file.write(data)

file.close()