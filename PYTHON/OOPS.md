# Four Pillars of OOPs in Python

# 1. Encapsulation

Encapsulation means wrapping data and methods into a single unit (class) and restricting direct access.

Example:

```python id="o7g4c5"
class Student:

    def __init__(self):
        self.__marks = 90   # private variable

    def show_marks(self):
        print(self.__marks)

s = Student()

s.show_marks()
```

Why?

* Protects data
* Prevents accidental modification

---

# 2. Inheritance

Inheritance means one class can use properties and methods of another class.

Example:

```python id="1kj0x4"
class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()

d.sound()
```

Output:

```python id="x8g2s6"
Animal makes sound
```

Why?

* Code reuse
* Less duplication

---

# 3. Polymorphism

Polymorphism means same method name behaves differently for different objects.

Example:

```python id="q4s8l9"
class Dog:
    
    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()
```

Output:

```python id="4h7m2k"
Bark
Meow
```

Why?

* Flexibility
* Same interface for multiple objects

---

# 4. Abstraction

Abstraction means hiding internal implementation and showing only important details.

Example:

```python id="j3v5n1"
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")

c = Car()

c.start()
```

Why?

* Hides complexity
* Improves security

---

# Quick Summary

| Pillar        | Meaning                         |
| ------------- | ------------------------------- |
| Encapsulation | Data hiding                     |
| Inheritance   | Reusing code                    |
| Polymorphism  | Same method, different behavior |
| Abstraction   | Hiding implementation details   |

---