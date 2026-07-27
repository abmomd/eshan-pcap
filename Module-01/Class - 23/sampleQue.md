# 🏦 Project: Smart Banking Package Management System

## 📘 Story

A software company is developing a **Digital Banking System**. To keep the project organized, the developers have divided the application into multiple packages and modules.

Your task is to write the **main program** that correctly imports and uses these modules.

---

# 📂 Project Structure

```text
BankSystem/

│
├── banking/
│   │
│   ├── __init__.py
│   ├── accounts.py
│   ├── loans.py
│   ├── transactions.py
│   └── security.py
│
└── main.py
```

---

## Module Details

### accounts.py

Contains:

- create_account()
- check_balance()

---

### loans.py

Contains:

- apply_loan()

---

### transactions.py

Contains:

- deposit()
- withdraw()

---

### security.py

Contains:

- verify_pin()
- _encrypt_data() *(Private Function)*

---

# 🎯 Your Tasks

## Part 1

Import the **accounts** module and use both of its functions.

---

## Part 2

Import only the `apply_loan()` function from the **loans** module.

---

## Part 3

Import the **transactions** module using the alias `txn`.

---

## Part 4

Import the `verify_pin()` function using an alias called `verify`.

---

## Part 5

Call the imported functions in the following order:

1. Verify PIN
2. Create Account
3. Deposit Money
4. Withdraw Money
5. Check Balance
6. Apply Loan

---

## Part 6

Attempt to access the private function `_encrypt_data()`.

Is it possible?

Should it be used directly?

Explain your answer as comments in your code.

---

## Part 7

Suppose the **BankSystem** folder is stored at:

```text
D:\Python\Projects
```

Write the Python code required so that Python can locate this package.

---

## Part 8

Explain the purpose of the following files/directories:

- `__init__.py`
- `__pycache__`

---

# Concepts Covered

- Packages
- Modules
- import
- from ... import ...
- Aliasing (`as`)
- Private members
- sys.path
- __init__.py
- __pycache__