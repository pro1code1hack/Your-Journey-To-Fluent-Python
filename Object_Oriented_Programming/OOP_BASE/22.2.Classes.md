# What is a Python Class?

_A Python class is like an outline for creating a new object. An object is anything that you wish
to manipulate or change while working through the code. Every time a class object is instantiated,
which is when we declare a variable, a new object is initiated from scratch. Class objects can be used over and over
again whenever needed._

_A class is usually modeled after a Noun. Classes are things. So we might make a class that represents a Person, House,
Vehicle, or Animal. These are all common examples to use when learning about classes. For us, we will create a Vehicle
class.
What information would we associate with a vehicle, and what behavior would it have? A vehicle may have a type, brand,
model and so on.
This type of information is stored in python variables __called attributes__. These things also have behaviors. A
Vehicle can drive, stop,
honk its horn, and so on. Behaviors are contained in functions and a function that is part of a class is called a
method._

+ Example:

```python
class Vehicle:
 def __init__(self, brand, model, type):
  self.brand = brand
  self.model = model
  self.type = type
  self.gas_tank_size = 14
  self.fuel_level = 0

 def fuel_up(self):
  self.fuel_level = self.gas_tank_size
  print('Gas tank is now full.')

 def drive(self):
  print(f'The {self.model} is now driving.')

```

# Attributes

### Class Attributes

_Class attributes are attributes which are owned by the class itself. They will be shared by all the instances
of the class. Therefore they have the same value for every instance. We define class attributes outside all the methods,
usually they are placed at the top, right below the class header._

+ Example:

```python 
class A:
    a = "I am a class attribute!"
```

### Instance Attributes

_Instance Attributes are unique to each object, (an instance is another name for an object).
Here, any animal object we create will be able to store its name and age. We can change either attribute of either
animal,
without affecting any other animal objects we’ve created._

+ Example:

```python
class Animal:

 def __init__(self, name, age):
  self.name = name
  self.age = age
```

| Instance Attributes    | Class Attributes                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| an instance attribute defined inside the constructor. | a class attribute defined outside the constructor.                                                                                         |
| only accessible from the scope of an object.| accessible as both a property of the class and as a property of objects, as it is shared between all of them. |

# Methods

_Properties of the object are defined by the attributes and the behavior is defined using methods.
These methods are defined inside a class. These methods are the reusable piece of code that can be
invoked/called at any point in the program._

### Class constructor \_\_init__

_The properties that all Animals objects must have are defined in a method called
.__init__(). Every time a new Dog object is created, .__init__() sets the initial
state of the object by assigning the values of the object’s properties. That is,
.__init__() initializes each new instance of the class._

### Class constructor \_\_init__

_The properties that all Animals objects must have are defined in a method called
.__init__(). Every time a new Dog object is created, .__init__() sets the initial
state of the object by assigning the values of the object’s properties. That is,
.__init__() initializes each new instance of the class._

+ Example:

```python
class Animals:
 def __init__(self, name, age):
  self.name = name
  self.age = age
```

### \_\_new__ method !!!!!!!!!!!!!!!

_When you create an instance of a class, Python first calls the __new__() method to create the object and
then calls the __init__() method to initialize the object’s attributes._

_The __new__() is a static method of the object class. It has the following signature:_

+ Example:

```python
object.__new__(


class , * args, ** kwargs)
```

_The first argument of the __new__ method is the class of the new object that you want to create._

_The *args and **kwargs parameters must match the parameters of the __init__() of the class. However, the __new__()
method does use them._

+ Example:

```python
class Animal:
 def __new__(cls, name):
  print(f'Creating a new {cls.__name__} object...')
  obj = object.__new__(cls)
  return obj

 def __init__(self, name):
  print(f'Initializing the animal object...')
  self.name = name


cat = Animal('Jimmi')
```

### Instance methods

_Instance method are methods which require an object of its class to be created before it can be called.
To invoke a instance method, we have to create an Object of the class in which the method is defined._

+ Use the def keyword to define an instance method in Python.
+ Use self as the first parameter in the instance method when defining it. The self parameter refers to the current
  object.
+ Using the self parameter to access or modify the current object attributes.

+ Example:

```python
class Animal:
 # constructor
 def __init__(self, name, age):
  # Instance variable
  self.name = name
  self.age = age

 # instance method
 def show(self):
  print('Name:', self.name, 'Age:', self.age)


cat = Animal('Jimmi')
# call instance method
cat.show()
```

# Class method and static method in Python

_The class method in Python is a method, which is bound to the class but not the object of that class. The static
methods are also same but there are some basic differences. For class methods, we need to specify @classmethod
decorator, and for static method @staticmethod decorator is used._

_Syntax for Class Method:_

+ Example:

```python
class my_class:
 @classmethod
 def function_name(cls, arguments):
  # Function Body
  return value
```

_Syntax for Static Method._

+ Example:

```python
class my_class:
 @staticmethod
 def function_name(arguments):
  # Function Body
  return value
```

# Добавить в сравнение ещё методы с self, как-то красивее дописать

| Class Method                                                |                          Static Method                          |
|-------------------------------------------------------------|:-----------------------------------------------------------:|
| The class method takes cls (class) as first argument.                                            |                       The static method does not take any specific parameter.                       |
| Class method can access and modify the class state. | Static Method cannot access or modify the class state. |
| The class method takes the class as parameter to know about the state of that class. | Static methods do not know about class state. These methods are used to do some utility tasks by taking some parameters. |
| @classmethod decorator is used here. | @staticmethod decorator is used here. |

# Magic Methods

_Magic methods are special methods in python that have double underscores on both sides of the method name.
Magic methods are predominantly used for operator overloading. Operator overloading means provided additional
functionality to the operators, the python implicitly invokes the magic methods to provide additional
functionality to it_

+ \_\_add__ method
+

_the \_\_add__ method is a magic method which gets called when we add two numbers using the + operator. Consider the
following example_

+ Example:

```python
class ADD:
 def __init__(self, string_):
  self.string_ = string_

 def __add__(self, string2):
  return self.string_ + string2


ex = Str("Hello")
print(instance1 + " Folks")
```

+ \_\_str__() method

_\_\_str__(). It is overridden to return a printable string representation of any user defined class._

+ Example:

```python
class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age

 def __str__(self):
  return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)
```

+ \_\_getitem__ and \_\_setitem__ magic method

_\_\_getitem__ method is used to get an item from the invoked instances’ attribute. \_\_getitem__ is commonly used with
containers like list, tuple, etc._

+ Example:

```python
class A:
 def __init__(self, item):
  self.item = item

 def __getitem__(self, index):
  return self.item[index]


a = A([1, 2])
print(f"First item: {a[0]}")
print(f"Second item: {a[1]}")

```

+ Example:

```python
class Employee:
 def __new__(cls):
  print("__new__ magic method is called")
  inst = object.__new__(cls)
  return inst


def __init__(self):
 print("__init__ magic method is called")
 self.name = 'Satya'
```

_\__lt_\_, _\_gt_\_, _\_le_\_, _\_ge_\_, _\_eq_\_, and _\_ne_\_ magic methods_

_Comparative operators can be used to compare between the object’s attributes._

+ Example: __new__()

```python
class Comparison:
 def __init__(self, a):
  self.a = a

 def __lt__(self, object2):
  return self.a < object2.a

 def __gt__(self, object2):
  return self.a > object2.a

 def __le__(self, object2):
  return self.a <= object2.a

 def __ge__(self, object2):
  return self.a >= object2.a

 def __eq__(self, object2):
  return self.a == object2.a

 def __ne__(self, object2):
  return self.a != object2.a


a = Comparison(1)
b = Comparison(2)
print(
 a < b,
 a > b,
 a <= b,
 a >= b,
 a == b,
 a != b
)
```

| Operator Magic Methods          |  Description   |
|---------------------------------|-----|
| \__add__(self, other)           |To get called on add operation using + operator     |
| \__sub__(self, other)           |To get called on subtraction operation using - operator.     |
| \__mul__(self, other)           |To get called on multiplication operation using * operator.     |
| \__floordiv__(self, other)      |To get called on floor division operation using // operator.     |
| \__truediv__(self, other)       |    To get called on division operation using / operator.     |
| \__mod__(self, other)           |    To get called on modulo operation using % operator.     |
| \__pow__(self, other[, modulo]) |    To get called on calculating the power using ** operator.     |

### Type conversion magic methods

_Python also has an array of magic methods designed to implement behavior for built in type conversion functions like
float(). Here they are:_

```
__int__(self)
Implements type conversion to int.

__long__(self)
Implements type conversion to long.

__float__(self)
Implements type conversion to float.

__complex__(self)
Implements type conversion to complex.

__oct__(self)
Implements type conversion to octal.

__hex__(self)
Implements type conversion to hexadecimal.

__index__(self)
Implements type conversion to an int when the object is used in a slice expression. If you define a custom numeric type that might be used in slicing, you should define __index__.

__trunc__(self)
Called when math.trunc(self) is called. __trunc__ should return the value of `self truncated to an integral type (usually a long).

__coerce__(self, other)
Method to implement mixed mode arithmetic. __coerce__ should return None if type conversion is impossible. Otherwise, it should return a pair (2-tuple) of self and other, manipulated to have the same type.
```

_In the following example, you create a custom class Data and overwrite the __complex__()
magic method so that it returns a complex number (33+11j) when trying to call complex(x) on a custom Data object._

+ Example:

```python 
class Data:
    def __complex__(self):
        return (42+21j)
x = Data()
res = complex(x) 
print(res)
# (33+11j)
```

### Controlling Attribute Access

_Python accomplishes a great deal of encapsulation through "magic", instead of explicit modifiers for methods or
fields._

```
__getattr__(self, name)
You can define behavior for when a user attempts to access an attribute that doesn't exist (either at all or yet). This can be useful for catching and redirecting common misspellings, giving warnings about using deprecated attributes (you can still choose to compute and return that attribute, if you wish), or deftly handing an AttributeError. It only gets called when a nonexistent attribute is accessed, however, so it isn't a true encapsulation solution.

__setattr__(self, name, value)
Unlike __getattr__, __setattr__ is an encapsulation solution. It allows you to define behavior for assignment to an attribute regardless of whether or not that attribute exists, meaning you can define custom rules for any changes in the values of attributes. However, you have to be careful with how you use __setattr__, as the example at the end of the list will show.

__delattr__(self, name)
This is the exact same as __setattr__, but for deleting attributes instead of setting them. The same precautions need to be taken as with __setattr__ as well in order to prevent infinite recursi

Example:
def __setattr__(self, name, value):
    self.name = value
    # since every time an attribute is assigned, __setattr__() is called, this
    # is recursion.
```

+ Example:

```python
class Frob:
 def __init__(self, bamf):
  self.bamf = bamf

 def __getattr__(self, name):
  return 'Frob does not have `{}` attribute.'.format(str(name))


f = Frob("bamf")
f.bar
# 'Frob does not have `bar` attribute.'
f.bamf
# 'bamf'

```

# Destructor

_Destructors are called when an object gets destroyed. The __del__() method is a known as a destructor method
in Python. It is called when all references to the object have been deleted i.e when an object is garbage
collected._

+ Example:

```python
def __del__(self):
# body of destructor
```

+ Example:

```python
# Python program to illustrate destructor
class Employee:

 # Initializing
 def __init__(self):
  print('Employee created.')

 # Deleting (Calling destructor)
 def __del__(self):
  print('Destructor called, Employee deleted.')


obj = Employee()
del obj
```

