# Definition

_Polymorphism refers to having multiple forms. Polymorphism is a programming term that refers to the use of
the same function name, but with different signatures, for multiple types._

_Example of polymorphic functions with len()_
+ Example:
```python
print(len("hello world"))
print(len(["Python", "Java", "C++"]))
print(len({"Name": "Tonny", "Address": "Ukrain"}))
```

_Below is an example of how Python can use different types of classes in the same way.
For loops that iterate through multiple objects are created. Next, call the methods without caring about
what class each object belongs to. These methods are assumed to exist in every class._
+ Example:
```python
class Nican():
    def clas(self):
        print("S-class")

    def year(self):
        print("2020")

    def type(self):
        print("Cabriolet")


class BMW():
    def clas(self):
        print("A-class")

    def year(self):
        print("2018")

    def type(self):
        print("Sedan")


obj_ind = Nican()
obj_usa = BMW()
for car in (obj_ind, obj_usa):
    car.clas()
    car.year()
    car.type()
```

# Overloading vs Overriding

### Overloading

_Method Overloading in Python is a type of Compile-time Polymorphism using which we can define two or more methods
in the same class with the same name but with a different parameter list._
+ Example:
```python
class OverloadingExample:
    def add(self, x=None, y=None):
        if x != None and y != None:
            return x + y
        elif x != None:
            return x
        else:
            return 0


obj = OverloadingExample()

print("Value:", obj.add())
print("Value:", obj.add(4))
print("Value:", obj.add(10, 20))
```

### Overriding

_Method Overriding is a type of Run-time Polymorphism. A child class method overrides (or provides its implementation)
the parent class method of the same name, parameters, and return type. It is used to over-write (redefine) a parent
class method in the derived class._
+ Example:
```python

class A:

    def fun1(self):
        print('feature_1 of class A')

    def fun2(self):
        print('feature_2 of class A')


class B(A):

    # Modified function that is
    # already exist in class A
    def fun1(self):
        print('Modified feature_1 of class A by class B')

    def fun3(self):
        print('feature_3 of class B')


# Create instance
obj = B()

# Call the override function
obj.fun1()
```

| Method Overloading       | Method Overriding                                                                           |
|---------------------------------|---------------------------------------------------------------------------------------------|
|    In the method overloading, methods or functions must have the same name and different signatures.         | In the method overriding, methods or functions must have the same name and same signatures. |
|Method overloading is performed between methods within the class| Method overriding is done between parent class and child class methods.                     |
|It is a type of Compile-time Polymorphism| IIt is a type of Run-time Polymorphism |
|It occurs in the same class| It occurs in two classes via inheritance|
|Python does not support method overloading|Python supports method overriding|

#

_Polymorphism, a child class method is allowed to have the same name as the class methods in the parent class.
In inheritance, the methods belonging to the parent class are passed down to the child class. It's also possible to
change a method
that a child class has inherited from its parent._

_This is typically used whenever a parent class inherited method is not appropriate for the child class.
To rectify this situation, we use Method Overriding, which enables re-implementing of a method in a child class._
+ Example:
```python

class Helicopter:
    def intro(self):
        print("There are many types of helicopters.")

    def flight(self):
        print("Helicopter can fly")


class Plane(Helicopter):
    def flight(self):
        print("Plane can fly.")


class car(Helicopter):
    def flight(self):
        print("car cannot fly.")


obj_Helicopter = Helicopter()
obj_Plane = Plane()
obj_car = car()

obj_Helicopter.intro()
obj_Helicopter.flight()

obj_Plane.intro()
obj_Plane.flight()

obj_car.intro()
obj_car.flight()
```