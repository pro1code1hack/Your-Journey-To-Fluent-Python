## Strings

Besides numbers, Python can also manipulate strings, which can be expressed in several ways.
They can be enclosed in **single quotes** ('...') or **double quotes** ("...")
with the same result, \ can be used to escape quotes:
```python
print('Hi world')       # Hi world
print("Hi world")       # Hi world
print(type("Hi world"))      # <class 'str'>
```
#### Accessing characters in Python String:
Like many other popular programming languages, strings in Python are arrays of bytes
representing unicode characters. However, Python does not have a character data type,
a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
```python
s  = "Hello Python"
print(s[0])     # H
print(s[4])     # o
print(s[-1])    # n 
print(s[:5])    # Hello
print(s[6:])    # Python
print(s[::-1])  # nohtyP olleH
```
##### String length:
To get the length of a string, use the `len()` function.
```python
a = "Hello world"
print(len(a))       # 11
```
##### String Concatenation:
Strings, like numbers, can be added. 
The operation of adding strings is called concatenation or concatenation.
```python
s_1 = "Python is "
s_2 = "high-level "
s_3 = "programming language"
print(s_1 + s_2 + s_3 + "!!!")   # Python is high-level programming language!!!
```
In Python, you can also multiply a string by a number.
```python
s = "Hi"
print(s * 5)        # HiHiHiHiHi
```
## Strings methods
The most popular string methods
### str.capitalize() --> Converts the first character to upper case
```python
test_0 = 'hello WoRLd'
test_1 = "HI EHOR"
print(test_0.capitalize())      # Hello world
print(test_1.capitalize())      # Hi ehor
```
### str.count() -->  Returns the number of times a specified value occurs in a string
```python
print(test_0.count("o"))        # 2
print(test_1.count("h"))        # 0
```
### str.endswith() --> Returns true if the string ends with the specified value
```python
print("I am Vlad".endswith("d"))        # True
print(test_1.endswith("r"))             # False
```
### str.find()  -->  Searches the string  and returns the position of where it was found
```python
print("Oh,shit".find("h"))      # 1
print("Im sorry".find("y"))     # 7
```
### str.isalnum() -->    Returns True if all characters in the string are alphanumeric
```python
s = "13bruh3801"
print(s.isalnum())      # True
print("!@#$#%$#*".isalnum())        # False
```
### str.isalpha() -->    Returns True if all characters in the string are in the alphabet
```python
print("Yes".isalpha())          # True
print("Yes123".isalpha())       # False
```
### str.isdigit() -->    Returns True if all characters in the string are digits
```python
print("$1290".isdigit())        # False
print("106".isdigit())          # True
```
### str.islower()  -->   Returns True if all characters in the string are lower case
```python
print("hello world".islower())      # True
print("Hello World".islower())      # False
```
### str.isupper() -->    Returns True if all characters in the string are upper case
```python
print("HELLO EVERYBODY".isupper())      # True
print("FDSNSLAVESJKs".isupper())        # False
```
### str.join() -->   Converts the elements of an iterable into a string
```python
List = ["Three","Hundred","Bucks"]
print("$".join(List))           # Three$Hundred$Bucks
print("0".join("1"*8))          # 101010101010101
```
### str.lower() -->   Converts a string into lower case
```python
print("VLAD".lower())       # vlad
print(test_0.lower())       # hello world
```
### str.upper() -->   Converts a string into upper case
```python
print("just do it".upper())         # JUST DO IT
print("yes sir".upper())            # YES SIR
```
### str.lstrip() -->   Returns a left trim version of the string
```python
print("    Lets go".lstrip())         # Lets go
print("    danger!".lstrip())        # danger!
```
### str.replace() -->   Returns a string where a  value is replaced with a specified value 
```python
breakfast =  "My breakfast is  apple"
print(breakfast.replace("apple","burger"))      # My breakfast is  burger
print(breakfast.replace("My","Your"))           # Your breakfast is  apple
```
### str.rstrip()  -->  Returns a right trim version of the string
```python
print("I like it    ".rstrip())         # I like it
print('Python   '.rstrip())             # Python
```
### str.split() -->   Splits the string at the specified separator, and returns a list
```python
print("Python,Java,C,Assembler".split(","))  # ['Python', 'Java', 'C', 'Assembler']
print("1!2!3!4!5!".split("!"))          # ['1', '2', '3', '4', '5', '']
```
### str.startswith() -->	Returns true if the string starts with the specified value
```python
print("I like Python".startswith("I"))          # True  
print("I like Python".startswith("You"))        # False
```
### str.strip() -->   Returns a trimmed version of the string
```python
print("    !King James!    ".strip())       # !King James!
print("    !MJ Goat!   ".strip())           # !MJ Goat!
```
### str.swapcase() -->   Swaps cases, lower case becomes upper case and vice versa
```python
print("HI python".swapcase())           # hi PYTHON
print("wHO aRE yOU?".swapcase())        # Who Are You?
```
### str.title() -->    Converts the first character of each word to upper case
```python
print("i want pizza".title())           # I Want Pizza
print("apple banana cherry".title())    # Apple Banana Cherry  
```