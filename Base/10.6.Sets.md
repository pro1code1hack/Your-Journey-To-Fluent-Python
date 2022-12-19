## Set
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data,
A set is a collection which is unordered, unchangeable*, and unindexed.
```python
test_set = {"apple",243,"banana",True}
print(test_set)     # {'apple', True, 'banana', 243}
# Sets are unordered, so you cannot be sure in which order the items will appear
```
Set items are unordered, unchangeable, and do not allow duplicate values.
```python
test_set = {"name","height","weight","name"}
print(test_set)     # {'name', 'height', 'weight'}
```
### Set methods
### set.add() -->	Adds a given element to a set
```python
set = {12,45,90}
set.add(19)
print(set)      # {90, 19, 12, 45}
```
### set.clear() -->	Removes all elements from the set
```python
test_set = {9,99,999}
test_set.clear()
print(test_set)     # set()
```
### set.copy() -->	Returns a shallow copy of the set
```python
test_set = {9,99,999}
test_set_1 = test_set.copy()
print(test_set_1)       # {9, 99, 999}
```
### set.difference() -->	Returns a set that is the difference between two sets
```python
set_1 ={1,3,7,16,45}
set_2 ={7,3,45}
print(set_1.difference(set_2))      # {16,1}
```
### set.discard() -->	Removes the element from the set
```python
set_1 ={1,3,7,16,45}
set_1.discard(45)
print(set_1)        # {16, 1, 3, 7}
```
### set.frozenset() -->	Return an immutable frozenset object
```python
test_set = frozenset("apple")
print(test_set)     # frozenset({'l', 'e', 'a', 'p'})
```
### set.intersection() -->	Returns a set that has the intersection of all sets
```python
set_1 = {"meat","potatoes","juice","chocolate"}
set_2 ={"fish","potatoes","cola","juice"}
print(set_1.intersection(set_2))        # {'juice', 'potatoes'}
print(set_1)        # {'meat', 'potatoes', 'chocolate', 'juice'}
```
### set.intersection_update() -->	Updates the existing caller set with the intersection of sets
```python
set_1 = {"meat","potatoes","juice","chocolate"}
set_2 ={"fish","potatoes","cola","juice"}
set_1.intersection_update(set_2)
print(set_1)        # {'potatoes', 'juice'}
```
### set.isdisjoint() -->	Checks whether the sets are disjoint or not
```python
my_set = {11, 27, "Yes"}
print(my_set.isdisjoint(['2', 10, 18]))     # True
print(my_set.isdisjoint([2, 11, 18]))       # False
```
### set.issubset() -->	Returns True if all elements of a set A are present in another set B
```python
set_1 = {5,10,15}
print(set_1.issubset([5,10]))       # False
print(set_1.issubset([5,10,15]))    # True
print(set_1.issubset([5,10,15,20])) # True
```
### set.issuperset() -->	Returns True if all elements of a set A occupies set B
```python
set_1 = {5,10,15}
print(set_1.issubset([5,10]))       # True
print(set_1.issubset([5,10,15]))    # True
print(set_1.issubset([5,10,15,20])) # False
```
### set.pop() -->	Returns and removes a random element from the set
```python
test_set = {11,26,39,4}
print(test_set.pop())       # 26
print(test_set)             # {11, 4, 39}
```
### set.remove() -->	Removes the element from the set
```python
fruit_set = {"apple","orange","banana","cucumber"}
fruit_set.remove("cucumber")
print(fruit_set)        # {'apple', 'banana', 'orange'}
```
### set.union()   -->	Returns a set that has the union of all sets
```python
test_set_1 = {1,2,3,4}
test_set_2 = {4,5,6,7}
test_set_3 = test_set_1.union(test_set_2)
print(test_set_3)       # {1, 2, 3, 4, 5, 6, 7}
```
### set.update()  -->	Adds elements to the set
```python
set = {"milk",89,True,10}
set.update([12,56,"juice"])
print(set)          # {True, 'juice', 10, 12, 'milk', 56, 89}
```