## Dict
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:
```python
test_dict = {
    "name" : "Aleks",
    "year" : 1980,
    "height" : 6.5    
}
print(test_dict)        # {'name': 'Aleks', 'year': 1980, 'height': 6.5}
```
Dictionary items:
```python
test_dict = {
    "name" : "Aleks",
    "year" : 1980,
    "height" : 6.5    
}
print(test_dict["height"])      # 6.5
```
Duplicates on dictionary:
```python
test_dict = {
    "name" : "Aleks",
    "year" : 1980,
    "height" : 6.5,
    "year" : 1995
}
print(test_dict["year"])        # 1995
```
The values in dictionary items can be of any data type:
```python
test_dict = {
    "name" : "Anton",
    "age" : 23,
    "hobbies" : False,
    "list_of_pets" : ["dog","cat","hamster"]
}
```
### Dict methods
### dict.clear() --> Remove all the elements from the dictionary
```python
dict = {
    "one" : 1,
    "two " : 2,
    "three" : 3
}
print(dict.clear())     # None
```
### dict.copy() --> Returns a copy of the dictionary
```python
dict_0 = {
    "one" : 1,
    "two " : 2,
    "three" : 3
}
dict1 = dict_0.copy()
print(dict1)        # {'one': 1, 'two ': 2, 'three': 3}
```
### dict.get() --> Returns the value of specified key
```python
test_dict = {
    "Math" : 87,
    "English" : 68,
    "Chemistry" : 55,
    "Physics" : 91
}
print(test_dict.get("Math"))        # 87
```
### dict.items() --> Returns a list containing a tuple for each key value pair
```python
print(test_dict.items())            # dict_items([('Math', 87), ('English', 68), ('Chemistry', 55), ('Physics', 91)])
```
### dict.keys() --> Returns a list containing dictionary’s keys
```python
print(test_dict.keys())         # dict_keys(['Math', 'English', 'Chemistry', 'Physics'])
```
### dict.pop() --> Remove the element with specified key
```python
test_dict.pop("Chemistry")
print(test_dict)            #{'Math': 87, 'English': 68, 'Physics': 91}
```
### dict.popitem() --> Removes the last inserted key-value pair
```python
item = test_dict.popitem()
print(test_dict)        # {'Math': 87, 'English': 68}
print(item)             #('Physics', 91)
```
### dict.update() --> Updates dictionary with specified key-value pairs
```python
test_dict.update({item})
print(test_dict)        # {'Math': 87, 'English': 68, 'Physics': 91}
```
### dict.values() --> Returns a list of all the values of dictionary
```python
print(test_dict.values())       # dict_values([87, 68, 91])
```