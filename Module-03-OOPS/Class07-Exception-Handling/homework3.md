# 💳 Smart Payment Gateway System – Advanced Exception Handling Challenge

You are hired to build a **Smart Online Payment Gateway System** for an e-commerce platform.

The system must securely process payments while handling all possible transaction failures in a professional way.

You must implement:

- Custom exception classes
- Inheriting from built-in exceptions
- Structured exception data
- Accessing `.args`
- Multiple `except` blocks
- `else`
- `finally`
- Optional exception chaining
- Defensive programming

---

# 🎯 System Requirements

---

## 🔹 1️⃣ Create Custom Exceptions

Create the following exception classes:

### 1. `InvalidCardNumberError`
- Inherit from `ValueError`
- Raised if card number is not 16 digits

---

### 2. `InsufficientBalanceError`
- Inherit from `Exception`
- Must store:
  - available balance
  - attempted payment amount
- Pass a meaningful message to the base `Exception` class

---

### 3. `PaymentLimitExceededError`
- Inherit from `Exception`
- Raised if daily transaction limit is exceeded

---

### 4. `SuspiciousActivityError`
- Inherit from `RuntimeError`
- Raised if payment amount exceeds a suspicious threshold (e.g., ₹1,00,000)

---

## 🔹 2️⃣ Create Class: `UserAccount`

The class must contain:

- Instance variables:
  - `username`
  - `balance`
  - `daily_limit`
  - `daily_spent`

---

### Required Method:

```
make_payment(card_number, amount)
```

The method must:

- Raise `InvalidCardNumberError` if card number is not exactly 16 digits
- Raise `ValueError` if amount ≤ 0
- Raise `SuspiciousActivityError` if amount > 100000
- Raise `PaymentLimitExceededError` if daily_spent + amount > daily_limit
- Raise `InsufficientBalanceError` if amount > balance
- Otherwise:
  - Deduct amount from balance
  - Update daily_spent
  - Return success message

---

## 🔹 3️⃣ Create Function: `process_payment(user, card_number, amount)`

This function must:

- Print payment attempt details
- Use a `try` block to call `make_payment()`

Include the following exception handling:

- Catch `InvalidCardNumberError`
- Catch `InsufficientBalanceError`
  - Print `.args`
  - Print available balance from exception object
- Catch `PaymentLimitExceededError`
- Catch `SuspiciousActivityError`
- Catch `ValueError`
- Catch any unexpected exception

Use:

- `else` → Print successful transaction message
- `finally` → Print:
  ```
  Payment session ended.
  ```

---

## 🔹 4️⃣ Testing Scenario

Create:

```
user = UserAccount("Alice", 50000, 30000)
```

Test the following cases:

```
process_payment(user, "1234567812345678", 5000)
process_payment(user, "123", 1000)
process_payment(user, "1234567812345678", 60000)
process_payment(user, "1234567812345678", -500)
process_payment(user, "1234567812345678", 200000)
process_payment(user, "1234567812345678", 28000)
```


---

# 🎯 What This Assignment Tests

- Advanced exception handling
- Custom exception design
- Exception inheritance hierarchy
- Structured error data
- `.args`
- try–except–else–finally control flow
- Defensive programming
- Real-world production modeling
- Error categorization strategy

Design your solution like a real payment gateway used in production.