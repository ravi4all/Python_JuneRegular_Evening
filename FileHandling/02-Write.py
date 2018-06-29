# when file is open in write mode and if file do not
# exist then it creates a new file
file = open('demo_1.txt', 'w')

data = "This file is written by python script"

file.write(data)

file.close()