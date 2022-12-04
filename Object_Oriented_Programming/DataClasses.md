# Data classes
_Python classes called dataclasses are specifically designed to store data objects.
This module offers a decorator and utilities for automatically adding produced special methods to user-defined classes, such as __init__() and __repr__()._
```python
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
```
_Redundancy is evident in this scenario right away.
There are numerous instances of the title and author identifiers.
The overridden __eq__ and __repr__ methods will still be present in the real class._
```python
from dataclasses import dataclass

@dataclass
class Laptop:
    brand: str
    price: int
```
_The @dataclass decorator is part of the dataclasses package.
Using it, the following code would appear:_

_The parameters to dataclass() are:_
+ init: __init__() method will be created if the condition is true, which is the default.
This option is ignored if __init__() is already defined for the class.
+ repr: A __repr__() function will be created if the condition is true (the default).
The name of the class as well as the names and reprs of each field, in the order they are declared in the class, will be included in the generated repr string.
The fields that are designated as not being included in the repr are not.
InventoryItem(name='widget', unit price=3.0, quantity on hand=10), as an illustration.
This parameter is not used if repr () is already defined in the class. 
+ eq: An __eq__() method will be created if the value is true (the default). The class is compared using this method as if it were a tuple of fields, in order. The comparison's two instances must be of the same type.
This option is not taken into account if the class already defines __eq__().
+ order: If true (the default is False), the following methods will be generated: __lt__, __le__, __gt__, and __ge__.
These compare the class in the same order as a tuple of its fields.
The types of the two occurrences in the comparison must match.
A ValueError is raised if order is true while eq is false.
A TypeError is triggered if the class already defines any of the methods __lt__, __le__, __gt__, or __ge__. 
+ unsafe hash: If False (the default), a __hash__() function is produced based on the values of eq and frozen.
Built-in hash() and the addition of objects to hashed collections like dictionaries and sets both make use of __hash__().
A __hash__() indicates that the class's instances are immutable.
The existence and operation of __eq__(), as well as the values of the eq and frozen flags in the dataclass() decorator, all affect the intricate attribute of mutability. 
+ frozen: assigning to fields will result in an exception if frozen is true (the default value is False).
This simulates frozen read-only instances.
TypeError is thrown if the class defines __setattr__ or __delattr__.
the conversation that follows. 
+ match args: If true (the default is True), the list of parameters to the generated __init__() function will be used to create the __match args__ tuple (even if __init__() is not generated, see above).
If either of these conditions is true or if __match args__ has already been specified in the class, __match args__ will not be produced. 

_We might want a "leptops" class containing a list of books. If you run the following code: arbitrary methods._
```python
@dataclass
class Laptop:
    laptops: List[laptop] = []
```
+ Output:
```
ValueError: mutable default <class 'list'> for field laptops is not allowed: use default_factory
```
_It is advised to utilize the default factory argument of the field function to prevent issues. Any callable object or function without parameters may be used as its value._
```python
@dataclass
class Bookshelf:
    books: List[Book] = field(default_factory=list)
```
_The @dataclass decorator adds the properties of the class being processed after iterating through all parent classes beginning with object and locating each data class. It then stores the fields for each data class it finds in an ordered mapping. The fields from the resulting sorted dictionary are used by all created methods._

_As a result, you must define fields with default values if the parent class sets default values._

```python
@dataclass
class box:
    model: Any = None
    price: int = None

@dataclass
class laptop(box):
    descr: str = None
    model: str = "Unknown"
```
_will generate an __init__ method with this signature:_
```
def __init__(self, model: str="Unknown", price: str=None, descr: str=None)
```

