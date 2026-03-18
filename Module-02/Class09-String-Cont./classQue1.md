# 🔢 Seven-Segment Display Simulation – Medium Level

## ⏱ Estimated Time
30 minutes

## 🎯 Objectives

- Improve skills in **string manipulation**
- Learn how to use strings to represent **non-text data (visual patterns)**
- Practice working with **lists and structured data**
- Build logic for **multi-line output formatting**

---

## 📘 Scenario

You have probably seen a **seven-segment display** – commonly used in:

- Digital clocks
- Calculators
- Elevators
- Scoreboards

Each digit (0–9) is represented using **segments (LEDs)**.

In this problem, instead of actual segments, we simulate the display using characters:

```
# → LED ON
(space) → LED OFF
```

---

## 🖥 Visual Representation of Digits

Each digit is represented using **5 rows and 3 columns**:

```
  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ### 
```

Each group corresponds to digits from **0 to 9**.

---

## 🛠 Task

Write a program that:

- Accepts a **non-negative integer number** as input
- Displays the number using the **seven-segment LED style**
- Uses `#` for lit segments and space for unlit segments
- Prints the result in **5 rows**

---

## ⚙️ Requirements

- Input must be treated as a **string**
- Each digit must be displayed using its corresponding pattern
- Combine multiple digits **horizontally**
- Maintain proper spacing between digits
- Do NOT hardcode output for specific inputs

---

## 💡 Hint

- Store all digit patterns (0–9) in a **list**
- Each digit can be represented as a list of 5 strings
- Iterate row-wise to build the final output

---

## 🧪 Sample Input 1

```
123
```

### ✅ Output

```
  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 
```

---

## 🧪 Sample Input 2

```
9081726354
```

### ✅ Output

```
### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 
```

---

## 🚨 Edge Cases

- Input: `0` → Should display digit 0 correctly
- Input: single digit → Still print 5 rows
- Input: large number → Must scale properly

---
