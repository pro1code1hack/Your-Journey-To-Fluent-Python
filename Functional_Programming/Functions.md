# Functions

Functions are "self-contained" modules of code that accomplish a specific 
task.
## Syntax
```python
def example():
    print("Hello world")
```
To declare a function you have to start by writing `def` keyword, after 
that goes the name of a function. After the name go two round brackets 
where you can write arguments, but it is optional. And, lastly, `:` 
identifies the end of function header.
```python
def example():
    print("Hello world")

example()
```
#### Output:
```python
Hello world
```
To call a function type its name and round brackets after it, after calling
the function, code inside it will be run.
### Important:
Name of a function must follow rules of writing identifiers.
## Arguments or parameters of functions
```python
def addition(a, b):
    print(a + b)

addition(3, 4)
```
#### Output:
```
7
```
Here function `addition()` has two parameters: a and b, since we called 
the function with two arguments it runs smoothly and gives the correct answer.
If we were to call the function mentioning only one argument, it would not work.
```python
addition(3)
```
It gives an error:
```
TypeError: addition() missing 1 required positional argument: 'b'
```
## Return
Let's extend our `addition()` function, so it saves sum of `a` and `b`.
```python
def addition(a, b):
    c = a + b
addition(3, 5)
print(c)
```
It looks like the code is absolutely correct and will print number 8,
but it will only give an error:
```
NameError: name 'c' is not defined
```
It doesn't work because variable `c` is local and can not be called from 
outside the function. To return value from the function to the main code use 
`return` keyword, it also exits from the function to the main code.
```python
def addition(a, b):
    c = a + b
    return c
print(addition(3, 5))
```
#### Output:
```python
8
```
### Important:

1.`return` can only return value to the main code, not variable, in the given 
example you still would not be able ta call `c`
<br/>
2.If you return multiple values at one moment, function will return tuple.
## sources:
<sup><br/>
"Python Functions (Def): Definition With Examples". 2022. Programiz.Com.
https://www.programiz.com/python-programming/function.
<br/>
"Programming - Functions ". 2022. Cs.Utah.Edu. 
https://www.cs.utah.edu/~germain/PPS/Topics/functions.html.
<br/>
"Python Function Arguments (Default, Keyword And Arbitrary)". 2022. Programiz.Com. 
https://www.programiz.com/python-programming/function-argument.