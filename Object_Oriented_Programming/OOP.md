
# TODO
0. Рассписать что такое ООП в целом, зачем оно и тд тп
1. Рассписать что такое self
2. Провести много аналогий из жизни ( добавить свои слова в пример , тд тп)
3. Полиморфизм, Абстракция, Инкапсуляция (примеры + теоритеческие определения)
4. Композиция, Агрегация !! Забыл
4. Перечисления
5. Абстрактные классы/ Protocol
6. Интерфейсы (определение и конктретно в python что это такое)
7. Конструкторы(описать)
8. Делегаты/События (пройдём)
9. SOLID (пройдём лучше)11
11. Mixins детально описать + крутые примеры
12. Магические методы все рассписать с примерами
13. getters/setters (Property)

----
## На будущее
1. Design patterns (не учили, мб сегодня пройдём)
2. Метаклассы ( тоже не учили, они в 80% useless)
3. Enumeration
4. Dataclasses
5. __slots__ 
6. Дескрипторы

# Class

### Defining a Class in Python

_Like function definitions begin with the def keyword in Python, class definitions begin with a class keyword._
_The first string inside the class is called docstring and has a brief description of the class. Although not mandatory,
this is highly recommended._

```python
class MyNewClass:
    '''This is a docstring. I have created a new class'''
    pass
```

_A class creates a local namespace where all its attributes are defined. Attributes may be data or functions._
_As soon as we define a class, a new class object is created with the same name. This class object allows to access
the different attributes as well as to instantiate new objects of that class._

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

```python
harry = Person()
```

_This will create a new object instance named harry. We can access the attributes of objects using the object name
prefix._
_This means to say, since Person.greet is a function object (attribute of class), Person.greet will be a method object._

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

# Abstract Classes

_An abstract class to create a blueprint for other classes._
_Similarly, an abstract method is an method without an implementation. An abstract class may or may not include abstract
methods._
_To define an abstract class, you use the abc (abstract base class) module._
_The abc module provides you with the infrastructure for defining abstract base classes._
_To define an abstract method, you use the @abstractmethod decorator_

_The Employee class represents an employee, either full-time or hourly_

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

# Плохой пример полиморфизма, добавить ещё, рассписать концепцию, показать полиморфизм в функциях (отдельно от классов)

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

# Python Inheritance

_Inheritance allows us to define a class that inherits all the methods and properties from another class._

- Parent class is the class being inherited from, also called base class.
- Child class is the class that inherits from another class, also called derived class.

### Create a Parent Class

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

```python
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
```

### Polymorphism and Inheritance

_We can override some methods and attributes specifically to match the child class. Polymorphism allows us to have
access to these overridden methods and attributes that have the same name as in the parent class._

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
base classes._

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
https: // www.tutorialsteacher.com / python / magic - methods - in -python
```

# Python - Public, Protected, Private

## Public

_Public (generally methods declared in a class) are accessible from outside the class._

_*All members in a Python class are public by default. Any member can be accessed from outside the class environment._

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

```python

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

```python
class my_class:
    @classmethod


deffunction_name(cls, arguments):
# Function Body
return value
```

_Syntax for Static Method._

```python
class my_class:
    @staticmethod

    deffunction_name(arguments):
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

```python
class Aircraft(Vehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")
```

_Third, the Car class that inherits from the Vehicle class. But a car cannot fly, we raise an exception in the fly()
method:_

```python
class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise Exception('The car cannot fly')
```

_To fix this, you need to split the Vehicle class into small ones and inherits from these classes from the Aircraft and
Car classes:_

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