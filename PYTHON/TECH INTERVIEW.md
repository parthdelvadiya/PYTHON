# Python Interview Questions & Answers

# 1. Difference Between List and Tuple

## Answer

| List | Tuple |
|--------|--------|
| Mutable | Immutable |
| [] | () |
| Slower | Faster |
| More methods | Fewer methods |

```python
my_list = [1, 2, 3]
my_list.append(4)

my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Error
```

---

# 2. List Methods

## Common Methods

```python
append()
extend()
insert()
remove()
pop()
clear()
index()
count()
sort()
reverse()
copy()
```

Example:

```python
nums = [3, 1, 2]

nums.append(4)
nums.sort()

print(nums)
```

---

# 3. Tuple Methods

Only 2 methods:

```python
count()
index()
```

Example:

```python
t = (1, 2, 2, 3)

print(t.count(2))
print(t.index(3))
```

---

# 4. Set Methods

```python
add()
update()
remove()
discard()
pop()
clear()
union()
intersection()
difference()
```

Example:

```python
s = {1, 2, 3}
s.add(4)
```

---

# 5. Dictionary Methods

```python
keys()
values()
items()
get()
update()
pop()
popitem()
clear()
copy()
```

Example:

```python
student = {"name":"John"}

print(student.get("name"))
```

---

# 6. What is *args?

Used to pass multiple positional arguments.

```python
def add(*args):
    return sum(args)

print(add(1,2,3,4))
```

---

# 7. What is **kwargs?

Used to pass multiple keyword arguments.

```python
def info(**kwargs):
    print(kwargs)

info(name="John", age=25)
```

---

# 8. Difference Between args and kwargs

```python
*args   -> Positional arguments

**kwargs -> Keyword arguments
```

Example:

```python
def demo(*args, **kwargs):
    print(args)
    print(kwargs)
```

---

# 9. Reverse String

```python
s = "hello"

print(s[::-1])
```

Output:

```python
olleh
```

---

# 10. Swap Uppercase and Lowercase

```python
text = "PyThOn"

result = text.swapcase()

print(result)
```

Output:

```python
pYtHoN
```

---

# 11. Count Vowels

```python
s = "python"

count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print(count)
```

---

# 12. Check Palindrome

```python
s = "madam"

print(s == s[::-1])
```

---

# 13. Remove Duplicates from List

```python
nums = [1,2,2,3,4,4]

result = list(set(nums))

print(result)
```

---

# 14. Find Largest Number

```python
nums = [5,7,2,9]

print(max(nums))
```

---

# 15. Find Second Largest Number

```python
nums = [10,5,20,15]

nums.sort()

print(nums[-2])
```

---

# 16. Find Even Numbers

```python
nums = [1,2,3,4,5,6]

result = [i for i in nums if i % 2 == 0]

print(result)
```

---

# 17. Find Odd Numbers

```python
nums = [1,2,3,4,5]

result = [i for i in nums if i % 2 != 0]

print(result)
```

---

# 18. String Indexing

```python
s = "Python"

print(s[0])
print(s[-1])
```

---

# 19. String Slicing

```python
s = "Python"

print(s[0:4])
print(s[::-1])
```

---

# 20. List Comprehension

```python
squares = [x*x for x in range(5)]

print(squares)
```

---

# 21. Dictionary Comprehension

```python
square = {x:x*x for x in range(5)}

print(square)
```

---

# 22. What is Lambda Function?

```python
square = lambda x: x*x

print(square(5))
```

---

# 23. What is map()?

```python
nums = [1,2,3]

result = list(map(lambda x:x*2, nums))

print(result)
```

---

# 24. What is filter()?

```python
nums = [1,2,3,4]

result = list(filter(lambda x:x%2==0, nums))

print(result)
```

---

# 25. What is zip()?

```python
names = ["A","B"]
marks = [90,80]

print(list(zip(names,marks)))
```

---

# 26. Difference Between Deep Copy and Shallow Copy

```python
import copy

a = [[1,2]]

b = copy.copy(a)
c = copy.deepcopy(a)
```

---

# 27. What is enumerate()?

```python
names = ["a","b","c"]

for index, value in enumerate(names):
    print(index,value)
```

---

# 28. Check Prime Number

```python
n = 13

for i in range(2,n):
    if n%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
```

---

# 29. Fibonacci Series

```python
a,b = 0,1

for _ in range(5):
    print(a)
    a,b = b,a+b
```

---

# 30. Factorial

```python
n = 5
fact = 1

for i in range(1,n+1):
    fact *= i

print(fact)
```

---

# 31. Count Character Frequency

```python
s = "banana"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch,0)+1

print(freq)
```

---

# 32. Find Duplicate Characters

```python
s = "programming"

for ch in set(s):
    if s.count(ch) > 1:
        print(ch)
```

---

# 33. Merge Two Dictionaries

```python
d1 = {"a":1}
d2 = {"b":2}

result = {**d1, **d2}

print(result)
```

---

# 34. Sort Dictionary by Value

```python
d = {"a":3,"b":1,"c":2}

print(sorted(d.items(), key=lambda x:x[1]))
```

---

# 35. Read File

```python
with open("data.txt","r") as f:
    print(f.read())
```

---

# 36. Write File

```python
with open("data.txt","w") as f:
    f.write("Hello")
```

---

# 37. Append File

```python
with open("data.txt","a") as f:
    f.write("Python")
```

---

# 38. Exception Handling

```python
try:
    print(10/0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# 39. Multiple Exceptions

```python
try:
    pass

except ValueError:
    pass

except TypeError:
    pass
```

---

# 40. Finally Block

```python
try:
    print("Hello")

finally:
    print("Executed")
```

---

# 41. Class Example

```python
class Student:

    def __init__(self,name):
        self.name = name

obj = Student("John")
```

---

# 42. Inheritance

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

# 43. Method Overriding

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
```

---

# 44. Static Method

```python
class Demo:

    @staticmethod
    def add(a,b):
        return a+b
```

---

# 45. Class Method

```python
class Demo:

    count = 0

    @classmethod
    def update(cls):
        cls.count += 1
```

---

# 46. Generator

```python
def nums():

    for i in range(5):
        yield i

for i in nums():
    print(i)
```

---

# 47. Iterator

```python
nums = iter([1,2,3])

print(next(nums))
```

---

# 48. Find Missing Number

```python
nums = [1,2,3,5]

n = 5

expected = n*(n+1)//2

print(expected - sum(nums))
```

---

# 49. Flatten Nested List

```python
nested = [[1,2],[3,4]]

result = [item for sub in nested for item in sub]

print(result)
```

---

# 50. Most Asked Output Question

```python
a = [1,2,3]
b = a

b.append(4)

print(a)
```

Output:

```python
[1,2,3,4]
```

Reason:

```python
Both variables point to same object.
```

---

# 51. Difference Between is and ==

```python
a = [1,2]
b = [1,2]

print(a == b)
print(a is b)
```

Output:

```python
True
False
```

---

# 52. Mutable vs Immutable

Mutable:

```python
list
set
dict
```

Immutable:

```python
tuple
str
int
float
frozenset
```

---

# 53. What is __init__ ?

Constructor method executed automatically during object creation.

```python
class Demo:

    def __init__(self):
        print("Constructor")
```

---

# 54. What is pass?

Placeholder statement.

```python
def demo():
    pass
```

---

# 55. What is None?

Represents absence of value.

```python
x = None
```

---

# 56. Difference Between remove(), pop(), del

remove()

```python
nums.remove(3)
```

pop()

```python
nums.pop()
```

del

```python
del nums[0]
```

---

# 57. Find All Uppercase Characters

```python
s = "PyTHon"

for ch in s:
    if ch.isupper():
        print(ch)
```

---

# 58. Convert Every Character Case Manually

```python
s = "PyTHon"

result = ""

for ch in s:

    if ch.isupper():
        result += ch.lower()
    else:
        result += ch.upper()

print(result)
```

---

# 59. Find Common Elements

```python
a = [1,2,3]
b = [2,3,4]

print(list(set(a)&set(b)))
```

---

# 60. Remove Spaces

```python
s = "Hello World"

print(s.replace(" ",""))
```

---