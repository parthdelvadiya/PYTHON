# Python Data Types Methods Cheat Sheet

# LIST METHODS

```python
nums = [1, 2, 3]
```

## append()

Add one element at end.

```python
nums.append(4)

# [1,2,3,4]
```

## extend()

Add multiple elements.

```python
nums.extend([5,6])

# [1,2,3,5,6]
```

## insert()

Insert at specific index.

```python
nums.insert(1,100)

# [1,100,2,3]
```

## remove()

Remove first occurrence.

```python
nums.remove(2)
```

## pop()

Remove and return element.

```python
nums.pop()
nums.pop(0)
```

## clear()

Remove all elements.

```python
nums.clear()
```

## index()

Find position.

```python
nums.index(3)
```

## count()

Count occurrences.

```python
nums.count(2)
```

## sort()

Sort ascending.

```python
nums.sort()
```

Descending:

```python
nums.sort(reverse=True)
```

## reverse()

Reverse list.

```python
nums.reverse()
```

## copy()

Create shallow copy.

```python
new_nums = nums.copy()
```

---

# TUPLE METHODS

```python
t = (1,2,2,3)
```

## count()

```python
t.count(2)
```

## index()

```python
t.index(3)
```

Tuple only has these 2 methods because it is immutable.

---

# SET METHODS

```python
s = {1,2,3}
```

## add()

```python
s.add(4)
```

## update()

```python
s.update([5,6])
```

## remove()

```python
s.remove(3)
```

Error if element missing.

## discard()

```python
s.discard(10)
```

No error if missing.

## pop()

```python
s.pop()
```

Removes random element.

## clear()

```python
s.clear()
```

## copy()

```python
new_set = s.copy()
```

## union()

```python
a = {1,2}
b = {2,3}

a.union(b)
```

Result:

```python
{1,2,3}
```

## intersection()

```python
a.intersection(b)
```

Result:

```python
{2}
```

## difference()

```python
a.difference(b)
```

Result:

```python
{1}
```

## symmetric_difference()

```python
a.symmetric_difference(b)
```

Result:

```python
{1,3}
```

## issubset()

```python
{1,2}.issubset({1,2,3})
```

## issuperset()

```python
{1,2,3}.issuperset({1,2})
```

## isdisjoint()

```python
{1,2}.isdisjoint({3,4})
```

---

# DICTIONARY METHODS

```python
student = {
    "name":"John",
    "age":25
}
```

## keys()

```python
student.keys()
```

## values()

```python
student.values()
```

## items()

```python
student.items()
```

## get()

```python
student.get("name")
```

Safe access.

## update()

```python
student.update({"city":"NY"})
```

## pop()

```python
student.pop("age")
```

## popitem()

```python
student.popitem()
```

Removes last key-value pair.

## setdefault()

```python
student.setdefault("marks",0)
```

## clear()

```python
student.clear()
```

## copy()

```python
student.copy()
```

## fromkeys()

```python
dict.fromkeys(["a","b"],0)
```

Output:

```python
{'a':0,'b':0}
```

---

# STRING METHODS

```python
s = "python programming"
```

## upper()

```python
s.upper()
```

## lower()

```python
s.lower()
```

## swapcase()

```python
s.swapcase()
```

## title()

```python
s.title()
```

## capitalize()

```python
s.capitalize()
```

## strip()

```python
" hello ".strip()
```

## lstrip()

```python
" hello".lstrip()
```

## rstrip()

```python
"hello ".rstrip()
```

## replace()

```python
s.replace("python","java")
```

## split()

```python
s.split()
```

## join()

```python
"-".join(["a","b","c"])
```

## find()

```python
s.find("pro")
```

## index()

```python
s.index("pro")
```

## startswith()

```python
s.startswith("python")
```

## endswith()

```python
s.endswith("ing")
```

## count()

```python
s.count("m")
```

## isalpha()

```python
"abc".isalpha()
```

## isdigit()

```python
"123".isdigit()
```

## isalnum()

```python
"abc123".isalnum()
```

## isspace()

```python
" ".isspace()
```

## islower()

```python
"abc".islower()
```

## isupper()

```python
"ABC".isupper()
```

---

# FILE METHODS

```python
file = open("data.txt")
```

## read()

```python
file.read()
```

## readline()

```python
file.readline()
```

## readlines()

```python
file.readlines()
```

## write()

```python
file.write("Hello")
```

## writelines()

```python
file.writelines(["A\n","B\n"])
```

## seek()

```python
file.seek(0)
```

## tell()

```python
file.tell()
```

## close()

```python
file.close()
```

---

# MOST IMPORTANT BUILT-IN FUNCTIONS

## len()

```python
len([1,2,3])
```

## type()

```python
type("abc")
```

## id()

```python
id(obj)
```

## max()

```python
max([1,2,3])
```

## min()

```python
min([1,2,3])
```

## sum()

```python
sum([1,2,3])
```

## sorted()

```python
sorted([3,1,2])
```

## zip()

```python
zip(a,b)
```

## enumerate()

```python
enumerate(lst)
```

## map()

```python
map(func,data)
```

## filter()

```python
filter(func,data)
```

## any()

```python
any([False,True])
```

## all()

```python
all([True,True])
```

## range()

```python
range(10)
```

## isinstance()

```python
isinstance(5,int)
```
