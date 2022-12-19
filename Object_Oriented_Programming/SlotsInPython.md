# Slots
_Python uses a unique method called slots to decrease object memory. All Python objects add attributes via a dynamic dictionary. Slots is a static type method, therefore allocating attributes is not dependent on a dynamic dictionary._
+ Example:
```python
class Example(object):

    # defining the slots
    __slots__ = (a, b) 

     def __init__(self, *args, **kwargs):

         # initializing the values
         self.a = value1
         self.b = value2
```
+ Example:
```python
# defining the class.
class LaptopStor:
      
    # defining the slots.
    __slots__ =('brand', 'price')
      
    def __init__(self):
          
        # initializing the values
        self.brand ='Lenovo'
        self.price = 3999
  
# create an object of Example class
a = Example()
  
# print the slot
print(a.__slots__)
  
# print the slot variable
print(a.brand, a.price)
```

_It involves using __slots__ to instruct Python to only allocate space for a predetermined set of characteristics rather than using a dict. Here is an illustration using slots and without slots_

_Benefits:_
+ You may reduce your memory footprint by using __slots__. 
+ In some circumstances, the code will run more quickly when using __slots__. 
+ Use these slots when you know you'll be using a large number of objects (millions or more) and that they don't need to be dynamic.