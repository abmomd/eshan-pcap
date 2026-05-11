# 🔁 Palindrome Checker – Solution

---

## ✅ Approach Overview

To solve this problem, we must:

1. Normalize the input:
   - Convert to lowercase
   - Remove spaces
2. Handle edge case (empty string)
3. Compare string with its reverse

---

# 🧠 Method 1 – Using Slicing (Simplest)

## ✅ Code

```python
text = input("Enter text: ")

# Normalize
cleaned = text.lower().replace(" ", "")

# Check empty string
if len(cleaned) == 0:
    print("It's not a palindrome")
elif cleaned == cleaned[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
```

---

## 🧠 Explanation

- `lower()` → ignore case
- `replace(" ", "")` → remove spaces
- `[::-1]` → reverse string
- Compare both

---

# 🧠 Method 2 – Using Two-Pointer Technique (Interview Style)

## ✅ Code

```python
text = input("Enter text: ")

cleaned = text.lower().replace(" ", "")

if len(cleaned) == 0:
    print("It's not a palindrome")
else:
    left = 0
    right = len(cleaned) - 1
    is_palindrome = True

    while left < right:
        if cleaned[left] != cleaned[right]:
            is_palindrome = False
            break
        left += 1
        right -= 1

    if is_palindrome:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
```

---

## 🧠 Why This Method Matters

- Does NOT use slicing
- More memory efficient
- Common in interviews

---

# 🧠 Method 3 – Ignoring Punctuation (Advanced)

## ✅ Code

```python
text = input("Enter text: ")

cleaned = ""

for ch in text:
    if ch.isalpha():
        cleaned += ch.lower()

if len(cleaned) == 0:
    print("It's not a palindrome")
elif cleaned == cleaned[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
```

---

## 🧠 Explanation

- Keeps only alphabet characters
- Removes spaces and punctuation automatically

---

# 🧪 Example Run

### Input

```
Ten animals I slam in a net
```

### Output

```
It's a palindrome
```

---

### Input

```
Eleven animals I slam in a net
```

### Output

```
It's not a palindrome
```

---

# ⚠️ Common Mistakes

| Mistake | Fix |
|--------|-----|
| Not removing spaces | Use `replace()` |
| Case-sensitive comparison | Use `lower()` |
| Forgetting empty input case | Check length |
| Using only direct comparison | Normalize first |

---

# 🔥 Complexity

| Method | Time | Space |
|------|------|------|
| Slicing | O(n) | O(n) |
| Two-pointer | O(n) | O(1) |

---

# 🚀 Advanced Ideas

- 🔄 Check palindromes in a file
- 📊 Count palindromes in list
- 🧠 Longest palindrome substring
- 🔍 Ignore numbers & symbols

---

# 🎯 Key Learning

This problem teaches:

- String normalization
- Efficient comparison techniques
- Edge case handling
- Real-world text processing

---

Master this — it's a **classic string problem in interviews + exams**.