# Enumerations

_The "enum" module in Python is used to implement enumerations. Classes are used to build enumerations.
Enums are related with names and values._

+ Enums may be shown as a string or a representation.
+ Enums' types may be tested using type ().
+ The name of the enum member is shown using the "name" keyword.
+ Example:

```python
from enum import Enum


class Week(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


# printing enum member as string
print(Week.Monday)

# printing name of enum member using "name" keyword
print(Week.Monday.name)

# printing value of enum member using "value" keyword
print(Week.Monday.value)

# printing the type of enum member using type()
print(type(Week.Monday))

# printing enum member as repr
print(repr(Week.Monday))

# printing all enum member using "list" keyword
print(list(Week))

```

Output:

```
Week.Monday
Monday
1
<enum 'Week'>
<Week.Monday: 1>
[<Week.Monday: 1>, <Week.Tuesday: 2>, <Week.Wednesday: 3>, <Week.Thursday: 4> , <Week.Friday: 5> ,\
 <Week.Saturday: 6> , <Week.Sunday: 7>]
```

# Accessing Mode

+ Example:
  _There are two ways to access an enum member:_

+ By value: The value of an enum member is supplied in this procedure.
+ By name: The name of the enum member is supplied in this method.
  _The "name" or "value" keyword can also be used to access a different value or name._

```python
from enum import Enum


class Week(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


# Accessing enum member using value
print("The enum member associated with value 2 is : ", Week(2).name)

# Accessing enum member using name
print("The enum member associated with name AUTUMN is : ", Week['AUTUMN'].value)
```

_Great examples of enumerations in programming are the days of the week, Earth's cardinal directions, a program's status
codes,the months and seasons of
the year, the colors of a traffic light, and pricing schemes for web services._

# problems: Enumerations vs Constants(how to compare them)
