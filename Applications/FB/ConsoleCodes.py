Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = "Sachin Tendulkar"
>>> name.split()
['Sachin', 'Tendulkar']
>>> name = "Sachin,Tendulkar"
>>> name.split()
['Sachin,Tendulkar']
>>> name.split(",")
['Sachin', 'Tendulkar']
>>> data = [
    "Firstname,Lastname".split(","),
    "Sachin,Tendulkar".split(","),
    "Rahul,Dravid".split(","),
    "MS,Dhoni".split(","),
    "Virat,Kohli".split(",")
]
>>> data
[['Firstname', 'Lastname'], ['Sachin', 'Tendulkar'], ['Rahul', 'Dravid'], ['MS', 'Dhoni'], ['Virat', 'Kohli']]
>>> for row in data
SyntaxError: invalid syntax
>>> for row in data:
	print(row)

	
['Firstname', 'Lastname']
['Sachin', 'Tendulkar']
['Rahul', 'Dravid']
['MS', 'Dhoni']
['Virat', 'Kohli']
>>> for i in range(1,10):
	print(i)

	
1
2
3
4
5
6
7
8
9
>>> for i in range(1,10):
	print(i, end='')

	
123456789
>>> x = {}
>>> x['name'] = 'ram'
>>> x['pwd'] = '1234'
>>> x['email'] = 'ram@gmail.com'
>>> x
{'name': 'ram', 'pwd': '1234', 'email': 'ram@gmail.com'}
>>> users = []
>>> users.append(x)
>>> users
[{'name': 'ram', 'pwd': '1234', 'email': 'ram@gmail.com'}]
>>> x['name'] = 'Shyam'
>>> x['pwd'] = '124567889'
>>> x['email'] = 'shyam@yahoo.in'
>>> x
{'name': 'Shyam', 'pwd': '124567889', 'email': 'shyam@yahoo.in'}
>>> users.append(x)
>>> users
[{'name': 'Shyam', 'pwd': '124567889', 'email': 'shyam@yahoo.in'}, {'name': 'Shyam', 'pwd': '124567889', 'email': 'shyam@yahoo.in'}]
>>> from datetime import datetime
>>> datetime.now().date()
datetime.date(2018, 6, 29)
>>> print(datetime.now().date())
2018-06-29
>>> print(datetime.now())
2018-06-29 16:57:01.878473
>>> print(datetime.now().time())
16:57:13.190131
>>> 
