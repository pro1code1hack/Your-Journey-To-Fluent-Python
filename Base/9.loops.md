# loops in python
One of the main advantages of computer over human is that he can repeat the same task over
and over again without tiring. To repeat the same part of code multiple times in python loops
can be used. There are two common types of loops in python:
1. `for` - counting function, it will repeat exact amount of times;
2. `while` - conditional function, it will repeat while condition is `True`.
## while
Structure of the loop `while` in python looks like this:
```python
while condition:
    code
```
For example:
```python
text = input()
while text != "stop":
    print("write 'stop' to leave the loop")
    text = input()
```
This loop will continue printing "write 'stop' to leave the loop" and will only stop if user 
inputs "stop".
<br/>
you can also create infinite loop if you want, it will just execute code infinite amount of 
times, for example:
```python
while True:
    print("Fuck you")
```
This might seem useless, but with operator `break`(that we will discuss later) it becomes 
very useful.
## for
We use `for` when we need to repeat code exact amount of time that we already know. Structure 
of this loop:
```python
for loop_variable in range(number of iterations):
    code
```
And real example(Usually for loop variable used `i` name but it can be changed):
```python
for i in range(5):
    print("Fuck you")
```
#### Output:
```
Fuck you
Fuck you
Fuck you
Fuck you
Fuck you
```
you can also use variable `i` in code inside the loop if you need, value of `i`
will always start from 0 and wil; never reach 5:
```python
for i in range(5):
    print(i)
```
#### Output:
```
0
1
2
3
4
```
Again name `i` can be changed if you want!
## range
You already saw usage of `range()` in previous examples but this function has much more
functional than just it. In reality there are 3 arguments in this function. Its real look by 
default looks like that:
```
range(start=0, end, step=1)
```
`start` - starting point and is 0 by default so it can by optional:
```python
for i in range(0, 3):
    print(i)
print("==========")
for i in range(3):
    print(i)
```
#### Output
```
0
1
2
==========
0
1
2
```
so, as you can see both outputs are the same because parameter start is 0 by default,
but for example if you have to start not from 0 but from 2 you will have to use 
parameter `start`:
```python
for i in range(2, 7):
    print(i)
```
#### Output:
```
2
3
4
5
6
```
`end` - ending point, and is mandatory. 
<br/>
`step` - difference in values of `i` between iteration, is optional and set as 1 by default.
For example you want to print all even numbers in a set from 2 to 10 included, you can make
it using `step` and `end`:
```python
for i in range(2, 11, 2):
    print(i)
```
#### Output:
```
2
4
6
8
10
```
I wrote 11 here instead of 10 because end is not included.
<br/>
`step` can also be negative, then i will decrease with every iteration:
```python
for i in range(5, 0, -1):
    print(i)
```
#### Output:
```
5
4
3
2
1
```
## break, continue and else
### break and continue
Statement `break` forces program to immediately leave the loop sometimes even without
finishing iteration.
```python
while True:
    num = int(input("write number that is not 0"))
    if num == 0:
        break
```
this program has infinite loop and every iteration uszer is asked to type in a number that
is not 0, but if he will input 0 program will leave the loop thereby finishing itself.
<br/>
Statement `continue` is used to immediatly pass to the next iteration of a loop,for example 
you can write program that prints all the numbers from 1 to 15 except 4 and 13:
```python
for i in range(1, 16):
    if i == 4 or i == 13:
        continue
    print(i, end=", ")
```
#### Output:
```
1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 
```
### else
useless thing, but ok.
<br/>
`else` in function is written just after `if` or `while` blocks and the code in `else` will
only run if loop ended naturally(not by `break`):
```python
for i in range(0, 5):
    print(i)
else:
    print("finish")
```
#### Output:
```
0
1
2
3
4
finish
```
but if you break the loop:
```python
for i in range(0, 5):
    print(i)
    if i == 2:
        break
else:
    print("finish")
```
#### Output:
```
0
1
2
```
the code in `else` will not run.
### Important:
#### 1
Remember `break` only exits the closest loop, what it means is that if you have a loop in a 
loop `break` will only exit from the closest one:
```python
for i in range(1000):
    print("first loop")
        for j in range(1000):
            print("second loop")
            if input() == "stop":
                break
```
the program will firstly enter the first loop and print "first loop" once, entering
second loop after that where each iteration user will be able to input "stop" and
if he will it will exit from the second loop. But not from the first one. The same thing with 
`continue`.
#### 2
`else` is not affected by `continue`.
## Real usage examples:
### First example:
Using loops we can create a program that will calculate mean of an 
infinite amount of numbers:
```python
counter = 0
summ = 0
while True:
    choice = input("do you want to add a number(y/n)")
    if choice == 'y':
        counter += 1  #counter = counter + 1
        summ += int(input())
    else:
        print('mean =', summ/counter)
        break
```
#### Output:
```
do you want to add a number(y/n)y
input new number34
do you want to add a number(y/n)y
input new number54
do you want to add a number(y/n)y
input new number45
do you want to add a number(y/n)y
input new number23
do you want to add a number(y/n)n
mean = 39.0
```
Every single iteration this program asks user if they want to continue
adding numbers to the set of numbers mean of which will be found. If
user answers 'n' program prints mean and finishes.
### Second example:
Population of beers in Miskolc decreases by 50% every year. Using
loops we can calculate population after n years(if we know initial
number, lets say it equals 2048):
```python
years = int(input("input years"))
population = 2048
for i in range(years):
    population *= 0.5
print("population after", years, "years will be", int(population))
```
#### Output:
```
input years6
population after 6 years will be 32
```
Firstly we ask user for a number of years, then we iterate this much times
and every iteration multiply by 0.5, which basically means -50%.
After this we print result using `int()` function which makes a
variable have int data type, automatically rounding it(we do it because 
we don't want to have 0.5 bears).