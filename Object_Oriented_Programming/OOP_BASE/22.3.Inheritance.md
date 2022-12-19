# Inheritance

_Inheritance is the capability of one class to derive or inherit the properties from another class._

+ It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add
  more features to a class without modifying it.

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

# Types of Inheritance in Python

### Single Inheritance

_In python single inheritance, a derived class is derived only from a single parent class and allows the class to derive
behaviour and properties from a single base class. This enables code re usability of a parent class, and adding new
features to a class makes code more readable, elegant and less redundant._

+ Example:

```python

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


x = Student("John", "Doe")
x.printname()

```

### Multiple Inheritance

_When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all
the features of the base case._

+ Example:

```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def studing(self):
        print(f"{self.fname} studing")


class Child(Student, Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


x = Child("John", "Doe")
x.printname()
x.studing()
```

### Multilevel Inheritance

_In python, Multilevel inheritance is one type of inheritance being used to inherit both base class and derived
class features to the newly derived class when we inherit a derived class from a base class and another derived
class from the previous derived class up to any extent of depth of classes in python is called multilevel inheritance._

+ Example:

```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def studing(self):
        print(f"{self.fname} studing")


class Child(Student):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


x = Child("John", "Doe")
x.printname()
x.studing()
```

### Hierarchical Inheritance

_Hierarchical Inheritance If multiple derived classes are created from the same base, this kind of Inheritance
is known as hierarchical inheritance. In this instance, we have two base classes as a parent (base) class as well
as two children (derived) classes._

+ Example:

```python
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")


# Derived class1


class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")


# Derivied class2


class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

```

### Hybrid Inheritance

_Hybrid Inheritance is a blend of more than one type of inheritance. The class is derived from the two classes
as in the multiple inheritance. However, one of the parent classes is not the base class. It is a derived class.
This feature enables the user to utilize the feature of inheritance at its best._

+ Example:

```python
class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")


class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")


class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")


# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")

```

# Method Resolution Order

_MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy_

+ Example 1:

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

+ Example 2:

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

### Diamont problem*

_The diamond problem occurs when two classes have a common parent class, and another class has both those classes as

base classes._

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
