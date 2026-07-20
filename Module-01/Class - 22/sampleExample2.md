# 🛰️ Project: System Diagnostics Dashboard

## 📘 Story

A software company develops applications that run on Windows, Linux, and macOS.

Before launching the application, the developers want to generate a **System Diagnostics Report** to verify the user's computer and perform a few utility operations.

You have been hired to create this report using Python's built-in modules.

---

# 🎯 Your Task

Create a program that generates a system report.

---

## Part 1: Explore a Module

Display all the functions and constants available in the **math** module using the appropriate function.

---

## Part 2: Mathematical Calculations

Display:

- Value of π
- Value of e
- Square root of 625
- Factorial of 7
- 3 raised to the power 8

---

## Part 3: Lucky Coupon Generator

Generate:

- A random coupon number between **1000 and 9999**
- A random lucky customer from the list:

```python
["Alice", "Bob", "Charlie", "David", "Emma"]
```

- Shuffle the following prize boxes:

```python
["Gold", "Silver", "Bronze", "Gift Card", "Holiday Package"]
```

---

## Part 4: Reproducible Random Numbers

Set the random seed to **42**.

Generate five random numbers between **1 and 100**.

Display the numbers.

---

## Part 5: System Information

Display:

- Operating System
- Operating System Release
- Machine Architecture
- Processor Name
- Python Version

---

## Expected Output (Example)

```text
========== SYSTEM DIAGNOSTICS =========

Math Module Loaded

Pi : 3.141592653589793
Euler Number : 2.718281828459045
Square Root : 25.0
Factorial : 5040
Power : 6561.0

Coupon Number : 5823

Lucky Customer : Charlie

Prize Boxes
['Gift Card', 'Gold', 'Bronze', 'Holiday Package', 'Silver']

Random Numbers
82
15
4
95
36

Operating System : Windows
Release : 11
Architecture : AMD64
Processor : Intel(R) Core(TM) i7
Python Version : 3.12.5
```

---

# Concepts Covered

- dir()
- math module
- random module
- random.seed()
- platform module