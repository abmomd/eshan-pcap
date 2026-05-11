# Caesar Cipher – Encrypting a Message

## ⏱ Estimated Time
20–30 minutes

---

## 🎯 Objectives
- Practice string manipulation in Python  
- Understand character encoding using `ord()` and `chr()`  
- Implement basic encryption logic  
- Work with loops and conditional statements  

---

## 📘 Scenario

The **Caesar Cipher** is one of the simplest encryption techniques.

It works by shifting each letter in a message by **one position forward** in the alphabet:

- A → B  
- B → C  
- ...  
- Z → A  

This technique was used by **Julius Caesar** to send secret messages.

---

## 🛠 Task

Write a Python program that:

1. Accepts a message (string input)
2. Encrypts it using the Caesar cipher (shift = 1)
3. Outputs the encrypted message

---

## ⚙️ Requirements

- Only **alphabetic characters** should be processed  
- Convert all letters to **uppercase**
- Ignore all non-alphabetic characters  
- Wrap around:
  - Z → A  
- Do NOT hardcode outputs

---

## 💡 Hint

- Use `ord()` to convert a character to ASCII  
- Use `chr()` to convert ASCII back to character  
- Handle wrap-around using condition or modulo  

---

## 🧪 Sample Input

HELLO

## ✅ Sample Output

IFMMP

---

## 🧪 Sample Input

XYZ

## ✅ Sample Output

YZA

---

## 🚨 Edge Cases

- Input: Z → Output: A  
- Input: abc → Output: BCD  
- Input: HELLO123 → Output: IFMMP  
- Input: empty string → Output: empty string  

---

# ✅ Solution

```python
message = input("Enter message: ")
cipher = ""

for ch in message:
    if not ch.isalpha():
        continue

    ch = ch.upper()
    code = ord(ch) + 1

    if code > ord('Z'):
        code = ord('A')

    cipher += chr(code)

print("Encrypted:", cipher)