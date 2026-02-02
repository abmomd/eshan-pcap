# Stack in Python – Procedural vs OOP Approach

## 1. Recap: Object Creation and Initialization

### Example Class

```python
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self, a, b):
        return a + b
```

**Key Points**
- self refers to the current object
- The first parameter of every instance method is always self

---

## 2. Object Creation vs Object Initialization

### Object Creation
- Allocation of memory for the object
- Handled internally by Python

### Object Initialization
- Assigning values to object variables
- Done using the `__init__()` method

### Example

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("John", 22)
```

**Steps Involved**
- Object of Student class is created
- `__init__()` method is called
- `Student.__init__(s1, "John", 22)`
- Attributes are initialized

---

## 3. `__new__()` vs `__init__()`

### `__new__()`
- Responsible for creating the object
- Returns the instance

### `__init__()`
- Responsible for initializing the object

```python
class BankAccount:
    def __new__(cls):
        instance = super().__new__(cls)
        return instance

    def __init__(self, balance):
        self.balance = balance
```

---

## 4. What is a Stack?

A Stack is a linear data structure that follows the **LIFO principle**  
Last In, First Out

### Operations on Stack
- push → Insert element
- pop → Remove top element
- peek → View top element
- is_empty → Check if stack is empty
- size → Number of elements

### Real Life Examples
- Stack of plates
- Undo / Redo operations
- Browser back button
- Function call stack

---

## 5. Stack Using Procedural Approach

```python
stack = []

def push(item):
    stack.append(item)

def pop():
    if not stack:
        print("Stack is empty")
    else:
        return stack.pop()

def peek():
    if not stack:
        print("Stack is empty")
    else:
        return stack[-1]
```

**Problems with Procedural Approach**
- No data security
- Global variable dependency
- Hard to manage for large programs
- No control over access

---

## 6. Why Shift to OOP Approach?

### Advantages of OOP
- Encapsulation
- Better organization
- Reusability
- Security
- Easier maintenance

---

## 7. Stack Using OOP Approach

### Why `stack_list` should be private
- Stack operations must be controlled
- Direct access can break LIFO order
- Prevents accidental modification
- Follows encapsulation

### Private variable in Python
- `self.__stack_list`
- Internally becomes `_Stack__stack_list`

---

## 8. Complete Stack Class

```python
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, item):
        self.__stack_list.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.__stack_list.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.__stack_list[-1]

    def is_empty(self):
        return len(self.__stack_list) == 0

    def stack_len(self):
        return len(self.__stack_list)
```

---

## 9. Using the Stack Class

```python
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Top element:", s.peek())
print("Stack size:", s.stack_len())

s.pop()
print("Stack size after pop:", s.stack_len())
```

**Output**
```
Top element: 30
Stack size: 3
Stack size after pop: 2
```

---

## 10. Key Takeaways
- Stack follows LIFO
- Procedural approach works but is unsafe
- OOP approach provides encapsulation and data security
- Private variables protect internal data
