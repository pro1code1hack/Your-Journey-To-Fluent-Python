# Python Functions

_An area of code called a function carries out a particular duty._

_Let's say you need to write a program to calculate the graph and display it. Two functions can be developed to address
this issue:_

+ create a calculat function
+ create a display function
  _Our program is simple to comprehend and reuse because it breaks a difficult problem down into smaller components._

## Types of function

_In Python programming, functions come in two varieties:_

+ **Standard library functions** are accessible for usage in Python and are included in the language.
+ **User-defined functions** - We are able to design our own functions in accordance with our needs.

## Declaration of a Python function

_The syntax for a function declaration is:_

+ Example:

```python
def function(arg):
    #  body 

    return
```

_Definitions_

+ **def** - is a function declaration keyword
+ **function** - is the function's given name
+ **arguments** - any information supplied to the function
+ **return** - Returns the value of a function
+ Example:

```python
def say_hello():
    print('Hello World!')
```

## Calling a Function in Python

_In the above example, a function called say_hello() has been declared._

_We must now call this method in order to use it._

+ Example:

```python
def say_hello():
    print('Hello World!')


# call the function
say_hello()
```

+ Output:

```
Hello World!
```

_How it works:_

+ The program's control is transferred to the function definition when the function is called.
+ All code inside the function is run.
+ Following the function call, the program's control moves on to the following statement.

## Arguments in Python Function

_Arguments may also be passed to a function. A function's acceptance of a value is known as an argument._

+ Example:

```python
# function with two arguments
def info(first_name, surname):
    name = first_name + ' ' + surname
    print('Name: ', name)


# function call with two values
info('Yehor', 'Dremliuha')
```

_Here, info('Yehor','Dremliuha') specifies that the values Yehor and Dremliuha will be assigned to the parameters
first_name and surname, respectively._

## Return in Python

_A value can or cannot be returned by a Python function. The return statement is used if we want our function to return
a value to a function call._

+ Example:

```python
def info(first_name, surname):
    ...
    return name
```

_Here, we are returning the variable name._

## Python Function Arguments

_Deep analysis of arguments_

### Python Function Arguments

+ Example:

```python
def info(first_name, surname):
    ...
    return name
```

_The function info() in the example above requires the inputs first_name and surname._

### Argument for a Function with Default Values

_In Python, function arguments can have default values. In order to offer default values, we employ the **=** operator._

+ Example:

```python
def info(first_name='Yehor', surname='Dremliuha'):
    name = first_name + ' ' + surname
    return name
```

### Keyword Argument in Python

_Arguments in keyword arguments are assigned according to their names._

+ Example:

```python
def info(first_name, surname):
    ...
    return name


info(first_name='Yehor', surname='Dremliuha')
```

_In these cases, the positions of arguments are worthless._

### Using Arbitrary Parameters in Python

_You can send multiple arguments or keyword arguments to a function using *args and **kwargs._

#### Python Function Definitions Using the args Variable

_To send a variable number of arguments to a function in Python, use the special syntax *args in the function
specification. It is used to pass a variable-length, keyword-free argument list._

+ By convention, the sign * is frequently used with the word args in the syntax for taking in a variable number of
  arguments.
+ You can accept additional arguments using *args than the number of formal arguments you previously declared.
+ Example:

```python
def example(*argv):
    for arg in argv:
        print(arg)


example('Senior', 'Python', 'Developer', 'Roadmap')
```

```
Senior
Python
Developer
Roadmap
```

#### Python Function Definitions Using the kwargs Variable

_Python function definitions can send a keyworded, variable-length argument list by using the unique syntax **kwargs.
With the double star, we use the name kwargs._

+ A keyword argument is used to give the variable a name before passing it to the function.
+ The kwargs may be viewed as a dictionary that associates each term with the value that is passed along with it.

+ Example:

```python
def example(**kwargs):
    for key, value in kwargs.items():
        print("%s = %s" % (key, value))


myFun(first='Senior', second='Python', third='Developer', fourth='Roadmap')
```

```
first = Senior
second = Python
third = Developer
fourth = Developer
```

#### The use of *args and **kwargs in a function call

_We use of *args and **kwargs in a function call_

+ Example:

```python
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


myFun('Yehor', 'Dremliuha', first='Senior', second='Python', third='Developer', fourth='Roadmap')
```

_where first='Senior', second='Python', third='Developer', fourth='Roadmap' are supplied as **kwargs and printed
on the same line, and 'Yehor','Dremliuha' are passed as *args._

```
args: ('Yehor', 'Dremliuha')
kwargs: {'first': 'Senior', 'second': 'Python', 'third': 'Developer', 'fourth': 'Roadmap'}
```

## Higher Order Functions in Python

_When a function operates on another function, it is referred to as a higher order function. This might happen when the
function takes another function as an input or returns another function as an output. Knowing that this higher order
function applies to methods and functions that accept functions as a parameter or return functions as a result is
important. Higher order function notions are supported by Python as well._

_Higher-order function properties:_

+ The function can be kept in a variable.
+ The function can be used as a parameter in another function.
+ From a function, you may return the function.
+ You can be kept in data structures like lists, hash tables,...
+ Example:

```python
def isup(text):
    return text.isupper()


print(isup('HELLO'))

>> > True
```

### Function being passed as a parameter to another function

_Python defines functions as objects, therefore it is possible to send them as arguments to other functions._

+ Example:

```python
def isup(text):
    return text.isupper()


def check_text(func):
    checking = func("HELLO")
    print(checking)


check_text(isup)

>> > True
```

## Decorators

_In Python, decorators are the most typical application of higher-order functions. It enables programmers to change a
function's or a class's behavior. Decorators enable us to extend the behavior of a wrapped function without permanently
changing it by wrapping another function in them. Functions are called inside the wrapper function when using
decorators, where they are sent as arguments into another function._

+ Example:

```python
def decorator(func):  # func = print_hello
    def wrapper(*args, **kwargs):
        print("before it was only hello")
        func(*args, **kwargs)
        print("after it ")
        func(*args, **kwargs)
        print("world")

    return wrapper


@decorator
def print_hello(*args, **kwargs):
    print("hello")
    print(args)
    print(kwargs)


print_hello()
```

+ Example:

```python
# defining a decorator 
def hello_decorator(func):
    def wrapper():
        print("Hello, this is before function execution")

        func()

        print("This is after function execution")

    return wrapper


@hello_decorator
def function_to_be_used():
    print("This is inside the function !!")

```

## Lambda Functions

_A lambda function in Python is a unique class of function that doesn't have a function name._

### Declaring a lambda function in Python

_To build a lambda function, we substitute the lambda keyword for the def keyword._

```
lambda argument(s) : expression 
```

+ **argument(s)** - whatever argument was supplied to the lambda function
+ **expression** - expression is carried out and given back
+ Example:

```python
say_hello = lambda: print('Hello')
# call the lambda
say_hello()
```

### Python lambda Function with an Argument

# lambda that accepts one argument

+ Example:

```python
hello_to_user = lambda name: print('Hello,', name)

# lambda call
hello_to_user('Yehor')
```

_The hello_to_user variable in the example above has a lambda function attached to it._

_Here, name after the lambda keyword specifies that the lambda function accepts the argument named name._

## Function Composition in Python

_The process of combining two or more functions so that the result of one function becomes the input of the next
function and so on is known as function composition._

+ Example:

```python
def add(name):
    return x + 3


def multiply(x):
    return x * 5


# Adding 3 to 5 and multiplying the result with 5
print(multiply(add(10))) 
```

## Memoization in Python

_Memorization is a technique for storing the outcomes of earlier function calls to expedite subsequent computations.
Repeated function calls with the same inputs allow us to save the prior values rather than doing pointless calculations
again. Calculations are significantly accelerated as a consequence._

## Currying in Python

_Currying is a functional design pattern that is typically used to convert multiple-argument functions into a chain
of functions that only accept one parameter apiece._

_Have a look at the following function, which multiplies the supplied inputs._

+ Example:

```python
def mult(x, y, z):
    return x * y * z


result = mult(2, 5, 7)
print(result)
```

_Binding the different parameters together is the first stage in the currying process. Assume a function with n
arguments that needs all of them bound. To do this, we fix the function with the first argument and build a new function
that takes (n - 1) arguments. Up till the function only accepts one argument, we now keep on constructing more
functions._

_We employ the Python language's built-in partial function from functools._

+ Example:

```python
from functools import partial

mult2 = partial(mult, 2)
mult2_5 = partial(mult2, 5)
print(mult2_5(7))
```

### Currying using Decorator

_Using the decorator will make currying much more effective. A decorator enhances a function's performance by
enclosing it in code or functionality._

_Curry is a useful design principle. Curry's main goal is to turn a given function into a series of binding functions,
which simplifies developers' tasks and improves the readability of the solution._

## Partial Functions in Python

_We may fix a particular amount of parameters in a function and create a new function using partial functions._

+ Example:

```python
from functools import partial


# A normal function
def funk(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x


# A partial function that calls f with
# a as 3, b as 1 and c as 4.
ex = partial(funk, 1, 2, 3)

# Calling g()
print(ex(4))

>> > 1234
```

+ Example:

```python
def sum(a, b):
    print("First", a + b)


def sum(a, b, c):
    print("Second", a + b + c)


sum(1, 2, 32)  # correct 
sum(14, 2)  # error
```

_We can see from the program above that the second sum technique takes precedence over the first sum method.he function
returns the output when we call it with three arguments, but an error is returned when we call it with with two
arguments. Hence, function overloading is not supported by Python._

## Function annotations

_Function annotations are arbitrary Python expressions connected to different functions' components. These expressions
don't exist in the runtime environment of Python since they are only evaluated at build time._

### Purpose of function annotations:

+ To keep track of the type change occuring in the function, information about the type of the function's parameters and
  return type should be provided.

```
def foo(a:”int”, b:”float”=5.0)  -> ”int”
```

_Observations for basic parameters: The word ":" is followed by the name of the argument, which is then the expression.
Here is the syntax for annotations._

_Return type annotations: Return type annotations differ somewhat from function argument annotations. Expression comes
after the '->' and is then followed by the letter ':'. The return type annotation syntax is displayed below._

+ Libraries can make better compile-time help messages on the functionality of different methods, classes, and modules
  by using string-based annotations.

## Recursion in Python

_In order to prevent names declared within a function from colliding with those defined elsewhere, the Python
interpreter constructs a new local namespace when you call a function. Because the objects have different names and
live in different namespaces, one function can call another even if they declare the identical objects._

+ Example:

```python
def func():
    title = 'Senior Python Developer Roadmap'
    func()
```

_Python establishes a namespace and gives x the value 10 in that namespace when func() is called for the first time.
Then func() repeatedly calls itself. The interpreter establishes a second namespace and also assigns 'Senior Python
Developer Roadmap' to x there
when func() is called a second time. Because they are in different namespaces, these two instances of the name 'title'
are
distinct from one another and can coexist without interfering._

_The way funk() is now built, it might theoretically call itself endlessly without any calls ever returning.
In reality, nothing actually lasts forever. There is a limited amount of memory on your computer, and soon it would run
out._

_Python prevents that from happening. When a function calls itself recursively more than the allotted number of times,
the interpreter raises an exception known as RecursionError._

## Designing Functions

_We have so far talked about the formal characteristics of functions and how to use them. We will now discuss what
constitutes a good function. Essentially, all of the characteristics of good functions serve to confirm that they are
abstractions._

+ One position should be assigned to each function. It should be possible to describe the work in a single line of text
  and identify it by a brief name. Functions that carry out several tasks sequentially should be broken up into separate
  functions.
+ One of the fundamental principles of software engineering is to avoid repetition. According to the so-called DRY
  principle, many code snippets shouldn't represent redundant logic. Instead, the reasoning ought to be used just once,
  given a name, and then applied numerous times. An opportunity for functional abstraction has undoubtedly been
  uncovered
  if you frequently find yourself copying and pasting blocks of code.

### Documentation

_A docstring, often known as documentation, is frequently included in a function definition and must be indented
#alongside the function body. Docstrings are often quoted using three quotes. The function's job is briefly described
in the first line. The lines that follow can explain arguments and make the behavior of the function clearer:_

+ Example:

```python
def funk(a, b):
    """infornation about function

    a -- width of the rectangle
    t -- length of the rectangle
    """

    square = a * b
    return square
```

_**Comments**. Python allows comments to be appended to the end of lines after the # sign._

_These remarks are never included in the help for Python, and the interpreter ignores them. They are only there for
human use._