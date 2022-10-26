### What are Exceptions?
##### Definition: An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. An exception is a Python object that represents an error. 
##### There are standart 29 types of exceptions in python. Let`s take a look at some examples.
#### Example
```python
print(2/(2-2)))
```
#### Output:
```python
File "<stdin>", line 1
    print(2/(2-2)))
                  ^
SyntaxError: invalid syntax
```
##### In this example, we can observe a SyntaxError. It`s raised when there is an error in Python syntax.
#### Here is two more examples of exceptions.
-----------------------------
```python
print(2/(2-2))
```

```python
>>> print(2/(2-2))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```
----------------------------
```python
print('string'/25)
```

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```
--------------------------------------
##### You can read about these and other exceptions in this documentation  https://docs.python.org/3/tutorial/errors.html#syntax-errors
### What is Exceptions Handling?
##### Definition: Exception handling is the process of responding to unwanted or unexpected events when a computer program runs.
##### So what is exception handling for? Exception handling is needed so that when an error occurs when running the code, the program reacts to the error in any way you want.
#### Example
Need for exceptions

How can Exceptions be coded in Java?

API heirarchy for Exceptions

Types of Exceptions

Keywords in Exception API: try, catch, finally, throw, throws

Rules for coding Exceptions

Declaring Exceptions

Defining and Throwing Exceptions

Errors and Runtime Exceptions

Custom Exception

Assertions

What are Assertions?

Enabling and disabling assertions in development environment

## sources:
<sup><br/>
"Python - Exceptions Handling". 2022. https://www.tutorialspoint.com/index.htm
https://www.tutorialspoint.com/python/python_exceptions.htm#:~:text=An%20exception%20is%20an%20event,object%20that%20represents%20an%20error.
<br/>
"Programming - Functions ". 2022. Cs.Utah.Edu. 
https://www.cs.utah.edu/~germain/PPS/Topics/functions.html.
<br/>
"Python Function Arguments (Default, Keyword And Arbitrary)". 2022. Programiz.Com. 
https://www.programiz.com/python-programming/function-argument.