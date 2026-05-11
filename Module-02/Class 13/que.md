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

# ✈️ 2. Airline Reservation System

## 📘 Scenario

An airline company wants software to manage seat booking.

---

## 🎯 Requirements

The system should:

### 🔹 Accept:
- Passenger name
- Seat number
- Flight code

---

### 🔹 Handle:

| Exception | Scenario |
|----------|----------|
| `IndexError` | Seat number out of range |
| `KeyError` | Flight code missing |
| `ValueError` | Invalid passenger age |
| `LookupError` | Seat lookup failure |
| `AssertionError` | Flight capacity exceeded |

---

## ⚙️ Additional Rules

- Use list for seats
- Use dictionary for flights
- Use `assert` for max capacity

---

# 🏥 3. Hospital Patient Monitoring System

## 📘 Scenario

A hospital monitors patients using sensors.

The system continuously processes:

- Heart rate
- Oxygen level
- Blood pressure

---

## 🎯 Requirements

Handle the following situations:

| Exception | Scenario |
|----------|----------|
| `ValueError` | Invalid sensor reading |
| `AssertionError` | Dangerous vital signs |
| `OverflowError` | Extremely large sensor values |
| `TypeError` | Wrong data type |
| `KeyboardInterrupt` | Emergency shutdown |

---

## ⚙️ Additional Rules

- Heart rate must be between 30 and 200
- Oxygen level must be above 70
- Use assertions for critical checks

---

# ☁️ 4. Cloud File Storage System

## 📘 Scenario

A cloud storage company wants a secure file upload system.

---

## 🎯 Requirements

The system should:

### 🔹 Accept:
- File name
- File size
- User storage limit

---

### 🔹 Handle:

| Exception | Scenario |
|----------|----------|
| `FileNotFoundError` | Missing file |
| `MemoryError` | File too large |
| `PermissionError` | Unauthorized access |
| `ImportError` | Missing compression module |
| `AssertionError` | Negative storage remaining |

---

## ⚙️ Additional Rules

- Uploaded file must fit inside user quota
- Use assertions to protect storage calculations

---

# 🚗 5. Smart Self-Driving Car System

## 📘 Scenario

A self-driving car processes live road data.

The system handles:

- GPS
- Speed
- Camera sensors
- Navigation

---

## 🎯 Requirements

Handle the following:

| Exception | Scenario |
|----------|----------|
| `LookupError` | GPS location missing |
| `IndexError` | Sensor index invalid |
| `ValueError` | Invalid speed value |
| `AssertionError` | Unsafe speed detected |
| `KeyboardInterrupt` | Manual override by driver |

---

## ⚙️ Additional Rules

- Speed must remain below safety limit
- GPS database stored in dictionary
- Sensor readings stored in list

---

# 🛒 6. E-Commerce Payment Gateway

## 📘 Scenario

An online shopping company processes customer payments.

---

## 🎯 Requirements

The system should:

### 🔹 Validate:
- Card number
- Payment amount
- Product inventory

---

### 🔹 Handle:

| Exception | Scenario |
|----------|----------|
| `ValueError` | Invalid card number |
| `KeyError` | Product not found |
| `ArithmeticError` | Discount calculation failure |
| `AssertionError` | Negative stock |
| `OverflowError` | Extremely large payment |

---

## ⚙️ Additional Rules

- Inventory stored in dictionary
- Use assertions for stock validation

---

# 🧠 7. AI Chatbot Deployment System

## 📘 Scenario

An AI company deploys machine learning models dynamically.

---

## 🎯 Requirements

The deployment system should handle:

| Exception | Scenario |
|----------|----------|
| `ImportError` | Missing AI library |
| `MemoryError` | Model too large |
| `TypeError` | Wrong configuration type |
| `AssertionError` | Invalid model accuracy |
| `RuntimeError` | Model execution failure |

---

## ⚙️ Additional Rules

- Accuracy must remain above threshold
- Use assertions for model validation

---

# 🎯 Goal of These Problems

These systems simulate:

- Banking software
- Cloud platforms
- AI systems
- Medical software
- Automotive software

They help students learn:

- Defensive programming
- Real-world exception handling
- Validation logic
- Safe software design
- Production-quality thinking

---

# 🚀 Advanced Challenge

For every system:

- Add multiple `except` blocks
- Add logging
- Re-raise critical exceptions
- Use custom exceptions
- Add `finally` blocks for cleanup