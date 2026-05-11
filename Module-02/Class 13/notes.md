# ⚠️ Exception Handling in Python – Complete Notes

Exception handling is one of the most important concepts in Python programming.

It allows programs to:

- Handle errors gracefully
- Prevent crashes
- Continue execution safely
- Improve reliability and user experience

---

# 🧠 1️⃣ What is an Exception?

An **exception** is an event that occurs during program execution which interrupts the normal flow of the program.

Exceptions usually occur because of:

- Invalid input
- Division by zero
- File not found
- Invalid type conversion
- Accessing invalid indexes
- Mathematical errors

---

## 🔥 Example

```python
print(10 / 0)
```

### Output

```python
ZeroDivisionError
```

The program crashes because the exception is not handled.

---

# 🛡 2️⃣ Why Exception Handling is Important

Without exception handling:

- Programs terminate unexpectedly
- Users see ugly error messages
- Data may be lost

With exception handling:

- Programs recover safely
- Errors are managed properly
- User experience improves

---

# 🧠 3️⃣ Basic try-except Structure

## 🔹 Syntax

```python
try:
    # risky code
except:
    # error handling
```

---

## 🔹 Execution Flow

1. Python executes the `try` block
2. If no error occurs:
   - `except` block is skipped
3. If exception occurs:
   - Python jumps to `except`

---

## ✅ Example

```python
try:
    number = int(input("Enter a number: "))
    print(100 / number)
except:
    print("Something went wrong!")
```

---

# 🧠 4️⃣ Real-Life Analogy

Imagine driving a car:

- `try` → Driving normally
- `except` → Airbags activate during accident
- Program continues safely

---

# 🧠 5️⃣ Handling Specific Exceptions

Different errors should be handled differently.

Python allows multiple `except` blocks.

---

## 🔹 Syntax

```python
try:
    # risky code
except ExceptionType1:
    # handle first error
except ExceptionType2:
    # handle second error
```

---

# ✅ Example

```python
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Invalid number entered.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 🧠 Important Rule

Only ONE matching `except` block executes.

---

# 🧪 Example

```python
try:
    print(10 / 0)

except ValueError:
    print("Value Error")

except ZeroDivisionError:
    print("Division by zero")
```

### Output

```python
Division by zero
```

---

# 🧠 6️⃣ Anonymous except Block

You can add a final unnamed `except:` block.

It catches all remaining exceptions.

---

## 🔹 Syntax

```python
try:
    # risky code

except ValueError:
    # specific handling

except:
    # catches everything else
```

---

# ⚠️ Important Rule

Anonymous `except:` must always come LAST.

---

# ❌ Wrong

```python
try:
    pass

except:
    print("All errors")

except ValueError:
    print("Value Error")
```

This causes:

```python
SyntaxError
```

---

# ✅ Correct

```python
try:
    pass

except ValueError:
    print("Value Error")

except:
    print("All other errors")
```

---

# 🧠 7️⃣ Program Flow After Exception

After handling exception:

- Program continues normally
- Execution resumes after try-except block

---

## ✅ Example

```python
print("Start")

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Handled error")

print("Program continues")
```

### Output

```python
Start
Handled error
Program continues
```

---

# 🧠 8️⃣ Common Python Exceptions

| Exception | Cause |
|----------|------|
| `ValueError` | Invalid value |
| `TypeError` | Wrong data type |
| `ZeroDivisionError` | Division by zero |
| `IndexError` | Invalid index |
| `KeyError` | Missing dictionary key |
| `FileNotFoundError` | File missing |
| `AttributeError` | Invalid attribute |

---

# 🧪 Real-Life Examples

---

# 🏦 Example 1 – ATM Withdrawal

```python
try:
    amount = int(input("Enter withdrawal amount: "))
    balance = 5000

    if amount > balance:
        print("Insufficient balance")
    else:
        print("Transaction successful")

except ValueError:
    print("Please enter a valid amount.")
```

---

# 📁 Example 2 – File Reader

```python
try:
    file = open("data.txt")
    print(file.read())

except FileNotFoundError:
    print("File does not exist.")
```

---

# 🔐 Example 3 – Login System

```python
try:
    age = int(input("Enter age: "))

    if age < 18:
        print("Access denied")
    else:
        print("Access granted")

except ValueError:
    print("Age must be a number.")
```

---

# 🧪 Practice Questions

---

## 🔹 Question 1

What will happen?

```python
try:
    print(int("abc"))
except ValueError:
    print("Invalid conversion")
```

---

## 🔹 Question 2

What is the output?

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Math Error")

print("Done")
```

---

## 🔹 Question 3

Why is this wrong?

```python
try:
    pass

except:
    print("All errors")

except ValueError:
    print("Value Error")
```

---

# ⚠️ Common Mistakes

| Mistake | Fix |
|--------|-----|
| Using bare except everywhere | Catch specific exceptions |
| Wrong except order | General except must be last |
| Ignoring exceptions silently | Print useful message |
| Large try blocks | Keep try blocks small |


---

# 🎯 Summary

- Exceptions prevent normal execution
- `try` contains risky code
- `except` handles errors
- Multiple exceptions can be handled separately
- Anonymous `except:` catches remaining errors
- Programs continue after exception handling

---

# 🧠 Final Thought

Professional software is not software without bugs.

Professional software is software that:

- Detects problems
- Handles failures safely
- Continues running gracefully

That is exactly what exception handling provides.