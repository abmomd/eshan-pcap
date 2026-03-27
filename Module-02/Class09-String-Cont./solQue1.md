# 🔢 Seven-Segment Display Simulation – Solution

---

## ✅ Approach

To solve this problem:

1. Represent each digit (0–9) using a **list of 5 strings**
2. Store all digits inside a **list**
3. Read the input as a **string**
4. For each row (0 to 4):
   - Traverse each digit in input
   - Print corresponding row pattern
5. Combine patterns horizontally

---

## 💡 Key Idea

Each digit looks like:

```
digit = [
    "row1",
    "row2",
    "row3",
    "row4",
    "row5"
]
```

We store all digits in a list:

```
digits = [digit0, digit1, ..., digit9]
```

---

## 🧠 Complete Code

```python
def display_number(number):
    digits = [
        ["###", "# #", "# #", "# #", "###"],  # 0
        ["  #", "  #", "  #", "  #", "  #"],  # 1
        ["###", "  #", "###", "#  ", "###"],  # 2
        ["###", "  #", "###", "  #", "###"],  # 3
        ["# #", "# #", "###", "  #", "  #"],  # 4
        ["###", "#  ", "###", "  #", "###"],  # 5
        ["###", "#  ", "###", "# #", "###"],  # 6
        ["###", "  #", "  #", "  #", "  #"],  # 7
        ["###", "# #", "###", "# #", "###"],  # 8
        ["###", "# #", "###", "  #", "###"]   # 9
    ]

    number = str(number)

    for row in range(5):
        for digit in number:
            print(digits[int(digit)][row], end=" ")
        print()


# 🔹 Input from user
num = input("Enter a number: ")
display_number(num)
```

---

## 🧪 Example Run

### Input:

```
123
```

### Output:

```
  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 
```

---

# 🧠 Step-by-Step Explanation

---

## 1️⃣ Store Patterns

Each digit is represented using **5 rows**:

Example for digit `2`:

```
###
  #
###
#  
###
```

---

## 2️⃣ Convert Input to String

```python
number = str(number)
```

So we can iterate digit by digit.

---

## 3️⃣ Loop Row-wise

```python
for row in range(5):
```

We print row-by-row instead of digit-by-digit.

---

## 4️⃣ Print Each Digit’s Row

```python
for digit in number:
    print(digits[int(digit)][row], end=" ")
```

- Convert character → integer
- Access correct digit pattern
- Print corresponding row

---

## 5️⃣ Move to Next Line

```python
print()
```

---

# 🔥 Time & Space Complexity

- Time Complexity:  
  ```
  O(n)
  ```
  where `n` = number of digits

- Space Complexity:
  ```
  O(1)
  ```
  (fixed digit patterns)

---

# ⚠️ Common Mistakes

| Mistake | Fix |
|--------|-----|
| Using int input | Always treat as string |
| Printing digit-wise | Must print row-wise |
| Forgetting spacing | Add `" "` between digits |
| Wrong indexing | Use `int(digit)` |

---

# 🚀 Advanced Version Ideas

- 🔄 Animate digits (scrolling display)
- 🎨 Use custom symbols instead of `#`
- 📏 Adjustable digit width/height
- 🖥 GUI version (Tkinter / Web)

---

# 🎯 Key Learning

This problem teaches:

- Pattern-based thinking
- String manipulation
- Multi-line formatting
- Data structure usage (list of lists)
- Real-world simulation logic

---

Master this — it's a **classic PCAP-style problem**.