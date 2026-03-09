# 🏦 Advanced Real-Life Example – Smart Banking Transaction System

In real-world systems, exception handling is not just about printing errors.
It is about:

- Protecting system state
- Giving meaningful error messages
- Logging failures
- Guaranteeing cleanup
- Preserving original error context

Let’s build a **Smart Banking Transaction System**.

---

## 🎯 Scenario

You are designing a banking system that:

- Validates withdrawal amount
- Checks account balance
- Logs transactions
- Uses custom exceptions
- Always closes session properly

---

## 🧠 Step 1 – Define Custom Exceptions

```python
class InvalidAmountError(ValueError):
    pass


class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Balance: {balance}, Attempted: {amount}")
        self.balance = balance
        self.amount = amount
```

---

## 🧠 Step 2 – Account Class

```python
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal must be positive")

        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)

        self.balance -= amount
        return f"Withdrawal successful. Remaining balance: {self.balance}"
```

---

## 🧠 Step 3 – Transaction Processor

```python
def process_transaction(account, amount):
    print(f"\nProcessing withdrawal of {amount} for {account.holder}")

    try:
        result = account.withdraw(amount)

    except InvalidAmountError as e:
        print("Invalid transaction:", e)

    except InsufficientFundsError as e:
        print("Transaction failed!")
        print("Details:", e.args)
        print(f"Available balance was {e.balance}")

    except Exception as e:
        print("Unexpected error occurred:", e)

    else:
        print("Transaction completed successfully!")
        print(result)

    finally:
        print("Session closed.")
```

---

## 🧪 Step 4 – Testing Different Scenarios

```python
account = BankAccount("Alice", 1000)

process_transaction(account, 200)    # Valid
process_transaction(account, -50)    # Invalid amount
process_transaction(account, 2000)   # Insufficient funds
```

---

# ✅ Expected Output

```
Processing withdrawal of 200 for Alice
Transaction completed successfully!
Withdrawal successful. Remaining balance: 800
Session closed.

Processing withdrawal of -50 for Alice
Invalid transaction: Withdrawal must be positive
Session closed.

Processing withdrawal of 2000 for Alice
Transaction failed!
Details: ('Balance: 800, Attempted: 2000',)
Available balance was 800
Session closed.
```

---



This demonstrates:

✔ Custom exception classes  
✔ Inheriting from built-in exceptions  
✔ Using `super()` inside exceptions  
✔ Accessing `.args`  
✔ Multiple except blocks  
✔ `else` for success path  
✔ `finally` for guaranteed cleanup  
✔ Real-world logic  
✔ Proper separation of concerns  

---

# 🧠 Advanced Variation – Exception Chaining

You can chain exceptions like this:

```python
try:
    raise ValueError("Low-level failure")
except ValueError as e:
    raise RuntimeError("High-level failure") from e
```

This preserves the original traceback.

---

# 🎯 Key Takeaways

- `else` runs only if no exception occurs.
- `finally` always runs.
- `.args` stores constructor parameters.
- Custom exceptions can carry structured data.
- Real systems separate validation, processing, and error handling.
- Exception chaining preserves debugging context.

---

---
