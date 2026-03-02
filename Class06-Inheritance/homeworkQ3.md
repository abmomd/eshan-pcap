# 🏦 Smart Banking System – Advanced OOP Challenge

You are hired to build a **Smart Banking System** for a digital bank.

The bank has different types of accounts:

- Account (base class)
- SavingsAccount
- CurrentAccount
- PremiumCurrentAccount (inherits from CurrentAccount)

Each account behaves differently but shares some common functionality.

Your job is to design a clean inheritance hierarchy and demonstrate that it works correctly using only `print()` statements.

---

# 🎯 Your Task

---

## 🔹 1️⃣ Create Base Class: `Account`

### Instance Variables:
- `holder_name`
- `balance`

### Class Variable:
- `total_accounts` (counts total accounts created)

### Constructor:
- Accepts `holder_name` and `balance`
- Increments `total_accounts`

### Methods:

- `deposit(amount)`  
  Adds amount to balance and returns:
  ```
  Deposited <amount>
  ```

- `withdraw(amount)`  
  If sufficient balance:
  ```
  Withdrawn <amount>
  ```
  Otherwise:
  ```
  Insufficient funds
  ```

- `account_type()` → returns `"Generic Account"`

- `__str__()` →  
  ```
  Account Holder: <holder_name>, Balance: <balance>
  ```

---

## 🔹 2️⃣ Create Class: `SavingsAccount`

- Inherit from `Account`
- Add instance variable:
  - `interest_rate`

- Override:
  - `account_type()` → `"Savings Account"`

- Add method:
  - `apply_interest()`  
    Adds interest to balance and returns:
    ```
    Interest applied
    ```

- Override `__str__()` using `super()`

---

## 🔹 3️⃣ Create Class: `CurrentAccount`

- Inherit from `Account`
- Add instance variable:
  - `overdraft_limit`

- Override:
  - `withdraw(amount)`  
    Allow withdrawal if:
    ```
    balance + overdraft_limit >= amount
    ```

- Override:
  - `account_type()` → `"Current Account"`

- Override `__str__()` using `super()`

---

## 🔹 4️⃣ Create Class: `PremiumCurrentAccount`

- Inherit from `CurrentAccount`

- Override:
  - `account_type()` → `"Premium Current Account"`

- Override:
  - `withdraw(amount)`  
    Premium users have unlimited overdraft (always allow withdrawal).

- Override `__str__()` using `super()`

---

# 🧪 Create the Following Accounts

```
acc1 = SavingsAccount("Alice", 1000, 0.10)
acc2 = CurrentAccount("Bob", 500, 300)
acc3 = PremiumCurrentAccount("Charlie", 200, 500)
```

---

# 🖨 Using ONLY `print()` Statements, Display the Following

---

## 🔹 Part 1 – Account Details

Print:
- `acc1`
- `acc2`
- `acc3`

---

## 🔹 Part 2 – Inheritance Checks

Print:
- Is `SavingsAccount` a subclass of `Account`?
- Is `PremiumCurrentAccount` a subclass of `CurrentAccount`?
- Is `CurrentAccount` a subclass of `SavingsAccount`?

---

## 🔹 Part 3 – Instance Checks

Print:
- Is `acc1` an instance of `Account`?
- Is `acc3` an instance of `CurrentAccount`?
- Is `acc2` an instance of `SavingsAccount`?

---

## 🔹 Part 4 – Identity Checks

Print:
- `acc1 is acc2`
- `acc3 is acc3`

---

## 🔹 Part 5 – Transactions

Print results of:

- `acc1.deposit(500)`
- `acc1.withdraw(200)`
- `acc2.withdraw(700)`
- `acc3.withdraw(10000)`

Observe how different `withdraw()` behaviors occur.

---

## 🔹 Part 6 – Class Variable

Print:
- Total number of accounts created.

---

## 🔹 Part 7 – Polymorphism Test

Create:

```
bank_accounts = [acc1, acc2, acc3]
```

Using a loop, print:
- Each account object
- Each account’s type using `account_type()`

Notice how Python dynamically selects the correct overridden method.

---

# 🧠 Concepts This Tests

- Multi-level inheritance  
- Method overriding  
- `super()`  
- Class variables  
- Instance variables  
- `issubclass()`  
- `isinstance()`  
- `is` operator  
- Polymorphism  
- Runtime method resolution  
- Custom behavior per subclass  

---

