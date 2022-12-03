# Type Checking

_Python is a dynamic programming language with strong typing. Because it is dynamically typed and types are dynamically
inferred,
you may set variables' values without specifying the variable type, unlike in programming languages that are statically
typed, like Java._

+ Example:

```python
str_value = 'hello'

int_value = 123
```

### type()

_The Python function type() may be used to determine the kinds of the variables.
To find the precise variable types in the program during runtime debugging, utilize the type() function._

+ Example:

```python
str_value = 'hello'

int_value = 123

print(type(str_value))

print(type(int_value))
```

_The output of the code above is "int" and "str"  Since the variable's data type is an integer, "type()" may be used to
identify it._

### isinstance()

_Python's "insinstance("obj", "class")" function may be used to determine if an object is an instance of a class or not.
The boolean output value, which can only be True or False, is returned._

+ Example:

```python
str_value = 'hello'

int_value = 123

print(isinstance(str_value, str))

print(isinstance(int_value, int))
```

_The outcome of the code above is True. Since the variable's data type is a string, "isinstance()" may be used to
identify it._

_You can look at the instance as well. Say you wanted to determine whether a variable you have contains a numeric value
or not._

+ Example:

```python
class TriangleChecker:
    def __init__(self, first, second, third):
        if isinstance(first, (float, int)) and isinstance(second, (float, int)) and isinstance(third, (float, int)):
            self.first = first
            self.second = second
            self.third = third
            print("checked")
        else:
            print("Error")
```

### issubclass()

_If the student argument (first argument) is a subclass of the Human class, the issubclass() function determines whether
it is._

+ Example:

```python
class Human:
    def __init__(polygonType):
        print('Polygon is a ', polygonType)


class Student(Human):
    def __init__(self):


print(issubclass(Student, Human))
```

### Typing

_The good news is that type annotation was added to Python in version 3.5._

_Here is an illustration of a straightforward function, whose annotations declare the argument and return types:_

+ Example:

```python
def info(age: int) -> int:
    return 'I am' + age
```

_As seen in the example above, type annotation is achieved by following a variable with: <type>. By the way,
the return type should be None if the method does not return anything._

### Pydantic

_When working with data from external sources, such as the users of your program, static type checkers are useless.
type checkers can be useful in this situation. Pydantic is one of these tools, and it is used to verify data.
When the supplied data does not match a type declared with a type hint, validation issues are raised._

```
$ pip install pydantic
```

+ Example:

```python

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'Tad'
    friends: list[int] = []

```

_The annotation-only declaration informs Pydantic that the id field, which has the type int, is necessary.
If feasible, strings, bytes, or floats will be forced to become int_

_Name is not necessary because it has a default and is deduced as a string from the specified default._



