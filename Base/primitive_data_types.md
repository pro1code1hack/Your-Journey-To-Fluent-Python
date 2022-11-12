# Python primitive data types
``` 
In Python we have:
1.Integer(int)
2.Float
3.String(str)
4.Boolean Type(bool)
```
## Integers
An integer is a whole number with no decimal places. For example, 1 is an integer, but 1.0 isn’t.
The name for the integer data type is int, which you can see with type():
```python
x = 10
print(type(x))
# <class 'int'>
```
## Float
A floating-point number, or float for short, is a number with a decimal place.
1.0 is a floating-point number, as is -2.75. 
The name of the floating-point data type is float:
```python
x = 12.5
print(type(x))
# <class 'float'>
```
## Strings
Besides numbers, Python can also manipulate strings, which can be expressed in several ways.
They can be enclosed in **single quotes** ('...') or **double quotes** ("...")
with the same result, \ can be used to escape quotes:
```python
print('Hi world')       # Hi world
print("Hi world")       # Hi world
print(type("Hi world"))      # <class 'str'>
```
#### Accessing characters in Python String:
Like many other popular programming languages, strings in Python are arrays of bytes
representing unicode characters. However, Python does not have a character data type,
a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
```python
s  = "Hello Python"
print(s[0])     # H
print(s[4])     # o
print(s[-1])    # n 
print(s[:5])    # Hello
print(s[6:])    # Python
print(s[::-1])  # nohtyP olleH
```
##### String length:
To get the length of a string, use the `len()` function.
```python
a = "Hello world"
print(len(a))       # 11
```
##### String Concatenation:
Strings, like numbers, can be added. 
The operation of adding strings is called concatenation or concatenation.
```python
s_1 = "Python is "
s_2 = "high-level "
s_3 = "programming language"
print(s_1 + s_2 + s_3 + "!!!")   # Python is high-level programming language!!!
```
## Boolean Type
Python boolean type is one of the built-in data types provided by Python, which represents one of the two values i.e. 
True or False. Generally, it is used to represent the truth values of the expressions. For example, 1==1 is True whereas 2<1 is False.
```python
a = True
b = False
print(type(a))      # <class 'bool'> 
print(type(b))      # <class 'bool'>
```
#### Method `bool()` 
```python
x = 5
y = 10
print(bool(x > y))      # False
a = 10
b = 5
print(bool(a > b))       # True
```