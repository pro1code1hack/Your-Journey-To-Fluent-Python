# Mixin

_A class that offers method implementations for reuse by several connected child classes is
known as a mixin. The inheritance does not, however, establish a connection._

_A mixin collects a group of techniques for reuse. Each mixin should implement a single
distinct behavior using techniques that are closely related._

_Mixin classes should be named with the suffix Mixin because Python does not specify a formal way to define them._

+ Example:

```python
class Graphic:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y


class Mixin:
    def resize(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y


class ResizableClass(Mixin, Graphic):
    pass


rge = ResizableGraphicalEntity(6, 2, 20, 30)
rge.resize(200, 300)
```

_Here, the class Mixin derives straight from object rather than Graphic,
therefore ResizableClass just receives the resize function from it._

_As we previously stated, this makes the ResizableClass
inheritance tree simpler and lowers the danger of the diamond problem._

_It frees us from having to inherit undesirable methods when using Graphic
as a parent for other types._

_Tips:_

+ Simple class modifications are added using mixin classes.
+ Python uses multiple inheritance to implement mixins, which have a powerful expressive capacity but call for careful
  design.