# ⚠️ Advanced Exception Handling in Python – Complete Notes

This module covers advanced exception handling concepts including:

- Exception hierarchy
- Ordering of `except` blocks
- Raising exceptions manually
- `assert` statement
- Exception propagation

These concepts are extremely important for:

- PCAP certification
- Writing reliable programs
- Debugging professional applications

---

# 🧠 1️⃣ Exception Hierarchy in Python

All Python exceptions belong to a hierarchy.

At the very top is:

```python
BaseException
```

Below it are more general and more specific exceptions.

---

# 🔹 Simplified Hierarchy

```text
BaseException
 ├── Exception
      ├── ArithmeticError
      │     ├── ZeroDivisionError
      │     └── OverflowError
      │
      ├── LookupError
      │     ├── IndexError
      │     └── KeyError
      │
      ├── ValueError
      └── TypeError
```

---

# 🧠 Why Hierarchy Matters

A more general exception catches all its child exceptions.

Example:

```python
except ArithmeticError:
```

will catch:

- ZeroDivisionError
- OverflowError
- FloatingPointError

---

# 🧠 2️⃣ Ordering of except Blocks

## ✅ Important Rule

Always place:

- More specific exceptions FIRST
- More general exceptions LATER

---

# ✅ Correct Order

```python
try:
    risky_code()

except IndexError:
    print("Index issue")

except LookupError:
    print("General lookup issue")
```

---

# ❌ Wrong Order

```python
try:
    risky_code()

except LookupError:
    print("General lookup issue")

except IndexError:
    print("This block is useless")
```

---

# ⚠️ Why?

Because:

```python
LookupError
```

already catches:

```python
IndexError
```

So Python never reaches the second block.

---

# 🧠 3️⃣ Anonymous except Block

An unnamed `except:` catches every remaining exception.

---

## ✅ Correct Usage

```python
try:
    risky_code()

except ValueError:
    print("Value error")

except:
    print("Other error")
```

---

## ⚠️ Important Rule

Only ONE anonymous `except:` is allowed, and it must be LAST.

---

# ❌ Invalid

```python
try:
    risky_code()

except:
    print("Error")

except:
    print("Another error")
```

---

# 🧠 4️⃣ raise Statement

Python allows you to raise exceptions manually.

---

## 🔹 Syntax

```python
raise ExceptionName
```

---

# ✅ Example

```python
age = -5

if age < 0:
    raise ValueError
```

---

# 🧠 Real-Life Use

Useful for:

- Validation
- Security checks
- Business rules
- Defensive programming

---

# 🧠 5️⃣ Re-Raising Exceptions

Inside an `except` block:

```python
raise
```

re-raises the currently handled exception.

---

# ✅ Example

```python
try:
    print(1 / 0)

except ZeroDivisionError:
    print("Logging error...")
    raise
```

---

# ⚠️ Result

- Exception is partially handled
- Then raised again

Useful for:

- Logging systems
- Debugging frameworks

---

# 🧠 6️⃣ assert Statement

The `assert` statement checks whether a condition is True.

If condition is False:

```python
AssertionError
```

is raised automatically.

---

# 🔹 Syntax

```python
assert condition
```

---

# ✅ Example

```python
x = 10

assert x > 0
```

---

# ❌ Example

```python
x = -5

assert x > 0
```

Raises:

```python
AssertionError
```

---

# 🧠 Why assert is Useful

Assertions help protect:

- Critical assumptions
- Internal logic
- Dangerous operations

---

# 🧠 Real-Life Example – Banking System

```python
balance = 5000
withdraw = 10000

assert withdraw <= balance
```

Stops invalid transaction immediately.

---

# 🧪 Exercise 1

## Code

```python
try:
    print(1/0)

except ZeroDivisionError:
    print("zero")

except ArithmeticError:
    print("arith")

except:
    print("some")
```

---

## ✅ Output

```python
zero
```

---

## 🧠 Why?

- `1/0` raises:
  ```
  ZeroDivisionError
  ```
- First matching except executes
- Remaining blocks skipped

---

# 🧪 Exercise 2

## Code

```python
try:
    print(1/0)

except ArithmeticError:
    print("arith")

except ZeroDivisionError:
    print("zero")

except:
    print("some")
```

---

## ✅ Output

```python
arith
```

---

## 🧠 Why?

Because:

```python
ZeroDivisionError
```

inherits from:

```python
ArithmeticError
```

So the first block already catches it.

Second block becomes unreachable logically.

---

# 🧪 Exercise 3

## Code

```python
def foo(x):
    assert x
    return 1/x


try:
    print(foo(0))

except ZeroDivisionError:
    print("zero")

except:
    print("some")
```

---

## ✅ Output

```python
some
```

---

## 🧠 Why?

```python
assert x
```

fails because:

```python
x = 0
```

Zero is treated as False.

So:

```python
AssertionError
```

is raised BEFORE division occurs.

Since:

```python
AssertionError
```

is NOT:

```python
ZeroDivisionError
```

control goes to anonymous `except`.

---

# 🧠 Important Truthy/Falsy Values

Falsy values:

```python
0
0.0
''
[]
{}
None
False
```

All of them fail assertions.

---

# ⚠️ Common Mistakes

| Mistake | Fix |
|--------|-----|
| General except before specific | Reverse order |
| Multiple anonymous except blocks | Only one allowed |
| Using bare except everywhere | Catch specific exceptions |
| Confusing assert with if | assert raises exception |

---

# 🚀 Real-Life Examples

---

# 🏦 Banking Validation

```python
amount = -100

if amount < 0:
    raise ValueError("Negative amount")
```

---

# 🚗 Car Speed Monitoring

```python
speed = 250

assert speed <= 180
```

---

# 🧑‍💻 Login Security

```python
password = ""

assert password != ""
```

---

# 🎯 Summary

- Python exceptions form a hierarchy
- More specific exceptions must come first
- `raise` creates exceptions manually
- `raise` without name re-raises current exception
- `assert` validates assumptions
- Anonymous `except:` catches remaining exceptions

---

# 🧠 Final Thought

Good programmers write code that works.

Great programmers write code that:

- Detects failures
- Prevents corruption
- Handles unexpected situations safely

Advanced exception handling is one of the tools that makes this possible.