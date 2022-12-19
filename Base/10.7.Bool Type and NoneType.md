## Boolean Type
Python boolean type is one of the built-in data types provided by Python, which represents one of the two values i.e. 
True or False. Generally, it is used to represent the truth values of the expressions. For example, 1==1 is True whereas 2<1 is False.
```python
a = True
b = False
print(type(a))      # <class 'bool'> 
print(type(b))      # <class 'bool'>
```
#### Method `bool()` 
```python
x = 5
y = 10
print(bool(x > y))      # False
a = 10 -5
b = 5
print(bool(a==b))       # True
```
### Boolean operators
| A	    | B	     | A or B |
|-------|--------|--------|
| True  | 	True  | 	True  |
| True  | 	False | 	True  |
| False | 	True  | 	True  |
| False | 	False | 	False |

| A	    | B	     | A and B |
|-------|--------|---------|
| True  | 	True  | 	True   |
| True  | 	False | 	False  |
| False | 	True  | 	False  |
| False | 	False | 	False  |

| A	    | Not A  |
|-------|--------|
| True  | 	False |
| False | 	True  |

## NoneType
 The None keyword is used to define a null value, or no value at all. 
 
None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType)
```python
test = None
print(test)     # None
```