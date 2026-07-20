# 📦 Project: Smart Store Utility Toolkit

## 📘 Story

You have been hired by **QuickMart**, a retail company that is developing a utility toolkit for its billing software.

Instead of writing everything in one file, the company has already created several Python modules.

Your job is to write the **main program** that imports these modules correctly and uses their functions.

---

## 📂 Project Structure

```text
QuickMart/

├── billing.py
├── discount.py
├── inventory.py
├── reports.py
└── main.py
```

---

## Module Details

### billing.py

Contains:

- `generate_bill()`
- `calculate_tax()`

---

### discount.py

Contains:

- `apply_discount()`

---

### inventory.py

Contains:

- `check_stock()`
- `update_stock()`

---

### reports.py

Contains:

- `daily_report()`

---

## 🎯 Your Tasks

### Part 1

Import the **entire** `billing` module and use its functions.

---

### Part 2

Import only the `apply_discount()` function from the `discount` module.

---

### Part 3

Import the `inventory` module using the alias `inv`.

---

### Part 4

Import the `daily_report()` function from the `reports` module using the alias `report`.

---

### Part 5

Call all imported functions in an appropriate order to simulate a customer purchase.

---

## Expected Flow

```text
Checking Stock...

↓

Applying Discount...

↓

Generating Bill...

↓

Calculating Tax...

↓

Updating Inventory...

↓

Generating Daily Report...
```

---

## Concepts Covered

- import module
- from module import function
- import module as alias
- from module import function as alias
- Dot notation