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