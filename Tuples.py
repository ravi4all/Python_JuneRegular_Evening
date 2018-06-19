Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = (10,12,13,15,19,21,22)
>>> data[0]
10
>>> data[0:4]
(10, 12, 13, 15)
>>> data[-1]
22
>>> data[0] = 100
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> a = 10
>>> a = 10,
>>> a
(10,)
>>> a = 10,12,13,14
>>> a
(10, 12, 13, 14)
>>> emp = name, company, salary = 'Ram', 'TCS', 25000
>>> emp
('Ram', 'TCS', 25000)
>>> name
'Ram'
>>> company
'TCS'
>>> salary
25000
>>> 
