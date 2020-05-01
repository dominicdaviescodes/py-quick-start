# Section 5: Conditionals

control flow of execution, perform actions if specific conditions are met

```python
raining = input("is_it_raining? (yes/no)")
if raining == "yes":
    print("You need an umbrella")

# is_it_raining? (yes/no)yes
# You need an umbrella
```
### If statement (the simplest)

```python
# ask user for integer between -10 and 10
# if they enter < 5 print message to user

# input always returns users response as a string so n is a string
# a str and int can't be compared to eachother
n = input("Please enter a integer between -10 and 10, enter it here: ")
# change n to an int
n = int(n)
# now can compare values
if n < 5:
    print("You entered a value less than 5")

```
### If- else statement: perform action if condition is met. And if not met perform a different action.
```python
def minimum(x, y):  # generic representations of inputs
    if x < y:
        return x
    else:
        return y
# if x and y are same doesn't matter that y is returned

# test out minimum on inputs 2 and 5
result = minimum(2, 5)
print(result)
# 2

```
```python
def minimum(x, y):
    if x < y:
        return x
    else:
        return y


# test out minimum on inputs -2 and -5
result = minimum(-2, -5)
print(result)

```
```python
def minimum(x, y):
    if x < y:
        return x
    else:
        return y


# test out minimum on inputs 7 and 7
result = minimum(7, 7)
print(result)

```
```python
def minimum(x, y):
    if x < y:
        return x
    else:
        return y


# test out minimum on inputs 3 and 3.1
result = minimum(3, 3.1)
print(result)
# 3

```
### If-elif statement: perform an action if condition is met or another if another condition is met
```python
raining = input("is it raining? (yes/no)")
umbrella = input("Do you have and umbrella? (yes/no)")
# want to check 2 conditions
if raining == "yes" and umbrella == "yes":
    print("Don't forget your umbrella when you go out")
# if both aren't met
elif raining == "yes" and umbrella == "no":
    print("Where a waterproof coat when you go out")

```
can have multiple elif statements
```python
x = input("Enter number here: ")
# convert x from a string to float
# use built in float function that takes in a number and returns it as a float
x = float(x)  # doesn't alter numerical value this way. but float to int does
if x < 2:
    print("The number is less than 2.")
elif x < 6:
    print("The number is less than 6.")
elif x < 8:
    print("The number is less than 8.")
elif x < 10:
    print("The number is less than 10.")

```
#### if you ran the above with if statements ... 
```python
x = input("Enter number here: ")
# convert x from a string to float
# use built in float function that takes in a number and returns it as a float
x = float(x)  # doesn't alter numerical value this way. but float to int does
if x < 2:
    print("The number is less than 2.")
if x < 6:
    print("The number is less than 6.")
if x < 8:
    print("The number is less than 8.")
if x < 10:
    print("The number is less than 10.")

```

```python
# prints

# Enter number here: 1.5 which is less than all the conditions

# The number is less than 2.
# The number is less than 6.
# The number is less than 8.
# The number is less than 10.

```

```python


```
```python


```
```python


```
```python


```
```python


```
```python


```
```python


```
```python


```
```python


```
```python


```
```python


```