# Python Complete Basics Guide

# 1. What is Python?

Python is a high-level, interpreted programming language known for:

* Simple syntax
* Easy readability
* Large libraries
* AI/ML, Web Dev, Automation, Data Science support

Example:

```python
print("Hello World")
```

Output:

```python
Hello World
```

---

# 2. Variables

Variables store data in memory.

```python
name = "Parth"
age = 20
height = 5.9
```

Here:

* `name` → string
* `age` → integer
* `height` → float

Python automatically detects datatype.

---

# 3. Data Types

## Integer (int)

Stores whole numbers.

```python
x = 10
```

---

## Float

Stores decimal numbers.

```python
price = 99.99
```

---

## String (str)

Stores text.

```python
name = "Python"
```

---

## Boolean (bool)

Stores True or False.

```python
is_student = True
```

---

# 4. Type Checking

Use `type()`.

```python
x = 10

print(type(x))
```

Output:

```python
<class 'int'>
```

---

# 5. Type Conversion

Convert one datatype into another.

```python
x = "10"

print(int(x))
```

```python
10
```

Examples:

```python
int()
float()
str()
bool()
```

---

# 6. Input and Output

## Taking Input

```python
name = input("Enter your name: ")
```

Input always comes as string.

---

## Printing Output

```python
print(name)
```

---

# 7. Operators

## Arithmetic Operators

Used for calculations.

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
```

---

## Comparison Operators

Returns True or False.

```python
10 > 5
10 == 10
10 != 5
```

---

## Logical Operators

```python
and
or
not
```

Example:

```python
x = 10

print(x > 5 and x < 20)
```

---

# 8. If Else Conditions

Used for decision making.

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

# 9. Loops

Loops repeat code.

---

## For Loop

Used when number of iterations is known.

```python
for i in range(5):
    print(i)
```

Output:

```python
0
1
2
3
4
```

---

## While Loop

Runs until condition becomes False.

```python
x = 1

while x <= 5:
    print(x)
    x += 1
```

---

# 10. Break Continue Pass

## break

Stops loop completely.

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

---

## continue

Skips current iteration.

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

---

## pass

Does nothing.

```python
for i in range(5):
    pass
```

---

# 11. Functions

Functions are reusable blocks of code.

---

## Creating Function

```python
def greet():
    print("Hello")
```

---

## Calling Function

```python
greet()
```

---

## Function with Parameters

```python
def add(a, b):
    print(a + b)

add(2, 3)
```

---

## Return Statement

`return` sends value back.

```python
def square(x):
    return x * x

result = square(4)

print(result)
```

---

# 12. Scope

Scope means where variable can be accessed.

---

## Local Scope

Variable inside function.

```python
def test():
    x = 10
    print(x)

test()
```

`x` cannot be used outside function.

---

## Global Scope

Variable outside function.

```python
x = 100

def show():
    print(x)

show()
```

---

## global Keyword

Changes global variable.

```python
x = 5

def change():
    global x
    x = 20

change()

print(x)
```

---

# 13. Lists

List stores multiple values.

```python
nums = [1, 2, 3]
```

Lists are:

* Ordered
* Mutable (changeable)

---

# Common List Methods

---

## append()

Adds element at end.

```python
nums = [1, 2]

nums.append(3)

print(nums)
```

Output:

```python
[1, 2, 3]
```

---

## insert()

Adds at specific position.

```python
nums.insert(1, 100)
```

---

## remove()

Removes specific value.

```python
nums.remove(2)
```

---

## pop()

Removes by index.

```python
nums.pop(0)
```

---

## sort()

Sorts list.

```python
nums.sort()
```

---

## reverse()

Reverses list.

```python
nums.reverse()
```

---

## index()

Finds position.

```python
nums.index(3)
```

---

## count()

Counts occurrences.

```python
nums.count(2)
```

---

# 14. Tuple

Tuple is immutable list.

```python
t = (1, 2, 3)
```

Cannot change values.

---

## Tuple Methods

```python
count()
index()
```

---

# 15. Set

Stores unique values.

```python
s = {1, 2, 3}
```

Properties:

* Unordered
* No duplicates

---

## Set Methods

### add()

```python
s.add(10)
```

---

### remove()

```python
s.remove(2)
```

---

### union()

Combines sets.

```python
a.union(b)
```

---

### intersection()

Common elements.

```python
a.intersection(b)
```

---

# 16. Dictionary

Stores key-value pairs.

```python
student = {
    "name": "Parth",
    "age": 20
}
```

---

# Dictionary Methods

## keys()

```python
student.keys()
```

---

## values()

```python
student.values()
```

---

## items()

```python
student.items()
```

---

## get()

Safer access.

```python
student.get("name")
```

---

# 17. Strings

Strings are sequence of characters.

```python
name = "Python"
```

---

# String Methods

---

## upper()

```python
name.upper()
```

---

## lower()

```python
name.lower()
```

---

## replace()

```python
name.replace("P", "J")
```

---

## split()

Converts string to list.

```python
text = "a b c"

text.split()
```

---

## strip()

Removes spaces.

```python
" hello ".strip()
```

---

# 18. Mutable vs Immutable

## Mutable

Can change after creation.

Examples:

* List
* Dictionary
* Set

---

## Immutable

Cannot change.

Examples:

* String
* Tuple
* Integer

---

# 19. List Comprehension

Short way to create lists.

```python
nums = [x for x in range(5)]
```

Output:

```python
[0,1,2,3,4]
```

---

# 20. Lambda Functions

Small anonymous functions.

```python
square = lambda x: x*x

print(square(5))
```

---

# 21. Exception Handling

Handles errors safely.

```python
try:
    print(10/0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# 22. File Handling

---

## Write File

```python
with open("test.txt", "w") as f:
    f.write("Hello")
```

---

## Read File

```python
with open("test.txt", "r") as f:
    print(f.read())
```

---

# 23. Object Oriented Programming (OOP)

OOP organizes code using objects and classes.

---

# 24. Class and Object

## Class

Blueprint/template.

## Object

Real instance of class.

---

## Example

```python
class Student:

    def show(self):
        print("Hello")

s1 = Student()

s1.show()
```

---

# 25. Constructor (**init**)

Constructor runs automatically when object is created.

```python
class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Parth")

print(s1.name)
```

---

# 26. self Keyword

`self` refers to current object.

```python
self.name
```

Without self, object cannot store values.

---

# 27. Instance Variables

Variables belonging to object.

```python
self.name
self.age
```

Each object has separate copy.

---

# 28. Inheritance

One class acquires properties of another.

```python
class Animal:

    def sound(self):
        print("Sound")

class Dog(Animal):
    pass

d = Dog()

d.sound()
```

Dog inherited `sound()`.

---

# 29. Polymorphism

Same method behaves differently.

```python
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")
```

---

# 30. Encapsulation

Restrict direct access.

```python
class Test:

    def __init__(self):
        self.__data = 10
```

`__data` becomes private.

---

# 31. Modules

Module = Python file containing code.

---

## Import Entire Module

```python
import math
```

---

## Import Specific Function

```python
from math import sqrt
```

---

# 32. Important Built-in Functions

---

## len()

```python
len([1,2,3])
```

---

## type()

```python
type(10)
```

---

## range()

```python
range(5)
```

---

## max()

```python
max([1,2,3])
```

---

## min()

```python
min([1,2,3])
```

---

## sum()

```python
sum([1,2,3])
```

---

## sorted()

```python
sorted([3,1,2])
```

---

# 33. Python Memory Concepts

---

## == Operator

Checks values.

```python
a = [1,2]
b = [1,2]

print(a == b)
```

Output:

```python
True
```

---

## is Operator

Checks memory location.

```python
print(a is b)
```

Output:

```python
False
```

---

# 34. Shallow Copy vs Deep Copy

---

## Shallow Copy

Copies reference of nested objects.

```python
import copy

a = [[1,2]]

b = copy.copy(a)
```

---

## Deep Copy

Completely independent copy.

```python
b = copy.deepcopy(a)
```

---

# 35. Common Interview Questions

---

## Difference Between List and Tuple

| List         | Tuple         |
| ------------ | ------------- |
| Mutable      | Immutable     |
| Slower       | Faster        |
| More methods | Fewer methods |

---

## Difference Between remove() and pop()

| remove()      | pop()         |
| ------------- | ------------- |
| Removes value | Removes index |
| remove(5)     | pop(0)        |

---

## Difference Between append() and extend()

### append()

Adds whole object.

```python
a.append([3,4])
```

Output:

```python
[1,2,[3,4]]
```

---

### extend()

Adds elements individually.

```python
a.extend([3,4])
```

Output:

```python
[1,2,3,4]
```

---

# 36. Common Python Imports for ML

```python
# Linear Models
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

# KNN
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor

# SVM
from sklearn.svm import SVC
from sklearn.svm import SVR

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor

# Random Forest
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

# XGBoost
from xgboost import XGBClassifier
from xgboost import XGBRegressor

# Clustering
from sklearn.cluster import KMeans
```

---

# 37. Final Important Notes

* Python is dynamically typed
* Python is interpreted
* Everything in Python is object
* Indentation matters in Python
* Lists are mutable
* Tuples are immutable
* Dictionary stores key-value pairs
* Constructor = `__init__`
* `self` refers to current object
* `is` checks memory
* `==` checks values

---