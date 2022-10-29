# TODO

0. Рассписать что такое ООП в целом, зачем оно и тд тп +
1. Рассписать что такое self +
2. Провести много аналогий из жизни ( добавить свои слова в пример , тд тп)
3. Полиморфизм, Абстракция, Инкапсуляция (примеры + теоритеческие определения) ?
4. Композиция, Агрегация !! Забыл +
4. Перечисления ?
5. Абстрактные классы/ Protocol +-
6. Интерфейсы (определение и конктретно в python что это такое) ?
7. Конструкторы(описать) +
8. Делегаты/События (пройдём) -
9. SOLID (пройдём лучше)11 +-
11. Mixins детально описать + крутые примеры -- ?
12. Магические методы все рассписать с примерами
13. getters/setters (Property) +

----

## На будущее

1. Design patterns (не учили, мб сегодня пройдём)
2. Метаклассы ( тоже не учили, они в 80% useless)
3. Enumeration
4. Dataclasses
5. __slots__
6. Дескрипторы

## Prioblems

1. Mixin
2. Перечесления
3. интерфейси
4. делегати

# OOP

_Object Oriented Programming is considered as a design
for building software. In OOP every logic is written to get
our work done, but represented in form of Objects._

_The basic goal of OOPs concepts with real time examples is to
connect data and the functions that operate on it so that no other
part of the code may access it except that function._

# Class

_Instead of writing a program, you create classes with OOP.
Data and functions are both contained in a class. You construct an object
, which is an instance of that class, when you want to save something in memory.
As an example, you can create a Customer class that contains customer-related data
and functions. You must then build a new Customer class object if you want
your program to generate a customer in memory._

_Consider the Automobile Class. There may be many automobiles with different
names and brands, but they will all have some basic characteristics, such as
four wheels, a speed limit, and a range of mileage. The class is Car, and the
attributes are wheels, speed limitations, and mileage._

### Objects

_Object is the basic unit of object-oriented programming.Objects are identified
by its unique name. An objectrepresents a particular instance of a class. There
can be more than one instance of an object. Each instance of an object can hold
its own relevant data._

### Defining a Class in Python

_Like function definitions begin with the def keyword in Python, class definitions begin with a class keyword._
_The first string inside the class is called docstring and has a brief description of the class. Although not mandatory,
this is highly recommended._

+ Example:

```python
class MyNewClass:
    '''This is a docstring. I have created a new class'''
    pass
```

_A class creates a local namespace where all its attributes are defined. Attributes may be data or functions._
_As soon as we define a class, a new class object is created with the same name. This class object allows to access
the different attributes as well as to instantiate new objects of that class._

+ one more Example☺
+ Example:

```python
class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# Output: 10
print(Person.age)

# Output: <function Person.greet>
print(Person.greet)

# Output: "This is a person class"
print(Person.__doc__)
```

### Creating an Object in Python

_the class object could be used to access different attributes._
_It can also be used to create new object instances (instantiation) of that class._

+ Example:

```python
harry = Person()
```

_This will create a new object instance named harry. We can access the attributes of objects using the object name
prefix._
_This means to say, since Person.greet is a function object (attribute of class), Person.greet will be a method object._

+ Example:

```python
class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# create a new object of Person class
harry = Person()

# Output: <function Person.greet>
print(Person.greet)

# Output: <bound method Person.greet of <__main__.Person object>>
print(harry.greet)

# Calling object's greet() method
# Output: Hello
harry.greet()
```

_Class functions that begin with double underscore __ are called special functions as they have special meaning._
_Of one particular interest is the __init__() function. This special function gets called whenever a new object of that
class is instantiated._
_This type of function is also called constructors in Object Oriented Programming (OOP). We normally use it to
initialize all the variables._

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

### Self

_self represents the instance of the class. By using the “self” we can access the attributes and methods of the class in
python. It binds the attributes with the given arguments._

### The Constructor \_\_init__

_The \__init_\_ method is at the core of OOP and is required to create objects._

_A constructor is a special method that the program calls upon an object’s creation. The constructor is used in the
class to initialize data members to the object._

+ Example:

```python
class Dog:


def __init__(self, dogBreed, dogEyeColor):
    self.breed = dogBreed
    self.eyeColor = dogEyeColor
```

# Abstract Classes

_An abstract class to create a blueprint for other classes._
_Similarly, an abstract method is an method without an implementation. An abstract class may or may not include abstract
methods._
_To define an abstract class, you use the abc (abstract base class) module._
_The abc module provides you with the infrastructure for defining abstract base classes._
_To define an abstract method, you use the @abstractmethod decorator_

_The Employee class represents an employee, either full-time or hourly_

+ Example:

```python
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_salary(self):
        pass
```

_The FulltimeEmployee class inherits from the Employee class. It’ll provide the implementation for the get_salary()
method._

+ Example:

```python
class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary
```

# "Polymorphism"

_Polymorphism is a very important idea in programming. It consists of using a single entity (method, operator, or
object) to represent different types in different use cases._

_There are two classes Human and Animal. They have a similar structure and have methods with the same names info() and
walk()._

+ Example:

```python
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Student. My name is {self.name}. I am {self.age} years old.")

    def walk(self):
        print("walking")


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def walk(self):
        print("walking")
```

### Polymorphism With Class Methods

```python
class Car():

    def wheels(self):
        print(4)

    def mode_of_transport(self):
        print("Private usually")


class Bus():

    def wheels(self):
        print(8)

    def mode_of_transport(self):
        print("Public usually")


obj_car = Car()

obj_bus = Bus()

for vehicle in (obj_car, obj_bus):
    vehicle.wheels()

    vehicle.mode_of_transport()
```

### Polymorphism With Inheritance

_a child class gets access to the protected and public methods
and variables of the parent class whenever it inherits it. We exploit
this concept to implement Polymorphism using Inheritance as well._

```python 
class Vehicle:

     def desc(self):
       print("So many categories of vehicle")

     def wheels(self):
       print("Differs according to the vehicle category")

class car(Vehicle):

     def wheels(self):
       print(4)

class bus(Vehicle):

     def wheel(self):
       print(8)

obj_vehicle = Vehicle()
obj_car = car()
obj_bus = bus()
obj_vehicle.desc()
obj_vehicle.wheels()
obj_car.desc()
obj_car.wheels()
obj_bus.desc()
obj_bus.wheels()
```

# Python Inheritance

_Inheritance allows us to define a class that inherits all the methods and properties from another class._

- Parent class is the class being inherited from, also called base class.
- Child class is the class that inherits from another class, also called derived class.

### Create a Parent Class

+ Example:

```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```

### Create a Child Class

_Python also has a super() function that will make the child class inherit all the methods and properties from its
parent:_

+ Example:

```python
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
```

### Polymorphism and Inheritance

_We can override some methods and attributes specifically to match the child class. Polymorphism allows us to have
access to these overridden methods and attributes that have the same name as in the parent class._

+ Example:

```python


class Human:
    def __init__(self, name):
        self.name = name

    def weight(self):
        pass

    def height(self):
        pass

    def __str__(self):
        return self.name


class Man(Human):
    def __init__(self, length, weight, height):
        super().__init__()
        self.weight = weight
        self.height = height

    def weight(self):
        return self.weight

    def height(self):
        return self.height

```

## Method Resolution Order

_MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy_

+ Example 1

```python
class A:
    def method(self):
        print("A.method() called")


class B:
    pass


class C(B, A):
    pass


c = C()
c.method()
```

_The MRO for this case is: C -> B -> A_

+ Example 2

```python
class A:
    def method(self):
        print("A.method() called")


class B:
    def method(self):
        print("B.method() called")


class C(A, B):
    pass


class D(C, B):
    pass


d = D()
d.method()
```

_The MRO for this case is: D -> C -> A -> B_

### Diamont problem

_The diamond problem occurs when two classes have a common parent class, and another class has both those classes as
base classes. Composition allows composite classes to reuse the implementation of the components it contains._

+ Example:

```python

class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass


obj = Class4()
obj.m()
# Class4->Class2->Class3->Class1
```

# Mixin

_We have one parent class ("Vehicle"), and two child classes ("Car","Airplane")_

```python
class Vehicle():
    def __init__(self, position):
        self.position = position

    def trevel(self, destinition):
        route = calculate_route(souce=self.position, to=destinition)

    def calculate_route(self, source, to):
        return 0

    def move_along(self, route):
        print("moving")


class Car(Vehicle):
    pass


class Airplane(Vehicle):
    pass

```

# Composition

_Composition is an object oriented design concept that models a has a relationship.
In composition, a class known as composite contains an object of another class known
to as component. In other words, a composite class has a component of another class._

+ Example:

``` python
class Component:
  
   # composite class constructor
    def __init__(self):
        print('Component class object created...')
  
    # composite class instance method
    def m1(self):
        print('Component class m1() method executed...')
  
  
class Composite:
  
    # composite class constructor
    def __init__(self):
  
        # creating object of component class
        self.obj1 = Component()
          
        print('Composite class object also created...')
  
     # composite class instance method
    def m2(self):
        
        print('Composite class m2() method executed...')
  
        # calling m1() method of component class
        self.obj1.m1()
  
  
# creating object of composite class
obj2 = Composite()
  
# calling m2() method of composite class
obj2.m2()
```

# Aggregation

_Aggregation is a concept in which an object of one class can
own or access another independent object of another class._

+ It is a unidirectional association i.e. a one-way relationship. For example, a department can have students but vice
  versa is not possible and thus unidirectional in nature.
+ In Aggregation, both the entries can survive individually which means ending one entity will not affect the other
  entity.
+ Example:

```python

# Code to demonstrate Aggregation

# Salary class with the public method 
# annual_salary()
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


# EmployeeOne class with public method
# total_sal()
class EmployeeOne:

    # Here the salary parameter reflects
    # upon the object of Salary class we
    # will pass as parameter later
    def __init__(self, name, age, sal):
        self.name = name
        self.age = age

        # initializing the sal parameter
        self.agg_salary = sal  # Aggregation

    def total_sal(self):
        return self.agg_salary.annual_salary()


# Here we are creating an object 
# of the Salary class
# in which we are passing the 
# required parameters
salary = Salary(10000, 1500)

# Now we are passing the same 
# salary object we created
# earlier as a parameter to 
# EmployeeOne class
emp = EmployeeOne('Geek', 25, salary)

print(emp.total_sal())
```

# Interface ???????????????

_Interfaces play an important role. As an application grows,
updates and changes to the code base become more difficult to
manage. More often than not, you wind up having classes that look
very similar but are unrelated, which can lead to some confusion._

_At a high level, an interface acts as a blueprint for designing classes. Like classes, interfaces define methods.
Unlike classes, these methods are abstract. An abstract method is one that the interface simply defines._

# Python - Magic Methods

# Добавить пример каждого магического метода

_Magic methods in Python are the special methods that start and end with the double underscores._
_For example, when you add two numbers using the + operator, internally, the __add__() method will be called._

```python
>> > dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__',
 '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__',
 '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__',
 '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__',
 '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__',
 '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__',
 '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__',
 '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__',
 '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate',
 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

```

+ Example: __new__()

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

+ Example: __add__(), __str__()

```python
class distance:
    def __init__(self, x=None, y=None):
        self.ft = x
        self.inch = y

    def __add__(self, x):
        temp = distance()
        temp.ft = self.ft + x.ft
        temp.inch = self.inch + x.inch
        if temp.inch >= 12:
            temp.ft += 1
            temp.inch -= 12
            return temp

    def __str__(self):
        return 'ft:' + str(self.ft) + ' in: ' + str(self.inch)
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
### Controlling Attribute Access
_Python accomplishes a great deal of encapsulation through "magic", instead of explicit modifiers for methods or fields._

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
# Encapsulation - Public, Protected, Private

## Public

_Public (generally methods declared in a class) are accessible from outside the class._

_*All members in a Python class are public by default. Any member can be accessed from outside the class environment._

+ Example:

```python
class Student:
    schoolName = 'XYZ School'  # public class attribute

    def __init__(self, name, age):
        self.name = name  # public instance attribute
        self.age = age  # public instance attribute
```

## Protected

_Protected members of a class are accessible from within the class and are also available to its sub-classes. No other
environment is permitted access to it._

# Показать что нельзя достучаться до protected извне класса

+ Example:

```python



class Student:
    _schoolName = 'XYZ School'  # protected class attribute

    def __init__(self, name, age):
        self._name = name  # protected instance attribute
        self._age = age  # protected instance attribute
```

## Private

_The double underscore __ prefixed to a variable makes it private. It gives a strong suggestion not to touch it from
outside the class. Any attempt to do so will result in an AttributeError:_

+ Example:

```python
class Student:
    __schoolName = 'XYZ School'  # private class attribute

    def __init__(self, name, age):
        self.__name = name  # private instance attribute
        self.__salary = age  # private instance attribute

    def __display(self):  # private method
        print('This is private method.')
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
```python
from datetime import date
 
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
 
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
 
 
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
 
print(person1.age)
print(person2.age)
 
# print the result
print(Person.isAdult(22))
```
# Getter and Setter

_In Python, getters and setters are not the same as those in other
object-oriented programming languages. Basically, the main purpose
of using getters and setters in object-oriented programs is to
ensure data encapsulation. Private variables in python are not
actually hidden fields like in other object oriented languages.
Getters and Setters in python are often used when:_

+ We use getters & setters to add validation logic around getting and setting a value.
+ To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external
  user.

_To achieve getters & setters property, if we define normal get() and set() methods it will not reflect any special
implementation. For Example_

+ Example:

```python

# Python program showing a use
# of get() and set() method in
# normal function

class Geek:
    def __init__(self, age=0):
        self._age = age

    # getter method
    def get_age(self):
        return self._age

    # setter method
    def set_age(self, x):
        self._age = x


Egor = Geek()

# setting the age using setter
Egor.set_age(21)

# retrieving age using getter
print(Egor.get_age())

print(Egor._age)
```

_Using property() function to achieve getters and setters behaviour_

_property() function in Python has four arguments property(fget, fset, fdel, doc),
get() is a function for retrieving an attribute value, set() is a function for setting
an attribute value, del() is a function for deleting an attribute value._

+ Example:

```python
class Geeks:
    def __init__(self):
        self._age = 0

    # function to get value of _age
    def get_age(self):
        print("getter method called")
        return self._age

    # function to set value of _age
    def set_age(self, a):
        print("setter method called")
        self._age = a

    # function to delete _age attribute
    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)


mark = Geeks()

mark.age = 10

print(mark.age)
```

# SOLID

|     |                                 |
|-----|---------------------------------|
| S   | single responsibility principle |
| O   | open-closed principle           |         
| L   | Liskov substitution principle   |       
| I   | interface segregation principle|       
| D   | dependency inversion principle |   

## Single Responsibility Principle

_"A class should have one, and only one, reason to change."_

_The single responsibility principle (SRP) states that every class,
method, and function should have only one job or one reason to change._

+ Example:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')


if __name__ == '__main__':
    p = Person('John Doe')

    db = PersonDB()
    db.save(p)
```

+ The Person class is responsible for managing the person’s properties.
+ The PersonDB class is responsible for storing the person in the database.

## Open Closed Principle

_In practice we often see that modules are changed when new behavior is
required, which violates the OCP. We want to have fixed behavior but still be
flexible. :confused: Let’s see how these oppositions can work hand in hand._

+ Example:

```python
class soldier:
    def attack(self, weapon: str) -> None:
        if weapon == "gun":
            print("The soldier is shooting.")
        elif weapon == "grenade":
            print("The a soldier throws a grenade.")
        else:
            raise ValueError(f"The soldier doesn't have a {weapon}")
```

_This example breaks the OCP because when we want the soldier to
wield another weapon, we would have to change the attack method.
A better approach would be to create a function for each weapon
that is passed to and called by the attack method._

+ Example:

```python
class soldier:
    def attack(self, weapon) -> None:
        weapon()


def gun():
    print("The soldier shoots.")


def grenade():
    print("The a soldier throws a grenade.")


alfa = soldier()
alfa.attack(gun)
```

## Liskov substitution principle

_The Liskov substitution principle states that a child class must be
substitutable for its parent class. Liskov substitution principle aims
to ensure that the child class can assume the place of its parent class
without causing any errors._

# прикладу не має, думайте самі

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

## interface segregation principle

_“Clients should not be forced to depend upon interfaces that they do not use.”_

_The principle of interface separation is to reduce side effects
and the frequency of necessary changes by dividing the software
into several independent parts._

_First, define a Vehicle abstract class that has two abstract methods, go() and fly():_

+ Example:

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass

```

_Second, the Aircraft class that inherits from
the Vehicle class and implement both go() and fly() methods:_

+ Example:

```python
class Aircraft(Vehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")
```

_Third, the Car class that inherits from the Vehicle class. But a car cannot fly, we raise an exception in the fly()
method:_

+ Example:

```python
class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise Exception('The car cannot fly')
```

_To fix this, you need to split the Vehicle class into small ones and inherits from these classes from the Aircraft and
Car classes:_

+ Example:

```python
from abc import ABC, abstractmethod


# split the Vehicle interface into two smaller interfaces: Movable and Flyable
class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass


# inherits from the Flyable class from the Aircraft class
class Aircraft(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")


# inherit the Movable class from the Car class:
class Car(Movable):
    def go(self):
        print("Going")
```

## Dependency Inversion Principle

+ High-level modules should not depend on low-level modules.
+ Both should depend on abstractions (e.g. interfaces).

_if a component needs to be able to switch specific
implentations (details), it should not have a source code dependency
to those implementations._

# ПРИКЛАД!!!!!!!!!!!!!!!!!