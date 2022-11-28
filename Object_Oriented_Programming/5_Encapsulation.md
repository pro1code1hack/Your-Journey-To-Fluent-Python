# Encapsulation

_Encapsulation is a technique for combining the code acting on the data (methods)
and the data itself (variables) into a single entity. Encapsulation means that a class's
variables are kept private from other classes and are only accessible through its own methods._

# Public, Protected, Private

### Public

_Public (generally methods declared in a class) are accessible from outside the class._

_*All members in a Python class are public by default. Any member can be accessed from outside the class environment._

+ Example:

```python
class Student:
    schoolName = 'School'  # public class attribute

    def __init__(self, name, age):
        self.name = name  # public instance attribute
        self.age = age  # public instance attribute
```

### Protected

_A class's protected members can be accessed from inside the class and by its subclasses as well. Access to any other
environment is not allowed._

# Показать что нельзя достучаться до protected извне класса

+ Example:

```python

class Student:
    _schoolName = 'Hogwarts'  # protected class attribute

    def __init__(self, name, age):
        self._name = name  # protected instance attribute
        self._age = age  # protected instance attribute


exp1 = Student("Tony", 19)
exp1._schoolName


class a(Student):
    def __init__(self, name, age):
        super().__init__(name, age)


x = Student("Oleg", 11)
x._schoolName
```

### Private

_The double underscore __ prefixed to a variable makes it private. It gives a strong suggestion not to touch it from
outside the class. Any attempt to do so will result in an AttributeError:_

+ Example:

```python
class Student:
    __schoolName = 'Hogwarts'  # protected class attribute

    def __init__(self, name, age):
        self._name = name  # protected instance attribute
        self._age = age  # protected instance attribute


exp1 = Student("Tony", 19)
exp1._


class a(Student):
    def __init__(self, name, age):
        super().__init__(name, age)


x = Student("Oleg", 11)
x.__schoolName  # <----- EROR!!!!
```

# Getter and Setter Methods without Decorators

### Getter and Setter

_In object-oriented programming (OOPS), the methods known as getters are used to access
a class's private attributes. The Python getattr() function is equivalent to the setattr() function.
It changes the values of an object's attributes._

_In object-oriented programming (OOPS), the methods known as getters are used to access a class's secret
attributes. The Python getattr() method is equivalent to the setattr() function. It changes the values of
an object's attributes._

+ Example:

```python

class Example:
    def __init__(self, age=0):
        self._age = age

    # using the getter method   
    def get_age(self):
        return self._age
        # using the setter method   

    def set_age(self, a):
        self._age = a


Tony = Example()

# using the setter function  
Tony.set_age(19)

# using the getter function  
print(Tony.get_age())

print(Tony._age)

```

# Property

_The Python property() method has a built-in decorator called @property. When defining properties in a class,
it is used to grant "special" capability to specific methods so they can act as getters, setters, or deleters._

+ Example:

```python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_kelvins(self):
        return self.temperature + 273, 15


# Create a new object
exl = Celsius()

# Set the temperature
exl.temperature = 37

# Get the temperature attribute
print(exl.temperature)

# Get the to_kelvins method
print(exl.to_kelvins())
```

_The built-in Python function property() generates and returns a property object. This function's syntax is as follows:_

```python
property(fget=None, fset=None, fdel=None, doc=None)
```

+ fget is a function that retrieves an attribute's value.
+ fset is a function that sets an attribute's value.
+ fdel is capable of deleting the attribute.
+ doc is the string (like a comment)

_Even the terms get temperature and set temperature cannot be defined since they are superfluous and contaminate the
class namespace._

_For this, while defining our getter and setter methods, we reuse the temperature name. Let's see how a decorator may
put this into practice:_

+ Example:

```python
# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_kelvins(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
exl = Celsius(37)

print(exl.temperature)

print(exl.to_kelvins())

coldest_thing = Celsius(-300)
```

# problems :  Name Mangling ?????
