# Object Oriented Programming in Python (Introductory Notes)

---

## Imperative Programming

Imperative programming focuses on **how** a program operates by explicitly changing program state step by step.

```python
x = 10
x = x + 5
x = x * 2
x = x / 10

print(x)
```

---

## Procedural Programming

Procedural programming organizes code into reusable functions, but often relies on shared (global) state.

### Example: Simple Banking System

```python
balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount

def withdraw(amount):
    global balance
    balance = balance - amount

deposit(500)
withdraw(200)
print(balance)
```

### Problems with Procedural Approach
1. Global state is dangerous.
2. Functions can modify data unpredictably.
3. Hard to scale for large systems.

---

## What is Object Oriented Programming (OOP)?

Object Oriented Programming is a paradigm where we:
- Create a collection of **interacting objects**
- Each object:
  - Holds data (state)
  - Exposes behavior (methods)
  - Represents a real-world entity

---

## Components of OOP

1. Objects  
2. Classes  
3. Attributes  
4. Methods  
5. Interaction between objects  

---

## Classes and Objects

### Example: Bank Account

```python
class Bank:
    def __init__(self, balance):
        self.balance = balance

# Initial state
account1 = Bank(1000)

# State modification (identity remains same)
account1.balance = 3000
```

---

## Example: Counter Class

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c1 = Counter()
c1.increment()
```

- **State** → `count`
- **Behavior** → `increment()`

---

## Example: Mobile Phone

```python
class Phone:
    def __init__(self):
        self.battery = 50

    def call(self):
        self.battery -= 5

    def charge(self):
        self.battery += 50
```

---

## Object Interaction

Objects can:
- Call each other's methods
- Pass data
- Collaborate to complete tasks

### Example: Car and Engine

```python
class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
```

### Example: Student and Course

```python
class Course:
    def show_course(self):
        print("This is OOP")

class Student:
    def __init__(self):
        self.course = Course()

    def show_course(self):
        self.course.show_course()

s1 = Student()
s1.show_course()
```

---

## Object Equality vs Identity

- **Equality (`==`)** → compares values (state)
- **Identity (`is`)** → compares memory location

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True → same values
print(a is b)  # False → different objects
```

---

## Attributes

Attributes are variables associated with an object that describe its state.

- Created dynamically
- Belong to individual objects

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Eshan", 14)
s2 = Student("Ari", 14)
```

Internally stored as:

```text
{name: "Eshan", age: 14}
```

---

## Why `self` Exists?

`self` is a reference to the **current object**.
It allows instance methods to access and modify object data.

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

Behind the scenes:

```python
# s1 = Student("Eshan", 14)
Student.__init__(s1, "Eshan", 14)
```

---

## Summary

- OOP helps manage complexity by bundling data and behavior
- Objects model real-world entities
- Encapsulation avoids unsafe global state
- Interaction between objects enables scalable design

---
