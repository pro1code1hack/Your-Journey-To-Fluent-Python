# Collections module

Collections module provides you with more specialized container datatypes that might be helpful in some situations. In
order to use the module you obviously have to import it:

```python
import collections
```

Or if you need something specific from collections module, for example Counter write:

```python
from collections import Counter
```

*To learn more about imports read Import.md*

## Contents

1. namedtuple()
2. deque
3. DefaultDict
4. OrderedDict
5. Counter
6. ChainMap

## Named tuple

`namedtuple()` is a factory function which gives you possibility to create subclass of tuples with named fields. These
fields give you direct access to the values by their named using dot notation. This is useful because using indexes
for accessing values in tuples might be unreadable and unclear.

### Syntax

`collections.namedtuple(typename, field_names)`

### Example

```python
from collections import namedtuple

Product = namedtuple('product', ['name', 'price', 'amount'])

product1 = Product('banana', 4, 45)

print(product1)

print(product1.name)
```

#### Output:

```
product(name='banana', price=4, amount=45)
banana
```

namedtuple also provide some useful features, such as ***default values***, ***replacing values*** and ***generating
dicts***
from tuples:

```python
from collections import namedtuple

# default vales:
Product = namedtuple('product', ['name', 'price', 'amount'], defaults=[0, 0])
product1 = Product('banana')
print(product1)

# generating dict from tuple:
print(product1._asdict())

# replacing the value of the field:
product1 = product1._replace(name="potato", price=4, amount=4)
print(product1)
```

#### Output:

```
productname=('banana', price=0, amount=0)  # defaults
{'name': 'banana', 'price': 0, 'amount': 0}  # _asdict()
product(name='potato', price=4, amount=4)  # _replace()
```

## Deque

Deque(double-ended queue) is basically a list with more optimized **append** and **pop** operations on both sides of the
sequence.

### Syntax

`collections.deque(list)`

#### Example

```python
from collections import deque

dq = deque([1, 2, 3])

print(dq)
```

#### Output

```
deque([1, 2, 3])
```

### Adding and removing values

One of the most significant advantages of deque is ability to add or delete elements to the sequence on both sides much
more efficiently than if it was just a simple list and here is how it's done:

1. `append()` - adds element to the end of a deque
2. `appendleft()` - adds element to the beginning of a deque
3. `pop()` - delete element from the end of a deque
4. `popleft()` - delete element from the beginning of a deque

#### Example(1, 2)

```python
from collections import deque

dq = deque([1, 2, 3, 4])

# add an element to the end of a deque using append()
dq.append(5)
print(f'deque after adding 5 to the end using append(): {dq}')

# add an element to the beginning of a deque using appendleft()
dq.appendleft(0)
print(f'deque after adding 0 to the beginning using append(): {dq}')
```

#### Output:

```
deque after adding 5 to the end using append(): deque([1, 2, 3, 4, 5])
deque after adding 0 to the beginning using append(): deque([0, 1, 2, 3, 4, 5])
```

#### Example(3, 4)

```python
from collections import deque

dq = deque([1, 2, 3, 4])

# add an element to the end of a deque using append()
dq.pop()
print(f'deque after using pop(): {dq}')

# add an element to the beginning of a deque using appendleft()
dq.popleft()
print(f'deque after using popleft(): {dq}')
```

#### Output:

```
deque after using pop(): deque([1, 2, 3])
deque after using popleft(): deque([2, 3])
```

### Important

All list methods can be used with deque.

## DefaultDict

Dictionary-like containers, such as Defaultdict, can be found in module collections. The dictionary class's subclass
defaultdict produces objects that mimic dictionaries. Except the fact that defaultdict never raises a KeyError,
if a key doesn't exist, it provides a default value.

### Syntax

`collections.defaultdict(default_factory)`

parameter `default_factory` - A function returning the default value for the dictionary defined. If this argument is
absent then the dictionary raises a KeyError.

### Example

```python
from collections import defaultdict


# Function to return a default values for keys that is not present
def default_value():
    return 0


d = defaultdict(default_value)
d["a"] = 1
d["b"] = 2
print(d)

print(d["a"])
print(d["b"])

# calling a non-existent key
print(d["c"])
```

#### Output:

```
defaultdict(<function default_value at 0x10e0e3eb0>, {'a': 1, 'b': 2})
1
2
0
```

## OrderedDict

Ordered dict is just a dict that remembers in what order keys were created, but with python 3.7 even simple dicts are
capable of doing it, so it is pretty much useless.

## Counter

In programming, counting objects is a common process. Consider the situation when you need to count the number of times
an item appears in a list or iterable. If your list is not too long, counting the items on it should be simple and
quick. It will be harder to count the items if your list is lengthy.
<br\>
You normally use a counter or an integer variable with a zero initial value to count things. The counter is then
increased to represent the frequency of each object. A dictionary can be used in Python to count multiple things at
once. In this instance, the values will include the number of instances of a particular object, or the object's count,
while the keys will record specific objects. Here is an example using a common dictionary and a for loop to count the
letters in a word:

```python
word = "mississippi"
letter_counter = {}

for letter in word:
    if letter not in letter_counter:
        letter_counter[letter] = 0
    letter_counter[letter] += 1

print(letter_counter)
```

#### Output:

```
{'m': 1, 'i': 4, 's': 4, 'p': 2}
```

But it is little complicated and there is a better way of doing this, counter:

### Syntax

```
collections.Counter([iterable-or-mapping])
```

### Example

```python
from collections import Counter

# With sequence of items  
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B',
               'B', 'A', 'C']))
```

#### Output:

```
Counter({'B': 5, 'A': 3, 'C': 2})
```

## ChainMap

A ChainMap delivers a list of dictionaries after condensing numerous dictionaries into a single item.

### Syntax

```
collections.ChainMap(dict1, dict2)
```

### Example

```python
from collections import ChainMap

d1 = {'v': 3, 'n': 6}
d2 = {'dc': 3, 'c': 4}
d3 = {'ewe': 5, 'ftt': 6}
print(ChainMap(d1, d2, d3))
```

#### Output:

ChainMap({'v': 3, 'n': 6}, {'dc': 3, 'c': 4}, {'ewe': 5, 'ftt': 6})

```

```

### Accessing values and keys

values can be accesed by using key names, also values() and keys() methods work with chainmap.

### Adding dicts

you can add dict to a chainmap by using new_child() method, this way new dict will be added to the beginning of a
chainmap:

```python
from collections import ChainMap

d1 = {'v': 3, 'n': 6}
d2 = {'dc': 3, 'c': 4}
d3 = {'ewe': 5, 'ftt': 6}

cm = ChainMap(d2, d3)
print(cm)

cm = cm.new_child(d1)
print(cm)
```

#### Output:

```
ChainMap({'dc': 3, 'c': 4}, {'ewe': 5, 'ftt': 6})
ChainMap({'v': 3, 'n': 6}, {'dc': 3, 'c': 4}, {'ewe': 5, 'ftt': 6})
```
