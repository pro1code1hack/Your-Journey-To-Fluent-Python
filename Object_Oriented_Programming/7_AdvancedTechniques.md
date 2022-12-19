# Advanced Techniques

### Composition

_A notion that models a connection is composition. By merging items of different kinds, it makes it possible to create
complicated types. This implies that an object of the type Component can be contained in an object of the class
Composite. A Composite has a Component as a result of this connection._

_Instead of inheriting properties, the composition technique creates methods between classes, allowing the code to be
reused. Yes, classes produced by composition are more adaptable than those generated through heritage.
This is due to the fact that it is more productive to add new features without altering the current code structure._

+ One (or more) examples of the other classes are used to generate one of the classes that are present in the compositi
+ By adding items to several objects, code may be reused.
+ We may also do some class-specific tasks without utilizing every property of a different class.

+ Example:

```python
class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:
    def __init__(self, pay, bonus):
        self.bonus = bonus
        self.obj_salary = Salary(pay)

    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() + self.bonus)


obj_emp = Employee(100, 10)
print(obj_emp.annual_salary())
```

### Aggregation

_An idea known as "aggregation"refers to the ability of an item of one class to possess or have access to an
independent object of another class._

+ It is a one-way relationship or a unidirectional association. For instance, a department can have students,
  but the opposite is not feasible, making this relationship unidirectional.
+ Since both items in Aggregation can persist on their own, eliminating one won't have an impact on the other.

+ Example:

```python
class Salary:
    def __init__(self, pay):
        self.__pay = pay

    @property
    def pay(self):
        return self.__pay

    @pay.setter
    def pay(self, value):
        self.__pay = value

    def get_total(self):
        return (self.pay * 12)


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return "Total: " + str(self.pay.get_total() + self.bonus)


obj_sal = Salary(100)
obj_emp = Employee(obj_sal, 10)
print(obj_emp.annual_salary())
```

### Association

_It is a relationship between two classes, and their objects serve to create that relationship.
There is no owner object; each item has its own life cycle. It's a flimsy kind of a connection.
One-to-one, one-to-many, many-to-one, or many-to-many are all possible._

_For instance, both classes of pupils and professors are connected. There is no owner and each class's objects have
their own life cycles._

+ Example:

```python
class A(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def addNums(self):
        return self.b + self.c


class B(object):
    def __init__(self, d, e):
        self.d = d
        self.e = e

    def addAllNums(self, Ab, Ac):
        x = self.d + self.e + Ab + Ac
        return x


a = A("hi", 2, 6)
b = B(5, 9)

print(b.addAllNums(a.b, a.c))
```

### instead of composition, use aggregation

_Composition and Aggregation are subsets of association, which means that they are particular instances of association.
Objects of one class "own" objects of another class in both aggregate and composition. However, there is a minute
distinction:_

+ Aggregation suggests a connection in which the kid is free to exist without the parent.
  Example: Student and Class (parent) (child). If you delete the class, the students are still there.

+ Composition suggests a connection in which the kid is dependent on the parent for existence.
  Example: Room and House (parent) (child). A house and its rooms are one and the same.