# Descriptor

_A descriptor is, generally speaking, an object attribute with a binding behavior, one whose access is controlled by
methods in the descriptor protocol. These are the methods: "get," "set," and "delete." Any of these stated methods
for an object are referred to as descriptors._

### __get__() and __set__()

_Descriptors are frequently used to control access to instance data. The descriptor is associated with a public
attribute in the class dictionary, whilst the actual data is kept in the instance dictionary as a private attribute.
When the public attribute is accessed, the __get__() and __set__() methods of the descriptor are called._

+ Example:

```python
class Celsius:

    def __get__(self, instance, owner):
        return 5 * (instance.fahrenheit - 32) / 9

    def __set__(self, instance, value):
        instance.fahrenheit = 32 + 9 * value / 5


class Temperature:
    celsius = Celsius()

    def __init__(self, initial_f):
        self.fahrenheit = initial_f


t = Temperature(212)
print(t.celsius)
t.celsius = 0
print(t.fahrenheit)
```

### @property, @setter, @getter, @deleter

+ Example:

_The Pythonic alternative to formal getter and setter methods in your code is property(). You may convert class
characteristics into managed attributes or properties using this method. Protected and private fields can be altered.
You don't need to import anything to use property() because it is a built-in method._

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Gett the name')
        return self._name

    @name.setter
    def name(self, value):
        print('Sett the name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Delet the name')
        del self._name


ex = Person('Adam')
print('The name is:', ex.name)
ex.name = 'John'
del ex.name
```

_Here, we've utilized the @property decorator rather using the property() method._

_First, we clarify that the name() function is a Person property. As seen in the example,
this is accomplished by using @property before the getter method._

_The setter and deleter are then specified using the attribute name._

_Use @name.setter for the setter function and @name.deleter for the deleter method to do this._

_You'll see that we defined the getter, setter, and deleter using distinct definitions of the same function name()._

_As seen by the written output existing inside the method, anytime we use p.name,
it now internally calls the necessary getter, setter, and deleter._