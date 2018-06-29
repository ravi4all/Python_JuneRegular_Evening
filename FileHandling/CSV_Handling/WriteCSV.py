import csv
data = [
    "Firstname,Lastname".split(","),
    "Sachin,Tendulkar".split(","),
    "Rahul,Dravid".split(","),
    "MS,Dhoni".split(","),
    "Virat,Kohli".split(",")
]
with open('data.csv','w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)