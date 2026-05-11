# 🔐 Caesar Cipher – Enhanced Version (Solution)

---

## ✅ Approach

To solve this problem, we need to:

1. Take text input from the user  
2. Take a valid shift value (1–25)  
3. Process each character:
   - If alphabet → shift it
   - If not → keep it unchanged  
4. Preserve case (uppercase/lowercase)

---

## 🧠 Key Concepts Used

- `ord()` → Convert character → ASCII
- `chr()` → Convert ASCII → character
- `isalpha()` → Check if character is a letter
- `islower()` / `isupper()` → Preserve case
- Modulo `%` → Handle wrap-around

---

## 🧾 Complete Code

```python
# Caesar Cipher – Enhanced Version

# Step 1: Input text
text = input("Enter text to encrypt: ")

# Step 2: Input validation for shift
while True:
    try:
        shift = int(input("Enter shift value (1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Shift must be between 1 and 25.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Step 3: Encryption
result = ""

for ch in text:
    if ch.isalpha():
        if ch.islower():
            # Shift lowercase letters
            new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Shift uppercase letters
            new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        result += new_char
    else:
        # Non-alphabet characters remain unchanged
        result += ch

# Step 4: Output
print("Encrypted text:", result)
```

---

## 🧪 Example Run

### Input

```
abcxyzABCxyz 123
2
```

### Output

```
cdezabCDEzab 123
```

---

### Input

```
The die is cast
25
```

### Output

```
Sgd chd hr bzrs
```

---

# 🧠 Step-by-Step Explanation

---

## 🔹 1. ASCII Shifting Logic

For lowercase:

```
new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
```

### Why?

- `ord(ch) - ord('a')` → convert to 0–25 range
- `+ shift` → apply shift
- `% 26` → wrap around
- `+ ord('a')` → convert back to ASCII

---

## 🔹 2. Uppercase Handling

Same logic, but using:

```
ord('A')
```

---

## 🔹 3. Non-Alphabet Characters

```
if not ch.isalpha():
    keep as it is
```

---

## 🔹 4. Input Validation

- Loop until valid integer is entered
- Ensures shift is between 1 and 25

---

# 🔥 Complexity

- Time Complexity:
  ```
  O(n)
  ```
  where n = length of text

- Space Complexity:
  ```
  O(n)
  ```

---

# ⚠️ Common Mistakes

| Mistake | Fix |
|--------|-----|
| Forgetting wrap-around | Use `% 26` |
| Losing case | Check `islower()` / `isupper()` |
| Converting whole string at once | Process character by character |
| Not validating input | Use loop with try-except |

---

# 🚀 Advanced Version Ideas

- 🔄 Add decryption mode
- 🔍 Brute-force all shifts (crack cipher)
- 📄 Encrypt file contents
- 🌍 Support Unicode alphabets

---

# 🎯 Key Learning

This problem teaches:

- String traversal
- Character encoding
- Input validation
- Algorithm design
- Real-world encryption logic

---

Master this — it's a **classic PCAP + interview problem**.