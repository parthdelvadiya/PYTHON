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