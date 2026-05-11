# ⚠️ Built-in Python Exceptions – Complete Notes

Python provides many built-in exceptions to help programs detect and handle errors safely.

These exceptions are organized into a hierarchy from:

- Very general exceptions
- To very specific exceptions

Understanding them is extremely important for:

- PCAP certification
- Debugging
- Writing professional applications

---

# 🧠 1️⃣ What are Built-in Exceptions?

Built-in exceptions are predefined error classes provided by Python.

They are automatically raised when Python detects an error during execution.

---

# 🔥 Example

```python
print(10 / 0)
```

Raises:

```python
ZeroDivisionError
```

---

# 🧠 2️⃣ Abstract vs Concrete Exceptions

Python exceptions can be grouped into:

| Type | Meaning |
|------|---------|
| Abstract Exceptions | General categories |
| Concrete Exceptions | Specific errors |

---

# 🧠 3️⃣ Abstract Exceptions

Abstract exceptions are broad exception categories.

They usually are not raised directly.

Instead, their child exceptions are raised.

---

# 🔹 ArithmeticError

Handles arithmetic-related problems.

Child exceptions include:

- ZeroDivisionError
- OverflowError
- FloatingPointError

---

## ✅ Example

```python
try:
    print(10 / 0)

except ArithmeticError:
    print("Arithmetic problem occurred")
```

---

# 🔹 LookupError

Handles invalid lookup operations.

Child exceptions include:

- IndexError
- KeyError

---

## ✅ Example

```python
data = [1, 2, 3]

try:
    print(data[10])

except LookupError:
    print("Lookup failed")
```

---

# 🔹 BaseException

This is the MOST GENERAL exception in Python.

All exceptions ultimately inherit from:

```python
BaseException
```

---

# ⚠️ Important

Catching `BaseException` catches almost everything, including:

- KeyboardInterrupt
- SystemExit

Usually:

```python
except Exception:
```

is preferred instead.

---

# 🧠 4️⃣ Concrete Exceptions

Concrete exceptions represent specific errors.

---

# 🔹 AssertionError

Raised when:

```python
assert condition
```

fails.

---

## Example

```python
x = -1

assert x > 0
```

Raises:

```python
AssertionError
```

---

# 🔹 ImportError

Raised when importing fails.

---

## Example

```python
import unknown_module
```

Raises:

```python
ImportError
```

---

# 🔹 IndexError

Raised when invalid list index is used.

---

## Example

```python
numbers = [1, 2, 3]

print(numbers[10])
```

Raises:

```python
IndexError
```

---

# 🔹 KeyError

Raised when dictionary key is missing.

---

## Example

```python
student = {"name": "Alice"}

print(student["age"])
```

Raises:

```python
KeyError
```

---

# 🔹 KeyboardInterrupt

Raised when user interrupts program using:

```text
Ctrl + C
```

---

## Example

```python
try:
    while True:
        pass

except KeyboardInterrupt:
    print("Program interrupted safely")
```

---

# 🔹 MemoryError

Raised when Python runs out of memory.

---

## Example

```python
huge = [1] * (10**20)
```

May raise:

```python
MemoryError
```

---

# 🔹 OverflowError

Raised when result of calculation becomes too large.

---

## Example

```python
huge_value = 1E250 ** 2
```

May raise:

```python
OverflowError
```

---

# 🧠 5️⃣ Exception Hierarchy (Simplified)

```text
BaseException
 ├── Exception
      ├── ArithmeticError
      │     ├── OverflowError
      │     └── ZeroDivisionError
      │
      ├── LookupError
      │     ├── IndexError
      │     └── KeyError
      │
      ├── AssertionError
      ├── ImportError
      ├── MemoryError
      └── KeyboardInterrupt
```

---

# 🧪 Exercise 1

## Question

Which exception protects your code from keyboard interruption?

---

## ✅ Answer

```python
KeyboardInterrupt
```

---

## Example

```python
try:
    while True:
        pass

except KeyboardInterrupt:
    print("Stopped safely")
```

---

# 🧪 Exercise 2

## Question

What is the most general Python exception?

---

## ✅ Answer

```python
BaseException
```

---

# 🧪 Exercise 3

## Question

Which exception may occur here?

```python
huge_value = 1E250 ** 2
```

---

## ✅ Answer

```python
OverflowError
```

---

# 🧠 Real-Life Examples

---

# 🏦 Banking System

```python
try:
    amount = int(input("Enter amount: "))

except ValueError:
    print("Invalid amount")
```

---

# 📁 File Import System

```python
try:
    import payment_module

except ImportError:
    print("Module missing")
```

---

# 🎮 Game Inventory

```python
inventory = ["Sword", "Shield"]

try:
    print(inventory[5])

except IndexError:
    print("Item does not exist")
```

---

# 🚗 Car Navigation System

```python
locations = {
    "home": "Street A"
}

try:
    print(locations["office"])

except KeyError:
    print("Location not saved")
```

---

# ⚠️ Common Mistakes

| Mistake | Fix |
|--------|-----|
| Catching all exceptions blindly | Catch specific exceptions |
| Confusing IndexError and KeyError | Lists vs dictionaries |
| Using BaseException often | Use Exception instead |
| Ignoring KeyboardInterrupt | Handle safely in loops |

---

# 🚀 Best Practices

✅ Catch only expected exceptions  
✅ Keep try blocks small  
✅ Use meaningful error messages  
✅ Understand exception hierarchy  

---

# 🎯 Summary

- Python provides built-in exceptions
- Exceptions are organized hierarchically
- Abstract exceptions are broad categories
- Concrete exceptions represent specific errors
- `BaseException` is the most general exception
- Proper exception handling improves reliability

---

# 🧠 Final Thought

Programs fail.

Professional programs fail gracefully.

Understanding Python exceptions is one of the key skills that separates beginners from strong developers.