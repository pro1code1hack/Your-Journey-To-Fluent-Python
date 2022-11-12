# Arithmetic operators(+, -, *. /, //, %, **)
## (+), (-), (*), (/), (**)
In order to make simple arithmetic operations with variables or values, such as division, 
multiplication, addition, division, etc. You will need arithmetical operators, mostly they are
similar to real mathematical symbols and aren't hard to remember.
<br/>
The most simple arithmetic operators in python are:
1. addition - (+)
2. subtraction - (-)
3. multiplication - (*)
4. division - (/)
5. power - (**)

and they work absolutely identically to actual math:
```python
print(3 + 3)
print(3 - 3)
print(3 / 3)
print(3 * 3)
print(3 ** 3)
```
#### Output:
```
6
0
1
9
27
```
## //, %
These two are little harder but still very easy ones.
### modulus - (%)
In calculations, the modulus operation returns the remainder  or signed remainder of
division after one number is divided by another. It might sound complicated but in reality it is 
very easy, here is example:
```python
print(10 % 3)
print(10 % 4)
print(10 % 5)
print(10 % 6)
```
#### Output:
```
1
2
0
4
```
### floor division - (//)
For positive numbers floor division works just like simple division, except it ignores decimal
part of the result:
```python
print(10 // 1)
print(10 // 4)
print(10 // 6)
print(10 // 12)
```
#### Output:
```
10
2
1
0
```
With negative numbers it just rounds to other side:
```python
print(10 // 3)
print(-10 // 3)
```
#### Output:
```
3
-4
```
## Important:
### 1
The priority of arithmetical operators in python:
1. Firstly goes power(**);
2. Then multiplication, division, modulus and floor division(*, /, %, //);
3. And lastly addition and subtraction(+, -).
### 2
result of module division `n % m`, if `n > m` will be `n`, example: `10 % 12 = 10`.
