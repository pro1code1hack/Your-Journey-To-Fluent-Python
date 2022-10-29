# Logical operations
## if/else
Ok, now we know how to make arithmetical operations and input and output data, but code must
be able to do different tasks in relation to input. to make decisions program identifies either
a statement is true or false. Consider this example:
```python
country = input('which country are you from?')
if country == 'Ukraine':
    print('you are Ukrainian')
else:
    print('you are not Ukrainian')
```
Program asks user to write  his country and if it is true that variable `country` equals 
`'Ukraine'`then it prints:
```
you are Ukrainian 
```
else:
```
you are not Ukrainian
```
pretty straight forward, isn't it.
## relational operators
Sometimes only checking equality will not be enough, for example if you have to compare two
or more values(bigger, smaller, etc.). It is very simple and quite similar to actual math:
<br/>
(>) - greater than;
<br/>
(>=) - greater or equal to;
<br/>
(<) - less than;
<br/>
(<=) - less or equal to;
<br/>
(!=) - not equal.
<br/>
Example:
```python
age = int(input('what is your age'))
if age >= 18:
    print('you are old enough')
else:
    print('you re not old enough')
```
the program waits for user to type his age and writes this value into the `age` variable.
Then it checks if `age` is equal or greater than 18, it prints 'you are old enough',
and if the statement is false - 'you are not old enough'.
## elif
The `elif` is a shortened version of else if, it allows you to have multiple conditions in one body
, if the condition of block `if` is false then it checks next `elif` block, and so on, and so on,
until all the elif blocks finish and then `else` block executes. Example:
```python
num = 0
if num > 0:
    print(num, 'is a positive number')
elif num == 0:
    print(num, 'is zero')
else:
    print(num, 'is a negative number')
```
#### Output:
```
0 is zero
```
this program firstly checks if `num` is greater than 0, or if it is positive. Then, if the
statement is false it goes to `elif blocks` and checks if number equals zero, which it does,
and because it is true, program prints 'o is zero'.
## logical operators
Sometimes you will need more complex statements, for example, if you have to compare more than one
variable with different values in one statement. And here go logical operators, they are used on 
conditional statements (either True or False). They perform Logical AND, Logical OR and Logical
NOT operations.

| Operator	 | Description	                                         | Syntax   |
|-----------|------------------------------------------------------|----------|
| and       | 	Logical AND: True if both the operands are true     | 	x and y |
| or        | 	Logical OR: True if either of the operands is true	 | 	x or y  |
| not       | 	Logical NOT: True if operand is false	              | 	not x   |
Example:
```python
a = 10
b = 10
if a > 0 and b > 0:
    print('both numbers are positive')
elif a > 0 or b > 0:
    print('one number is positive')
else:
    print('neither of numbers is positive')
```
#### Output:
```
both numbers are positive
```
This program checks if variables `a` and `b` are positive nad prints different
texts in relation to values of `a` and `b`.
#### Important:
If you have more than one logical operator in one statement then they execute
in exact order:
<br/>
firstly - `not`
<br/>
secondly - `and`
<br/>
thirdly - `or`