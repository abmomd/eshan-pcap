# 🔤 String Comparison & Conversion – Complete Notes

This module covers:

- String comparison rules
- Sorting strings
- Type conversion (string ↔ number)
- Common pitfalls in Python

---

# 🧠 1️⃣ String Comparison in Python

Strings can be compared using:

```
==  !=  >  <  >=  <=
```

---

## 🔹 How Comparison Works

Python compares strings **character by character** using **Unicode (ASCII) values**.

Example:

```python
print(ord('A'))  # 65
print(ord('a'))  # 97
```

So:

```
'A' < 'a'
```

---

## 🔹 Important Rules

### ✅ Rule 1: Case matters

Uppercase letters come before lowercase letters.

```
"Apple" < "apple"
```

---

### ✅ Rule 2: Comparison is lexicographical

Compare character by character:

```
"cat" > "car"
```

Because:
- 'c' = 'c'
- 'a' = 'a'
- 't' > 'r'

---

### ⚠️ Rule 3: String vs Number

- `"abc" == 123` → False  
- `"abc" != 123` → True  
- `"abc" > 123` → ❌ ERROR (TypeError)

---

# 🧪 Exercise 1

Which are TRUE?

---

### 🔸 1. `'smith' > 'Smith'`

Compare first letters:

```
's' (115) > 'S' (83)
```

✅ True

---

### 🔸 2. `'Smiths' < 'Smith'`

Compare:

```
Smith vs Smith
```

Then:

```
'S' == 'S'
...
```

But:

- "Smith" ends earlier
- Longer string is considered **greater**

So:

```
'Smiths' > 'Smith'
```

❌ False

---

### 🔸 3. `'Smith' > '1000'`

Compare first characters:

```
'S' (83) > '1' (49)
```

✅ True

---

### 🔸 4. `'11' < '8'`

Compare:

```
'1' (49) < '8' (56)
```

So:

```
'11' < '8'
```

✅ True

---

## ✅ Final Answers

```
True
False
True
True
```

---

# 🧠 2️⃣ Sorting Strings

There are two ways:

---

## 🔹 sorted()

- Returns a **new sorted list**

```python
words = ["banana", "apple", "cherry"]
print(sorted(words))
```

---

## 🔹 sort()

- Sorts the list **in-place**

```python
words.sort()
```

---

## 🔹 Sorting Rule

Sorting is based on **Unicode values**

So:

```
'A' < 'a'
```

---

# 🧪 Exercise 2

```python
s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])
```

---

### Step 1: Split

```
['Where','are','the','snows','of','yesteryear?']
```

---

### Step 2: Sort

ASCII order:

```
['Where', 'are', 'of', 'snows', 'the', 'yesteryear?']
```

Why?

- 'W' (87) comes before lowercase letters

---

### Step 3: Output

```
s3[1] → 'are'
```

---

## ✅ Final Answer

```
are
```

---

# 🧠 3️⃣ Type Conversion

---

## 🔹 Number → String

```python
x = 100
s = str(x)
```

---

## 🔹 String → Number

```python
int("123")     # 123
float("12.5")  # 12.5
```

---

### ⚠️ Important

Invalid conversion raises error:

```python
int("abc")  # ValueError
```

---

# 🧪 Exercise 3

```python
s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)
```

---

### Step 1

```
s1 = "12.8"
```

---

### Step 2

```python
i = int(s1)
```

❌ ERROR → cannot convert `"12.8"` to int directly

---

## ⚠️ Important Insight

This code will **raise an exception**:

```
ValueError: invalid literal for int()
```

---

## ✅ Final Answer

```
Runtime Error (ValueError)
```

---

# 🔥 Key Pitfalls

| Mistake | Why |
|--------|-----|
| `"10" > "2"` | String comparison, not numeric |
| `int("12.8")` | Invalid conversion |
| Sorting strings | Based on ASCII, not meaning |

---

# 🎯 Summary

- String comparison is **lexicographical**
- Case matters (`A < a`)
- Strings and numbers cannot be compared directly
- Sorting uses Unicode values
- `str()` converts number → string
- `int()` / `float()` convert string → number
- Invalid conversion → exception

---
