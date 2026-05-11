# 🌍 Advanced Real-Life Exception Handling Challenges

These assignments are designed to simulate **real production systems**.

Each problem requires proper use of:

- `try-except`
- Multiple exceptions
- Exception hierarchy
- `raise`
- `assert`
- Real-world validation logic

---

# 🏦 1. Smart ATM Banking System

## 📘 Scenario

You are building software for a Smart ATM machine.

The ATM should:

- Allow users to withdraw money
- Validate account information
- Handle incorrect operations safely

---

## 🎯 Requirements

Create a program that:

### 🔹 Accepts:
- PIN number
- Withdrawal amount
- Account balance

---

### 🔹 Use the following exceptions:

| Exception | Scenario |
|----------|----------|
| `ValueError` | Invalid withdrawal amount |
| `AssertionError` | Negative balance detected |
| `ZeroDivisionError` | ATM service charge calculation failure |
| `KeyboardInterrupt` | User cancels transaction |
| `ArithmeticError` | General arithmetic issue |

---

## ⚙️ Additional Rules

- Withdrawal cannot exceed balance
- Balance must never become negative
- Service charge = amount / number_of_notes
- Use `assert` to protect balance

---