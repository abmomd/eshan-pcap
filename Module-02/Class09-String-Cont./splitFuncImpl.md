# 🧩 Custom String Split Function – Medium Level

## 🎯 Objectives

- Improve your understanding of **string manipulation**
- Practice working with **loops and conditions**
- Learn how built-in methods like `split()` work internally

---

## 📘 Scenario

You already know how Python’s built-in `split()` method works.

Now it's time to **implement your own version** of it.

---

## 🛠 Task

Write a function named:

```
mysplit()
```

### 🔹 Function Requirements

Your function must:

- Accept exactly **one argument** → a string
- Return a **list of words**
- Words must be separated based on **whitespace characters**
- Handle edge cases correctly

---

## ⚙️ Rules

Your function should behave like `split()` with respect to spaces:

- Ignore multiple spaces
- Ignore leading and trailing spaces
- Do NOT use Python's built-in `split()` method

---

## 🚨 Edge Cases

Your function must handle:

- Empty string → return `[]`
- String with only spaces → return `[]`
- Single word → return list with one element

---

## 🧪 Test Cases

Your function should produce the following outputs:

```python
print(mysplit("To be or not to be, that is the question"))
```

Output:

```
['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
```

---

```python
print(mysplit("To be or not to be,that is the question"))
```

Output:

```
['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
```

---

```python
print(mysplit("   "))
```

Output:

```
[]
```

---

```python
print(mysplit("abc"))
```

Output:

```
['abc']
```

---

```python
print(mysplit(""))
```

Output:

```
[]
```

---

 how Python internally processes strings and builds lists of words without relying on built-in shortcuts.