# Abstraction(Abstract Classes, Abstract Methods)

_An abstract class is a class, you cannot directly construct objects from it.
Its goal is to specify the characteristics of other classes, such as the methods and attributes
that should be included in them._

### Why Use Abstract Base Classes?

_Since they lack the method implementation, abstract classes—as we have already discussed—are
used to design the framework for our classes. This is a very helpful feature, especially when child
classes need to offer their own unique implementation._

_To define an abstract class, you use the abc (abstract base class) module._

_The abc module provides you with the infrastructure for defining abstract base classes._

_To define an abstract method, you use the @abstractmethod decorator_

+ Example:

```python
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):

        Pass
```

_Say that we wish to draw several shapes. To do this, we develop a fundamental abstract class called Shape,
which will serve as the guide for subsequent forms. This class will offer the methods that must be used by
its child classes to implement particular shapes._

+ Example:

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, shape):
        self.shape = shape

    @abstractmethod
    def draw(self):
        pass
```

_As you may have noticed, we have declared the method draw() to be undefined.
The other classes that inherit from this class will implement this method._

_We create classes Circle and Triangle, which will implement the draw() method and inherit the Shape class._

+ Example:

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, shape):
        self.shape = shape

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self):
        super().__init__("circle")

    def draw(self):
        print("Drawing a Circle")


class Triangle(Shape):

    def __init__(self):
        super().__init__("triangle")

    def draw(self):
        print("Drawing a Triangle")


# create a circle object
circle = Circle()
circle.draw()

# create a triangle object
triangle = Triangle()
triangle.draw()
```

# Difference between abstract class and interface

| Interface                                                                                                                 | Abstract class                                                          |
|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| There can only be abstract methods on an interface. Since Java 8, it is also capable of having static and default methods. | Both abstract and non-abstract methods can be found in abstract classes. |
| Multiple inheritance is supported via interface.                                                                          | Multiple inheritance is not supported by abstract classes.              |
| The interface class comes with its own fields and logic                           | The abstract class is just a template                                   |

# Abstract Methods

_A method that is declared but lacks an implementation is said to be abstract. Subclasses are required to provide
implementations for the abstract methods since abstract classes cannot be instantiated._

### @abstractmethod, @abstractproperty

_A decorator indicating abstract methods._

_As seen in the following instances of usage, abstractmethod() should be used as the innermost decorator when combined
with other method descriptors:_

_Python uses getters and setters in the form of properties. To utilize abstract properties, use the @abstractproperty
decorator in the ABC module._

+ Example:

```python
class Example(ABC):
    @abstractmethod
    def abstract_method(self, arg1):
        ...

    @classmethod
    @abstractmethod
    def abstract_classmethod(cls, arg2):
        ...

    @staticmethod
    @abstractmethod
    def abstract_staticmethod(arg3):
        ...

    @property
    @abstractmethod
    def abstract_property(self):
        ...

    @abstractmethod
    def _get_x(self):
        ...

    @abstractmethod
    def _set_x(self, val):
        ...

    x = property(_get_x, _set_x)
```

# Protocol

_Similar to Go, this capability enables you to create interfaces and verify that objects fulfill them implicitly.
This is what is known as static duck typing._

```python

```

# Problems:

3. Abstract Instances / Invoke Methods from Abstract Class
    4. Implementation through Subclassing
    5. Protocol and Duck Typing