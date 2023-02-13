# Generators

_Python generators are objects that allow for the same kind of list-like looping as other objects.
Lazy iterators' contents are not kept in memory like lists are. Using generators to iterate over
enormous datasets is the most effective method._

_In Python, creating a generator is not too difficult. It is just as simple to define a yield statement-based
function as a return statement-based function would be._

_In contrast to a return statement, which completely ends a function, a yield statement just stops the function
while saving all of its state and continuing running on subsequent calls._

_To exclude odd integers from a range of n numbers. The following two approaches might be used to resolve the issue._

+ Example(using function):

```python
def even_integers_function(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result
```

_use the Generator function. We may loop through the generator object produced by the generator method below to obtain
a list of even integers._

+ Example:

```python
def even_integer_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
```

+ Example:

```python
def revers(text):
    length = len(text)
    for i in range(length - 1, -1, -1):
        yield text[i]


# For loop to reverse the string
for i in revers("olleh"):
    print(i)
```

_It is possible to declare a function in Python that operates like an iterator, making it quick, simple,
and tidy for programmers to create iterators._

### Generator function and normal function are different

+ There are one or more yield functions in generator functions but only one function in normal functions.
+ Between calls, local variables and their states are retained.
+ On subsequent calls, *StopIteration* is automatically invoked when the generator function ends.
  _To prevent the iteration to go on forever, we can use the *StopIteration* statement._
+ The call is moved to the generator function when the generator function is invoked,
+ pausing the normal function's execution in the process.

### Yield vs Return

| Yield                                                                                                                                     | Return                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| It regulates how the generator works in terms of flow. It pauses the execution by saving the states after returning the value from yield. | The function is ended by the return statement which also returns the value. |
| It serves generating purposes.                                                                                                            | It is employed for typical functions.                                       |

# List comprehensions vs generator expressions

_It is a good approach to list definition and construction. We may use the for loop to generate a list with less code
by utilizing list comprehension. What typically requires three to four lines of code can be condensed into only one._

```python
ls = []

for i in range(13):
    if i % 2 == 0:
        ls.append(i)

print(ls)

>> > [0, 2, 4, 6, 8, 10, 12]
```

_Basically, if all you're doing is iterating once, use a generator expression. You're probably better off using a list
comprehension if you wish to store and use the created results._

### Yield and yield from

_The numbers 0 to 5 are also produced by this iteration of funk(). It doesn't seem necessary to say that we want to loop
through and yield the values of both funk2 and funk3, though. Here lies the value of produce from._

```python
def funk2():
    for i in range(10):
        yield i


def funk3():
    for j in range(10, 20):
        yield j


def generator():
    for i in funk2():
        yield i
    for j in funk3():
        yield j

```

_With this new keyword, funk can be rewritten._

```python
def generator():
    yield from funk2()
    yield from funk3()
```




