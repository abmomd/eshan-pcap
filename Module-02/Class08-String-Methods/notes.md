# 🧵 Python Strings – Complete Notes

Python strings are one of the most commonly used data types.  
They are **immutable sequences of characters**, meaning once a string is created, its contents cannot be changed.

Strings support many operations similar to other sequences like lists and tuples.

---

# 1️⃣ Types of Strings in Python

There are **two types of strings**.

## 🔹 One-Line Strings

These are enclosed in:

```
'string'
```

or

```
"string"
```

Example:

```python
name = "Alice"
message = 'Hello World'
```

---

## 🔹 Multi-Line Strings

Multi-line strings span multiple lines and are enclosed using **triple quotes**.

```
'''string'''
```

or

```
"""string"""
```

Example:

```python
text = """
Python is a powerful
programming language.
"""
```

These are commonly used for:

- Documentation
- Long messages
- SQL queries

---

# 2️⃣ String Length

The **length of a string** is calculated using:

```
len()
```

Example:

```python
print(len("Python"))
```

Output:

```
6
```

---

### Escape Characters

Escape sequences are counted as characters.

Example:

```python
print(len("\n\n"))
```

Output:

```
2
```

Here:

```
\n
```

represents a newline character.

---

# 3️⃣ String Operations

## 🔹 Concatenation

Strings can be joined using the `+` operator.

Example:

```python
first = "Hello"
second = "World"
print(first + " " + second)
```

Output:

```
Hello World
```

---

## 🔹 Replication

Strings can be repeated using `*`.

Example:

```python
asterisk = '*'
plus = '+'

decoration = (asterisk + plus) * 4 + asterisk
print(decoration)
```

Output:

```
*+*+*+*+*
```

---

# 4️⃣ Character Code Functions

Python provides two important functions.

## 🔹 ord()

Returns the Unicode code point of a character.

```python
print(ord('A'))
```

Output:

```
65
```

---

## 🔹 chr()

Returns the character for a given Unicode code point.

```python
print(chr(65))
```

Output:

```
A
```

---

### Important Identity

These expressions are always true:

```
chr(ord(character)) == character
ord(chr(codepoint)) == codepoint
```

---

# 5️⃣ Useful String Functions

## 🔹 Convert string into list

```python
print(list("Python"))
```

Output:

```
['P','y','t','h','o','n']
```

---

## 🔹 max()

Returns character with **highest Unicode value**.

```python
print(max("Python"))
```

---

## 🔹 min()

Returns character with **lowest Unicode value**.

```python
print(min("Python"))
```

---

# 6️⃣ Finding Substrings

## 🔹 index()

Finds the position of a substring.

```python
text = "Python Programming"
print(text.index("Program"))
```

Output:

```
7
```

If substring is not found, it raises an error.

---

# 7️⃣ Important String Methods

## Case Conversion

| Method | Description |
|------|-------------|
| `capitalize()` | First letter uppercase |
| `lower()` | Convert to lowercase |
| `upper()` | Convert to uppercase |
| `swapcase()` | Swap case |
| `title()` | Capitalize each word |

Example:

```python
text = "python programming"
print(text.title())
```

Output:

```
Python Programming
```

---

## String Formatting

### center()

Centers text in a field.

```python
print("Python".center(20,'-'))
```

---

### join()

Joins elements of list/tuple.

```python
words = ['I','love','Python']
print(" ".join(words))
```

Output:

```
I love Python
```

---

### split()

Splits string into list.

```python
sentence = "Python is fun"
print(sentence.split())
```

Output:

```
['Python','is','fun']
```

---

## Removing Spaces

| Method | Description |
|------|-------------|
| `strip()` | Remove both sides spaces |
| `lstrip()` | Remove left spaces |
| `rstrip()` | Remove right spaces |

Example:

```python
text = "   Python   "
print(text.strip())
```

---

## Replace Text

```python
text = "I like Java"
print(text.replace("Java","Python"))
```

Output:

```
I like Python
```

---

# 8️⃣ String Checking Methods

These methods return **Boolean values**.

| Method | Meaning |
|------|---------|
| `isalnum()` | Letters or numbers |
| `isalpha()` | Only letters |
| `islower()` | All lowercase |
| `isupper()` | All uppercase |
| `isspace()` | Only spaces |
| `startswith()` | Starts with substring |
| `endswith()` | Ends with substring |

Example:

```python
print("Python".isalpha())
```

Output:

```
True
```

---

