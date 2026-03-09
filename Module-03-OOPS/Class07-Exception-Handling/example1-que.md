# 🏦 Smart Banking Transaction System – Advanced Exception Handling Challenge

You are hired to design a **Smart Banking Transaction System** for a digital bank.  
The system must handle withdrawals safely and professionally using advanced exception handling techniques.

Your goal is to implement a clean, production-style exception handling structure using:

- Custom exception classes
- Multiple `except` blocks
- `else`
- `finally`
- Exception objects (`as e`)
- Accessing `.args`
- Proper error messaging

---

# 🎯 Requirements

## 🔹 1️⃣ Create Custom Exceptions

Create the following custom exceptions:

1. `InvalidAmountError`
   - Should inherit from `ValueError`
   - Raised when withdrawal amount is zero or negative

2. `InsufficientFundsError`
   - Should inherit from `Exception`
   - Should store:
     - Current balance
     - Attempted withdrawal amount
   - Must pass a meaningful message to the base Exception class

---

## 🔹 2️⃣ Create Class: `BankAccount`

The class must have:

- Instance variables:
  - `holder`
  - `balance`

- Method:
  ```
  withdraw(amount)
  ```

The method must:

- Raise `InvalidAmountError` if amount ≤ 0
- Raise `InsufficientFundsError` if amount > balance
- Otherwise:
  - Deduct amount
  - Return a success message containing updated balance

---

## 🔹 3️⃣ Create Function: `process_transaction(account, amount)`

This function must:

- Print a message indicating transaction start
- Use a `try` block to call `account.withdraw(amount)`

Include the following exception handling:

- Catch `InvalidAmountError`
- Catch `InsufficientFundsError`
  - Print all arguments stored inside the exception object using `.args`
  - Print the stored balance from the exception object
- Catch any other unexpected exception

Use:

- `else` block to print a success confirmation message
- `finally` block to print:
  ```
  Session closed.
  ```

---

## 🔹 4️⃣ Test Cases

Create:

```
account = BankAccount("Alice", 1000)
```

Then call:

```
process_transaction(account, 200)
process_transaction(account, -50)
process_transaction(account, 2000)
```

---

# 🧠 Conceptual Questions (Answer in Comments)

1. Why does `else` execute only in some cases?
2. Why is `finally` always executed?
3. What does the `.args` property contain?
4. Why is `InvalidAmountError` inheriting from `ValueError`?
5. What would happen if you removed the `except InsufficientFundsError` block?
6. What is the benefit of storing structured data inside a custom exception?

---

# 🚀 Advanced Challenge (Optional)

Modify the system to:

- Re-raise unexpected exceptions after logging them.
- Add another custom exception:
  ```
  DailyLimitExceededError
  ```
- Demonstrate exception chaining using:
  ```
  raise NewException from original_exception
  ```

---

# 🎯 Goal

This assignment tests:

- Advanced exception handling
- Custom exception design
- Inheritance in exceptions
- Structured error information
- `try-except-else-finally` flow control
- Real-world defensive programming

