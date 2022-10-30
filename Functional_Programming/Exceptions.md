## What are Exceptions?
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
##### You can read about these and other exceptions in link below
##### https://www.tutorialspoint.com/python/standard_exceptions.htm
## What is Exceptions Handling?
##### Definition: Exception handling is the process of responding to unwanted or unexpected events when a computer program runs.
##### So what is exception handling for? Exception handling is needed so that when an error occurs when running the code, the program reacts to the error in any way you want.
## Types of exceptions Handling
#### 1. Raising an Exception
##### The raising instruction is supposed to raise the specified exception. If no exceptions are found in the observable scope, then a RuntimeError exception is thrown at the place where the promotion is specified, without specifying, indicating that this is an error.
#### Example
```python
x = int(input())
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
```
```python
10
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
Exception: x should not exceed 5. The value of x was: 10
```
#### 2. The AssertionError Exception
##### Instead of waiting for a program to crash midway, you can also start by making an assertion in Python. We assert that a certain condition is met. If this condition turns out to be True, then that is excellent! The program can continue. If the condition turns out to be False, you can have the program throw an AssertionError exception.
#### Example
```python
import sys
assert ('MacOS' in sys.platform), "This code runs on Linux only."
```
```python
Traceback (most recent call last):
  File "<stdin>>", line 2, in <module>
    assert ('MacOS' in sys.platform), "This code runs on Linux only."
AssertionError: This code runs on Linux only.
```
#### 3. The try and except Block: Handling Exceptions
##### The try and except block in Python is used to catch and handle exceptions. Python executes code following the try statement as a “normal” part of the program. The code that follows the except statement is the program’s response to any exceptions in the preceding try clause.
<img src="..//Images/ExceptionsTryExcept.png" alt="Alt text">

##### As you saw earlier, when syntactically correct code runs into an error, Python will throw an exception error. This exception error will crash the program if it is unhandled. The except clause determines how your program responds to exceptions.
#### Example 
```python
def f(x, y):
    return x / y
FirstNum = int(input('x: '))
SecondNum = int(input('y: '))
try:
    f(FirstNum, SecondNum)
except ZeroDivisionError:
    print("You can`t divide by zero")
```
```python
x: 2
y: 0
You can`t divide by zero
```
#### Example 
```python
def f(x, y):
    return x / y


FirstNum = int(input('x: '))
SecondNum = int(input('y: '))
try:
    f(FirstNum, SecondNum)
except ZeroDivisionError as error:
    print(error)
else:
    print(f'Your result is {f(FirstNum, SecondNum)}')
```
```python
x: 2
y: 5
Your result is 0.4
```
#### Example 
```python
def f(x, y):
    return x / y


FirstNum = int(input('x: '))
SecondNum = int(input('y: '))
try:
    f(FirstNum, SecondNum)
except ZeroDivisionError as error:
    print(error)
else:
    print(f'Your result is {f(FirstNum, SecondNum)}')
finally:
    print('This row will be here anyway')
```
```python
x: 2
y: 0
division by zero
This row will be here anyway
```
```python
x: 2
y: 6
Your result is 0.3333333333333333
This row will be here anyway
```
## Exception hierarhy
##### An important thing to know is that exceptions, like everything else in Python, are just objects. They follow an inheritance hierarchy, just like classes do. For example, the ZeroDivisionError is a subclass of ArithmeticError, which is a subclass of Exception, itself a subclass of BaseException.
UWU
##### So, if you wanted to catch a divide-by-zero error, you could use except ZeroDivisionError. But you could also use except ArithmeticError, which would catch not only ZeroDivisionEror, but also OverflowError and FloatingPointError. Here`s short hierarchy of exceptions
- BaseException
- - Exception
- - - ArithmeticError
- - - - FloatingPointError
- - - - OverflowError
- - - - ZeroDivisionError
- - - AssertionError

##### A full chart of the hierarchy for built-in exceptions can be found at the bottom of the (Python documentation)[https://docs.python.org/3/library/exceptions.html#exception-hierarchy].

## Good tone

### Don't catch the exception
##### It's bad form to catch the generic Exception class. This will catch all types of exceptions that are subclasses of the Exception class, which is pretty much all of them. You may have bugs that you don't care about and don't affect how your program works, or maybe you're dealing with an untrusted API and want to swallow the bugs and try again. By catching an Exception, you run the risk of encountering an unexpected exception that your program can't actually recover from, or worse, swallowing an important exception without properly logging it - a huge headache when trying to debug programs that strangely fail. 

### Definitely don't catch BaseException
##### Catching a BaseException is a really bad idea because you will swallow all types of exceptions, including KeyboardInterrupt, the exception that causes your program to terminate when SIGINT (Ctrl-C) is sent. Do not do that.


## Sources:

##### "Python - Exceptions Handling". 2022. https://www.tutorialspoint.com/index.htm
##### https://www.tutorialspoint.com/python/python_exceptions.htm#:~:text=An%20exception%20is%20an%20event,object%20that%20represents%20an%20error.

##### "Python Exceptions: An Introduction ". https://realpython.com/ 
##### https://realpython.com/python-exceptions/

##### "Learn Python".https://www.learnpython.dev/ 
##### https://www.learnpython.dev/03-intermediate-python/40-exceptions/10-all-about-exceptions/
<img src="..//Images/ExceptionsHandlingGirl.png" alt="Alt text">