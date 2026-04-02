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