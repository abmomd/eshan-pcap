# 🚨 Exception Handling in Python 

This module explains advanced exception handling concepts required for PCAP and real-world programming.

We will cover:

- `try`
- `except`
- `else`
- `finally`
- Exception objects
- Custom exception classes
- Extending built-in exceptions

---

# 🧠 1️⃣ try–except–else–finally Structure

## 🔹 Basic Structure

```python
try:
    # risky code
except SomeException:
    # handle error
else:
    # runs if no exception
finally:
    # always runs
```

---

# 🔹 else Block

### ✅ Key Rule:
The `else:` block runs **only if no exception occurs inside the try block.**

### 📌 Real-Life Analogy:
Imagine you are transferring money online:

- Try → Attempt transaction
- Except → Handle failure
- Else → Show success message
- Finally → Close session/log out

---

### Example

```python
import math

try:
    print(math.sqrt(9))
except ValueError:
    print("inf")
else:
    print("fine")
```

### Output:
```
3.0
fine
```

Why?

- `sqrt(9)` works.
- No exception.
- `else` executes.

---

# 🔹 finally Block

### ✅ Key Rule:
The `finally:` block **always executes**, whether exception occurs or not.

It is used for:

- Closing files
- Closing database connections
- Releasing resources
- Logging

---

### Example

```python
import math

try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("fine")
finally:
    print("the end")
```

### Output:
```
inf
the end
```

Why?

- `sqrt(-9)` raises `ValueError`
- except block runs
- else is skipped
- finally runs ALWAYS

---

# 🧠 2️⃣ Exception Objects & `as`

## 🔹 Syntax

```python
except ExceptionName as e:
```

This captures the exception object.

The exception object contains:

- `args` → tuple of arguments passed to exception
- message details

---

### Example

```python
try:
    raise ValueError("Invalid input", 404)
except ValueError as e:
    print(e.args)
```

Output:
```
('Invalid input', 404)
```

---

# 🧠 3️⃣ Extending Exception Classes

You can create your own exception by inheriting from built-in exceptions.

### Example

```python
class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)

try:
    raise NewValueError("Enemy warning", "Red alert", "High readiness")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')
```

### Output:
```
Enemy warning! Red alert! High readiness! 
```

### Why?

Because:
- `ValueError` stores constructor arguments inside `.args`
- The custom exception inherits that behavior

---

# 🏥 Real-Life Example 1 – ATM Withdrawal System

Write a program that:

- Tries to withdraw money
- Raises `ValueError` if amount is negative
- Uses:
  - `else` to confirm successful withdrawal
  - `finally` to display "Transaction complete"

---

# 🏦 Real-Life Example 2 – Bank Account with Custom Exception

Create:

```python
class InsufficientFundsError(Exception):
    pass
```

Raise this error if withdrawal > balance.

Catch it using:

```python
except InsufficientFundsError as e:
```

Print the message from `e.args`.

---

# ✈️ Real-Life Example 3 – Airline Booking System

Create a custom exception:

```python
class SeatUnavailableError(Exception):
    pass
```

If seat number is already booked:

- Raise exception
- Catch it
- Print message
- Always print "Session closed" using `finally`

---

# 🧠 Exercise Solutions

---

## ✅ Exercise 1

```python
import math

try:
    print(math.sqrt(9))
except ValueError:
    print("inf")
else:
    print("fine")
```

### Output:
```
3.0
fine
```

---

## ✅ Exercise 2

```python
import math

try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("fine")
finally:
    print("the end")
```

### Output:
```
inf
the end
```

---

## ✅ Exercise 3

```python
class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)

try:
    raise NewValueError("Enemy warning", "Red alert", "High readiness")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')
```

### Output:
```
Enemy warning! Red alert! High readiness! 
```

---

# 🔥 Advanced Real-Life Practice Questions

---

## 🧩 Question 1 – Online Login System

Design a login system:

- Raise `ValueError` if username is empty
- Raise `PermissionError` if password is wrong
- Use:
  - `else` to print "Login successful"
  - `finally` to print "Session ended"

Predict output for different scenarios.

---

## 🧩 Question 2 – File Handling System

Simulate:

- Try opening a file
- Catch `FileNotFoundError`
- Use `else` to print file content
- Use `finally` to print "File closed"

Explain execution flow.

---

## 🧩 Question 3 – Custom Medical Alert System

Create:

```python
class CriticalHealthError(Exception):
    pass
```

If heart rate > 180:

- Raise exception
- Catch it using `as`
- Print all arguments stored in `.args`
- Use finally to print "Monitoring continues"

---

# 📌 Summary Table

| Block | When It Runs |
|-------|--------------|
| try | Code that may fail |
| except | When exception occurs |
| else | When NO exception occurs |
| finally | ALWAYS runs |

---

# 🎯 PCAP Important Points

- `else` runs only if no exception
- `finally` always executes
- `.args` stores constructor arguments
- Custom exceptions inherit behavior
- You can extend built-in exceptions

---

# 🚀 Final Thought

Exception handling makes your programs:

- Safe
- Robust
- Professional
- Real-world ready

Mastering this helps in:

- PCAP exam
- Interviews
- Production systems
- Debugging large applications

---

