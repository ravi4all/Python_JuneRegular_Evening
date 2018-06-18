Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 'hello world'
>>> type(s)
<class 'str'>
>>> len(s)
11
>>> s[0]
'h'
>>> s[5]
' '
>>> s[6]
'w'
>>> s[0:4]
'hell'
>>> s[0:5]
'hello'
>>> s[-1]
'd'
>>> s[0:]
'hello world'
>>> s[5:]
' world'
>>> s[:6]
'hello '
>>> s[:]
'hello world'
>>> s[0:9:2]
'hlowr'
>>> s[::-1]
'dlrow olleh'
>>> s[0] = 'c'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s[0] = 'c'
TypeError: 'str' object does not support item assignment
>>> 
