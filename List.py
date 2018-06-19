Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = ['hi','hello',101,102,23.5,26.7]
>>> type(data)
<class 'list'>
>>> data[0]
'hi'
>>> data[0] = 'bye'
>>> data
['bye', 'hello', 101, 102, 23.5, 26.7]
>>> data[0:5]
['bye', 'hello', 101, 102, 23.5]
>>> data[0:50]
['bye', 'hello', 101, 102, 23.5, 26.7]
>>> data[-1]
26.7
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> data = []
>>> data.append('hi')
>>> data
['hi']
>>> data.append('hello')
>>> data
['hi', 'hello']
>>> import time
>>> data = []
>>> for i in range(10):
	data.append(i)
	print(data)
	time.sleep(1)

	
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for i in range(10):
	data.pop()
	print(data)
	time.sleep(1)

	
9
[0, 1, 2, 3, 4, 5, 6, 7, 8]
8
[0, 1, 2, 3, 4, 5, 6, 7]
7
[0, 1, 2, 3, 4, 5, 6]
6
[0, 1, 2, 3, 4, 5]
5
[0, 1, 2, 3, 4]
4
[0, 1, 2, 3]
3
[0, 1, 2]
2
[0, 1]
1
[0]
0
[]
>>> data = [23,12,45,'mumbai','pune',10.5,12.6,100,101]
>>> 'pune' in data
True
>>> data.index('pune')
4
>>> data.insert(5,'noida')
>>> data
[23, 12, 45, 'mumbai', 'pune', 'noida', 10.5, 12.6, 100, 101]
>>> data.pop(3)
'mumbai'
>>> data.remove(10)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    data.remove(10)
ValueError: list.remove(x): x not in list
>>> data.remove(101)
>>> data
[23, 12, 45, 'pune', 'noida', 10.5, 12.6, 100]
>>> data_2 = [101,102,103,104]
>>> data.extend(data_2)
>>> data
[23, 12, 45, 'pune', 'noida', 10.5, 12.6, 100, 101, 102, 103, 104]
>>> data.count(12)
1
>>> data_2 = [10,2,13,10,103,110,115,111,102,154]
>>> sorted(data_2)
[2, 10, 10, 13, 102, 103, 110, 111, 115, 154]
>>> sorted(data_2, reverse = True)
[154, 115, 111, 110, 103, 102, 13, 10, 10, 2]
>>> 
