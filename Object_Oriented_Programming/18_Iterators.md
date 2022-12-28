# Iterators

_In Python, iterators are used extensively. Within for loops, comprehensions, generators, etc.,
they are skillfully integrated._

_An object that may be iterated upon is known as an iterator in Python. a data-returning object
that does so one element at a time._

_A Python iterator object is required to implement the iterator protocol, which is made up of the two special methods
__iter__() and __next__()._

# \_\_next__()

_The subsequent item in the container is returned by this procedure. The StopIteration exception should be
raised if there are no more items._

+ Example:

```python

my_list = [1, 2, 3, 4]

my_iter = iter(my_list)

print(next(my_iter))  # Output: 1

print(next(my_iter))  # Output: 2

print(my_iter.__next__())  # Output: 3

print(my_iter.__next__())  # Output: 4

# This will raise error, no items left
next(my_iter)
```

_Output:_

```
1
2
3
4

```

# \_\_iter__()

_As previously noted, this function returns the iterator object itself. This is necessary so that the for and in
commands may utilize iterators and containers together._

```python
my_list = [1, 2, 3, 4]

iter_val = iter(my_list)  #
while (True):
    try:
        value = next(iter_val)
        print(value)
    except StopIteration:
        break
```

_We can also use for loop. We may iterate over any object that can yield an iterator with this, including lists,
strings, files, and many more._

+ Example:

```python
my_list = [1, 2, 3, 4]

for element in my_list:
    print(element)

```

_Output:_

```
1
2
3
4
```

+ Example:

```python
text = "Hello World "
for i in text:
    print(i)

```

_Output:_

```
H
e
l
l
o  

W
o
r
l
d
```

+ Example:

```python
class Example:

    def __init__(self, limit):
        self.n = 1
        self.limit = limit

    def __next__(self):
        if self.n <= self.limit:
            output = 2 ** self.n
            self.n += 1
            return output
        else:
            raise StopIteration


ex = Example(3)

print(next(ex))  # prints 1
print(next(ex))  # prints 2
print(next(ex))  # prints 4
print(next(ex))  # prints 8
print(next(ex))  # raises StopIteration exception
```

_Output:_

```
2
4
8
Traceback (most recent call last):
File "<string>", line 25, in <module>
  File "<string>", line 16, in __next__
StopIteration
```

+ Example:

```python
class GoodExample:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 4
        return num


ex = GoodExample()
myiter = iter(ex)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

```

_Output:_

```
1
5
9
13
```