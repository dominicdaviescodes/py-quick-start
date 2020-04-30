Python uses operating system-specific interpreters to execute code.

Data is categorized into different types.

### Booleans
* data type bool

### integers whole numbers

### floating point (decimals) 
* data type: float

### strings
* data type: str
* arithmatic expression in quotes is a string

##  Storing data using variables

Example: Hangman
Game over when-
* all guesses are used up
* guess word correctly

We need to keep track of how many guesses are remaining.
Use a variable, can access and change value when you want.
Name should indicate what the variable contains. eg email contains an email address.
* create variable at beginning
* call it guesses with a value of 10
* guesses will need to be updated throughout game
* value will decrease by 1 each guess
  
```python
guesses = 10
print(guesses)

# 10
```

```python
guesses -= 1
print(guesses)

# 9
```

```python
guesses -= 1
print(guesses)

# 8
```
# Goal of programming:
### Solve problems efficiently

You could potentially have repeated code everywhere.
* takes longer to write code
* takes longer for computer to execute instructions

## Need to be concise and organised
#### Use Functions!
* each function performs a particular procedure
* write a set of instructions and store in a function
* just (call it) refer to that function whenever you want to use it

## Built in functions
functions that have already been defined.
* print() takes in data and shows it on screen. works with all data types
* input() ask user for data which you can work with. prompt user and save in a variable.

```python
name = input("what is your name?")
color = input("what's your fave color?")
```
user provides data by responding to the prompts

what is your name? Dom
what's your fave color?  red

check we recieved the data

```python
print(name) # Dom
print(color) # red

```
now we can greet the user using these variables

```python

print("hi " + name + "! " + color + " is a great color!")

```

```python

name = input("what is your name?")
color = input("what's your fave color?")

print(name)
print(color)

print("hi " + name + "! " + color + " is a great color!")

# hi Dom! red is a great color!
```
# Define and call your own functions

```python

def functionName(inputName or leave empty):
    body # what needs to be performed.
```
```python

def addFive(x):
    print(5 + x)

addFive(30) # 35
addFive(62.5)   # 67.5
```
### function that doesn't use an argument
```python
def greeting():
    print("Hey there!")

greeting()
```
### function that recieves an input and doesn't return an output

```python
def greet(name):
    print("Hi " + name + "!")

greet("Joshua")
```
### function that takes in a number as input and returns square of it. recieves and returns.
```python
def square(x):
    return x * x

result = square(5)

print(result)
#25
```

```python
def square(x):
    return x * x

result = square(5)

print(result)

anotherOne = square(result)
print(anotherOne)
```
#### functions can take more than one input
```python
def sumOfSquares(x, y):
    square1 = x * x
    square2 = y * y
    return square1 + square2


result = sumOfSquares(2, 3)
print(result)
```
### function that doesn't recieve input and returns output
```python
# ask user if it's raining today
def is_it_raining():
    raining = input("Is it raining today?")
    return raining


tuesday_rain = is_it_raining()
print(tuesday_rain)

```
# Modules - reuse code that's already been written

## Useful module: calendar

```python
import calendar
cal = calendar.month(2019, 7)

print(cal)

# prints
     July 2019
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
```
## Useful module: math
gives access to math functins

```python
# square roots

import math

result = math.sqrt(49)
print(result)

# 7.0 always returns float
```
### random module
lots of functions related to randomness

```python
import random

# takes 2 inputs and returns a random integer that lies between the 2
number = random.randint(1,100)

print(number)
```

```python
import random

movies = ["Lion King", "Spider Man", "John Wick", "Pets"]

watch = random.choice(movies)
print(watch)
```
can shuffle items
```python
import random

movies = ["Lion King", "Spider Man", "John Wick", "Pets"]

random.shuffle(movies)
print(movies)

# ['John Wick', 'Pets', 'Spider Man', 'Lion King']
```
# Section 4: Sequences, collections of data

## Store an individual piece of data (variable) string

```python
name = "brad"
```
## store a collection of data (variable) list
```python
group = ["Daniel", "Mary", "Gloria"]
```
## Lists
lists can contain mixed data types, integers, strings etc.
```python
n = 5
print(n)
# 5
```
store multiple numbers in a list, specific order, square brackets. store the list in a variable
```python
listA = [5, 10, 15, 20]
print(listA)

# [5, 10, 15, 20]
```
access an item from the list
zero based 
```python
listA = [5, 10, 15, 20]
print(listA[2])
# 15
```
change a value
```python
listA = [5, 10, 15, 20]
listA[2] = 150

print(listA[2])

# 150
```
# Tuples (protect your data)
* a sequence that can't be changed after creation

```python
child1_birth = ("Julia", "Lucile Hospital", "Stanford", "California", "United States", "07/29/2019", "16:25")
child2_birth = ("John", "Mount Hospital", "Glamorgan", "Cardiff", "Wales", "09/29/2019", "16:25")

print(child1_birth)
# ('Julia', 'Lucile Hospital', 'Stanford', 'California', 'United States', '07/29/2019', '16:25')
```
```python
print(child1_birth[0])
# Julia
```
lists can be modified, tuples can't have items modified, ie. you can't change time of birth index 6.
```python

```
