print(0.1 + 0.2 == 0.3)
# False Floating point precision issue.

print(bool("False"))
# True

x = {1,2,3}
y = {3,4,5}
print(x & y)
# 3 intersection

# `	Union  
{1,2} | {3,4} = {1,2,3,4}

# -	Difference	
{1,2} - {2,3} = {1}

# ^	Symmetric diff	
{1,2} ^ {2,3} = {1,3}

print((1, 2, 3) + (4,))
# (1,2,3,4)
# (4,) is a tuple with one element 
# The comma is necessary — otherwise (4) is just an integer
# (1,2,3)+(4) is an error 

print(type(lambda x: x))
# <class 'function'>

print(True + True) # 2
print(False + True) # 1

print(bool([]), bool([0]))
# False True
# An empty list is considered False in Python.
# Even though it contains 0 (which is False individually), the list itself is not empty, so it is True.
# Non-empty containers → True

print([0], [False], [""])
# True,True,True

print(None == False)
# False

import numpy as np

c = np.array([1, 2, 3])
d = c[1:]
d[0] = 99

print(c)
# [ 1 99  3]
# d = c[1:] creates a view, not a copy.
# So d and c share the same memory.
# c = [1, 2, 3]
# d = [2, 3] (view of c)

s = "42"
print(s.zfill(5))
# 00042

# ljust(width, fillchar)
s = "Hi"
print(s.ljust(5))
'Hi   '

print(s.ljust(5, '*'))
'Hi***'

print(s.rjust(5))
'   Hi'

print(s.center(6, '-'))
'--Hi--'

s = "  Hello  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
'Hello'
'Hello  '
'  Hello'

s = "-42"
print(s.zfill(5))
# '-0042' keeps the sign 

# If you need to check membership (x in data) in a large dataset, which datatype is best?

# | Data Type   | Membership Speed |
# | ----------- | ---------------- |
# | list        | O(n)            |
# | tuple       | O(n)            |
# | dict (keys) | O(1)            |
# | set         | O(1) ✅ (BEST)    |

arr = [5, 2, 9, 1]
print(sorted(arr))

# Internally → uses Timsort
# | Case           | Complexity     |
# | -------------- | -------------- |
# | ✅ Best Case    | O(n)       |
# | ✅ Average Case | O(n log n) |
# | ✅ Worst Case   | O(n log n) |

# Searching Algorithm
# | Algorithm              | Best | Average  | Worst    | Notes             |
# | ---------------------- | ---- | -------- | -------- | ----------------- |
# | **Linear Search**      | O(1) | O(n)     | O(n)     | Works on unsorted |
# | **Binary Search**      | O(1) | O(log n) | O(log n) | Needs sorted      |
# | **Hashing (set/dict)** | O(1) | O(1)     | O(n)     | Fastest lookup    |
# | **Jump Search**        | O(1) | O(√n)    | O(√n)    | Sorted            |
# | **Exponential Search** | O(1) | O(log n) | O(log n) | Sorted            |

# SORTING ALGORITHMS (VERY IMPORTANT)
# | Algorithm          | Best       | Average    | Worst      | Stable | Notes               |
# | ------------------ | ---------- | ---------- | ---------- | ------ | ------------------- |
# | **Bubble Sort**    | O(n)       | O(n²)      | O(n²)      | ✅      | Simple but slow     |
# | **Selection Sort** | O(n²)      | O(n²)      | O(n²)      | ❌      | Less swaps          |
# | **Insertion Sort** | O(n)       | O(n²)      | O(n²)      | ✅      | Good for small data |
# | **Merge Sort**     | O(n log n) | O(n log n) | O(n log n) | ✅      | Divide & conquer    |
# | **Quick Sort**     | O(n log n) | O(n log n) | O(n²)      | ❌      | Fast but risky      |
# | **Heap Sort**      | O(n log n) | O(n log n) | O(n log n) | ❌      | No extra space      |
# | **Timsort**        | O(n)       | O(n log n) | O(n log n) | ✅      | Python uses this    |


a = [3, 1, 2]
a.sort()   # in-place
print(a)

a = [3, 1, 2]
b = sorted(a)

# | Algorithm         | In-place? |
# | ----------------- | --------- |
# | Bubble Sort       | ✅         |
# | Insertion Sort    | ✅         |
# | Selection Sort    | ✅         |
# | Quick Sort        | ✅         |
# | Heap Sort         | ✅         |
# | Merge Sort        | ❌         |
# | Python `sorted()` | ❌         |
# | Python `.sort()`  | ✅         |

# What is the default mode of open()?
# 'r'

# What happens if file does NOT exist and you open with 'r'?
# Error occurs

# Which mode creates file if not exists?
# 'w'

# What does 'a' mode do?
# Appends at end

# Which mode allows both read & write without deleting content?
# 'r+'

# What does read() return?
# string

# What does readlines() return?
# list of lines

f = open("file.txt", "w")
f.write("Hello\nWorld")
f.close()

f = open("file.txt", "r")
print(f.readline())
# Hello\n

# Which method moves cursor?
# seek()