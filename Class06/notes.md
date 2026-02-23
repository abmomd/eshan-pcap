# 🧬 Inheritance in Python  


---

# 📘 1. What is Inheritance?

## 🔎 Core Idea

Inheritance is one of the **four pillars of Object-Oriented Programming (OOP)**:

- Encapsulation  
- Abstraction  
- Inheritance  
- Polymorphism  

### 🧠 Definition

Inheritance allows a class (child/subclass) to acquire:
- Methods
- Variables
- Behavior

from another class (parent/superclass).

---

## 🎯 Why Use Inheritance?

Instead of rewriting common functionality, we reuse it.

### 🔎 Real-Life Example

Consider:

- Person  
    - Student  
    - Teacher  
    - Staff  

All share:
- name
- id
- introduction method

So we create a base class:

```python
class Person:
    pass
```

And derive others from it.

---

## 🏗 Syntax

```python
class ChildClass(ParentClass):
    pass
```

---

# 🖨 2. The `__str__()` Method – Object Representation

## 📘 Theory

- `__str__()` is a special method (magic/dunder method).
- It defines how an object is converted to a readable string.
- It is automatically called when:
  - `print(object)` is used
  - `str(object)` is used

If not defined, Python prints something like:

```
<__main__.ClassName object at 0x...>
```

Which is not user-friendly.

---

## 🔎 Real-Life Analogy

It is like a person introducing themselves.

---

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"

p = Person("Ashraf")
print(p)
```

---

## 🧠 PCAP Tip

- `__str__()` improves readability.
- It must return a string.
- If it returns anything else → TypeError.

---

# 🧬 3. `issubclass()` – Class Relationship Checker

## 📘 Theory

Syntax:

```python
issubclass(ClassA, ClassB)
```

Returns:
- True if ClassA inherits from ClassB
- False otherwise

It checks **class hierarchy**, not objects.

---

## 🔎 Real-Life Example

Dog is a type of Animal.

```python
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))  # True
```

---

## 🧠 Important

- A class is considered a subclass of itself.
- Works only with classes, not objects.

---

# 🧍 4. `isinstance()` – Object Type Checker

## 📘 Theory

Syntax:

```python
isinstance(object, Class)
```

Checks whether:
- Object belongs to a class
- OR belongs to its parent class

---

## 🔎 Real-Life Example

A student is also a person.

```python
class Person:
    pass

class Student(Person):
    pass

s = Student()

print(isinstance(s, Student))  # True
print(isinstance(s, Person))   # True
```

---

## 🧠 Difference from `issubclass()`

| Function | Works On | Checks |
|----------|----------|--------|
| issubclass() | Classes | Inheritance |
| isinstance() | Objects | Object type |

---

# 🪞 5. The `is` Operator – Identity Comparison

## 📘 Theory

`is` checks:
- Memory location
- Object identity

It does NOT check equality of values.

---

## 🔎 Example

```python
class Student:
    pass

s1 = Student()
s2 = Student()
s3 = s1

print(s1 is s2)  # False
print(s1 is s3)  # True
```

---

## 🧠 Exam Insight

| Operator | Checks |
|----------|--------|
| == | Value equality |
| is | Identity (same object) |

---

# ⬆ 6. `super()` – Accessing Parent Class

## 📘 Theory

`super()` returns a reference to the nearest parent class.

Used for:
- Calling parent methods
- Extending parent functionality
- Avoiding duplicate code

---

## 🔎 Real-Life Example

Child adds extra behavior but still uses parent behavior.

```python
class Employee:
    def __str__(self):
        return "Employee"

class Manager(Employee):
    def __str__(self):
        return "Manager -> " + super().__str__()

m = Manager()
print(m)
```

---

## 🧠 Why Use `super()`?

Without it, we must manually write parent class name.

Bad practice:

```python
Employee.__str__(self)
```

Good practice:

```python
super().__str__()
```

---

# 🧑‍🤝‍🧑 7. Inheriting Methods and Variables

## 📘 Theory

A subclass automatically inherits:
- Instance variables
- Class variables
- Methods

Unless overridden.

---

## 🔎 Example

```python
class Employee:
    population = 0

    def __init__(self, name):
        self.name = name
        Employee.population += 1

    def greet(self):
        return f"Hello, I am {self.name}"

class Developer(Employee):
    pass

d = Developer("Aman")
print(d.greet())
print(Employee.population)
```

---

## 🧠 Key Idea

- Class variables are shared among all instances.
- Instance variables belong to each object.

---

# 🔍 8. Attribute Lookup Order (Very Important for PCAP)

## 📘 Theory

When accessing:

```python
obj.attribute
```

Python searches in this order:

1. Object’s namespace  
2. Class namespace  
3. Parent class  
4. Grandparent class  
5. Left-to-right (in multiple inheritance)  
6. If not found → AttributeError  

---

## 🔎 Example

```python
class A:
    def say(self):
        return "A"

class B(A):
    pass

b = B()
print(b.say())
```

Python finds `say()` inside class A.

---

# 🔄 9. Method Overriding

## 📘 Theory

If a subclass defines a method with the same name as parent:
- The child version replaces the parent version.

This is called **method overriding**.

---

## 🔎 Example

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

d = Dog()
print(d.speak())
```

---

## 🧠 Important

- Parent method is hidden, not deleted.
- Can still be accessed using `super()`.

---

# 🧠 10. Combined Example (PCAP Style)

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    def __str__(self):
        return f"Person: {self.name}"

class Teacher(Person):
    def __str__(self):
        return "Teacher -> " + super().__str__()

class Student(Person):
    pass

t = Teacher("Mr. Khan")
s = Student("Aisha")

print(t)
print(s)
print(isinstance(s, Person))
print(issubclass(Teacher, Person))
print(t is s)
print(Person.population)
```

---

# 📌 PCAP Exam Quick Revision Table

| Concept | Key Point |
|----------|------------|
| Inheritance | Reuse code |
| `__str__()` | Readable object output |
| `issubclass()` | Class relationship |
| `isinstance()` | Object type check |
| `is` | Identity check |
| `super()` | Call parent method |
| Overriding | Replace parent behavior |
| Lookup Order | Object → Class → Parent |

---

# 🎯 Why Inheritance Matters

Inheritance gives:

- Code reuse  
- Logical structure  
- Real-world modeling  
- Polymorphism support  
- Scalable design  

---


