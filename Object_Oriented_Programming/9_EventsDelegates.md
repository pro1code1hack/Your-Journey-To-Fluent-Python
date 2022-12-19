# Events

_Python's Event Handler class functions in a manner comparable to those of other programming languages.
We now realize that organizing an event is essentially like raising a flag for it.
And an event handler is a class that manages and keeps track of these events. A user form serves as a fairly
straightforward illustration of how events and event handlers operate. Once the user has finished filling out the
information, they must click the submit button to send and process the information. There are two endpoints in Python,
where we mentioned events._

_One is the class that raises the event and is referred to as a publisher, while the other class is referred to as#
subscribers and is in charge of receiving the raised events._
_As a result, each additional event handler that is linked to the event is called sequentially when it is fired._

+ Example:

````python
# Event
def chop_vegetables():
    print("chopping vegetables")
    return True


def salt_soup():
    print("salting soup")
    return True


def boil_water():
    print("boiling water")


def make_soup(on_done1, on_done2):
    boil_water()
    on_done1()
    on_done2()
    print("soup is ready")


make_soup(chop_vegetables, salt_soup)

````

# Delegation

_Delegation is a method that is object-oriented (also called a design pattern). Let's imagine you wish to alter the
behavior of only one of an object's methods, let's call it object x. The method you want to change can be provided
with a new implementation in a new class, which delegated all other methods to the corresponding method of x._

_Delegation may be readily implemented by Python programmers. For instance, the class that implements such behavior
is the one that changes all written data to uppercase and functions as a file:_

+ Example:

```python
class Microwave:
    def __init__(self):
        pass

    def heat_up_food(self):
        print("Food is being microwaved")


class Dishwasher:
    def __init__(self):
        pass

    def wash_dishes(self):
        print("Dishwasher starting")


class Kitchen:
    def __init__(self):
        self.microwave = Microwave()
        self.dishwasher = Dishwasher()

    def heat_up_food(self):
        self.microwave.heat_up_food()

    def wash_dishes(self):
        self.dishwasher.wash_dishes()
```

_Consider the Kitchen class for the sake of this illustration. Kitchens don't actually work as rooms in real life,
but we think of a kitchen's usefulness as being made up of the appliances it possesses. I can heat things up in my
kitchen if it has a microwave, and I can wash dishes in my kitchen if it has a dishwasher._

_The Kitchen class has the characteristics of the Microwave and Dishwasher classes. Our kitchen can now use their
techniques._