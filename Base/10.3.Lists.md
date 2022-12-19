## List
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data,
lists are created using square brackets:
```python
the_list = ["apple", "banana", "orange", "cherry"]
print(the_list)     # ['apple', 'banana', 'orange', 'cherry']
```
#### List items are ordered, changeable, and allow duplicate values:
```python
the_list = ["apple", "banana", "apple" ,  "orange", "cherry"]
print(the_list[0])   # apple
the_list[-1] = "dragon fruit"
print(the_list)      # ['apple', 'banana', 'apple', 'orange', 'dragon fruit']
```
#### Basic list function:
```python
num_list = [12,21,78]
print(len(num_list))    # 3
print(max(num_list))    # 78
print(min(num_list))    # 12
print(sum(num_list))    # 111
print(num_list * 2)     # [12, 21, 78, 12, 21, 78]
```
#### Print a list of elements:
```python
#1
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)
#2
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*numbers)
```
#### List comprehension
```python
numbers = [i for i in range(10)]
squares = [i ** 2 for i in range(10)]
lines = [input() for _ in range(int(input()))]
```
## List Methods

### list.append()  -->  Adds an element at the end of the list
```python
list_0 = [1,2,3,4]
list_0.append(12)
print(list)     # [1, 2, 3, 4, 12] 
list_0.append([10,78])
print(list)     # [1, 2, 3, 4, 12, [10, 78]]
```
### list.clear() -->   Removes all the elements from the list
```python
list_1  = [65,76,87,98,12]
list_1.clear()
print(list)         # <class 'list'>
```
### list.copy()  -->  Returns a copy of the list
```python
list1 = [1,2,3,4,5,"Yes"]
list2 = list1.copy()
print(list2)        # [1, 2, 3, 4, 5, 'Yes']      
print(list2 == list1)       # True
```
### list.count()  -->  Returns the number of elements with the specified value
```python
test_count = [1,1,8,"bio",4,1]
print(test_count.count(1))      # 3
```
### list.extend() -->   Add the elements of a list (or any iterable), to the end of the current list
```python
test_count.extend([45,1,78])    
print(test_count)           # [1, 1, 8, 'bio', 4, 1, 45, 1, 78]
test_count.extend("Hello")
print(test_count)           # [1, 1, 8, 'bio', 4, 1, 45, 1, 78, 'H', 'e', 'l', 'l', 'o']
```
### list.index()  -->  Returns the index of the first element with the specified value
```python
print([23,65,43,5].index(5)) # 3
```
### list.insert()  -->  Adds an element at the specified position
```python
test = ["pizza","burger","coke"]
test.insert(1,"sprite")
print(test)         #['pizza', 'sprite', 'burger', 'coke']
```
### list.pop() -->   Removes the element at the specified position
```python
test.pop(2)
print(test)     # ['pizza', 'sprite', 'coke']
test.pop()
print(test)     # ['pizza', 'sprite']
```
### list.remove()  -->  Removes the first item with the specified value
```python
L = [16,98,56,4]
L.remove(98)
print(L)        # [16, 56, 4]
```
### list.reverse()  -->  Reverses the order of the list
```python
L.reverse()
print(L)        # [4, 56, 16]
```
### list.sort()  -->  Sorts the list
```python
L.sort()
print(L)        # [4, 16, 56]
```