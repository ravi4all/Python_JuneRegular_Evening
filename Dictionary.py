Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> emp = {'id':101,'name':'Ram','company':'TCS','sal':25000}
>>> emp
{'id': 101, 'name': 'Ram', 'company': 'TCS', 'sal': 25000}
>>> emp[1]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    emp[1]
KeyError: 1
>>> emp['name']
'Ram'
>>> emp.keys()
dict_keys(['id', 'name', 'company', 'sal'])
>>> emp.values()
dict_values([101, 'Ram', 'TCS', 25000])
>>> emp.items()
dict_items([('id', 101), ('name', 'Ram'), ('company', 'TCS'), ('sal', 25000)])
>>> emp['address'] = 'Delhi'
>>> emp
{'id': 101, 'name': 'Ram', 'company': 'TCS', 'sal': 25000, 'address': 'Delhi'}
>>> for item in emp:
	print(item)

	
id
name
company
sal
address
>>> for item in emp.items():
	print(item)

	
('id', 101)
('name', 'Ram')
('company', 'TCS')
('sal', 25000)
('address', 'Delhi')
>>> for i in range(len(emp)):
	print("Id" : emp['id'])
	
SyntaxError: invalid syntax
>>> for item in emp.items():
	print(item)

	
('id', 101)
('name', 'Ram')
('company', 'TCS')
('sal', 25000)
('address', 'Delhi')
>>> emp.get('id')
101
>>> emp = {'id':[1,2,3,4],'name':['Ram','Shyam','Mohan','Gopal'],'company':[23000,45000,25000,21000]}
>>> emp
{'id': [1, 2, 3, 4], 'name': ['Ram', 'Shyam', 'Mohan', 'Gopal'], 'company': [23000, 45000, 25000, 21000]}
>>> emp['name']
['Ram', 'Shyam', 'Mohan', 'Gopal']
>>> emp = {'id':[1,2,3,4],'name':['Ram','Shyam','Mohan','Gopal'],'salary':[23000,45000,25000,21000],'company':['TCS','IBM','HCL','IBM']}
>>> print(emp['id'][0], emp['name'][0], emp['salary'][0])
1 Ram 23000
>>> for i in range(len(emp['id'])):
	print(emp['id'][i], emp['name'][i],emp['company'][i], emp['salary'][i])

	
1 Ram TCS 23000
2 Shyam IBM 45000
3 Mohan HCL 25000
4 Gopal IBM 21000
>>> 
