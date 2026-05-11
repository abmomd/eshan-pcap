# 🌍 Real-Life Examples of Built-in Python Exceptions

Understanding exceptions becomes much easier when you connect them to real-world systems.

Below are practical examples showing where different Python exceptions may occur in real applications.

---

# 🧠 1️⃣ ArithmeticError

## 📘 Scenario – Banking Interest Calculator

A banking system calculates compound interest.

A mathematical issue occurs during calculation.

---

## ✅ Example

```python
try:
    amount = 1000000
    years = 1000

    result = amount ** years
    print(result)

except ArithmeticError:
    print("Arithmetic calculation failed.")
```

---

## 🧠 Real Life

Used in:

- Financial systems
- Scientific simulations
- Physics engines

---

# 🧠 2️⃣ ZeroDivisionError

## 📘 Scenario – School Result System

A school system calculates average marks.

But number of students becomes zero.

---

## ✅ Example

```python
try:
    total_marks = 500
    students = 0

    average = total_marks / students
    print(average)

except ZeroDivisionError:
    print("Cannot divide by zero students.")
```

---

# 🧠 Real Life

Used in:

- Analytics dashboards
- Statistics systems
- Data science pipelines

---

# 🧠 3️⃣ LookupError

## 📘 Scenario – GPS Navigation System

A navigation app searches for a city that does not exist.

---

## ✅ Example

```python
cities = {
    "Paris": "France",
    "Tokyo": "Japan"
}

try:
    print(cities["London"])

except LookupError:
    print("Location not found.")
```

---

## 🧠 Real Life

Used in:

- Search engines
- Maps systems
- Inventory lookup systems

---

# 🧠 4️⃣ IndexError

## 📘 Scenario – Movie Ticket Booking

A cinema booking system tries to access a seat that doesn't exist.

---

## ✅ Example

```python
seats = ["A1", "A2", "A3"]

try:
    print(seats[10])

except IndexError:
    print("Seat number does not exist.")
```

---

## 🧠 Real Life

Used in:

- Booking systems
- Gaming inventories
- Spreadsheet software

---

# 🧠 5️⃣ KeyError

## 📘 Scenario – Employee Database

A company system searches for missing employee information.

---

## ✅ Example

```python
employee = {
    "name": "Alice",
    "department": "HR"
}

try:
    print(employee["salary"])

except KeyError:
    print("Employee data missing.")
```

---

## 🧠 Real Life

Used in:

- Database systems
- APIs
- JSON processing

---

# 🧠 6️⃣ AssertionError

## 📘 Scenario – ATM Withdrawal Limit

ATM should never allow negative withdrawal amount.

---

## ✅ Example

```python
withdraw_amount = -500

try:
    assert withdraw_amount > 0
    print("Transaction approved")

except AssertionError:
    print("Invalid withdrawal amount.")
```

---

## 🧠 Real Life

Used in:

- Security checks
- Internal validations
- Testing systems

---

# 🧠 7️⃣ ImportError

## 📘 Scenario – AI Application

An AI system tries to load a machine learning module that is missing.

---

## ✅ Example

```python
try:
    import tensorflow

except ImportError:
    print("Required AI module not installed.")
```

---

## 🧠 Real Life

Used in:

- Deployment systems
- Plugin architectures
- Modular applications

---

# 🧠 8️⃣ KeyboardInterrupt

## 📘 Scenario – Long Running Server

A server is running continuously until administrator stops it manually.

---

## ✅ Example

```python
try:
    while True:
        print("Server running...")

except KeyboardInterrupt:
    print("Server stopped safely.")
```

---

## 🧠 Real Life

Used in:

- Servers
- Background processes
- Data monitoring systems

---

# 🧠 9️⃣ MemoryError

## 📘 Scenario – Big Data Processing

A data analytics system tries to load huge data into memory.

---

## ✅ Example

```python
try:
    huge_data = [0] * (10**20)

except MemoryError:
    print("System ran out of memory.")
```

---

## 🧠 Real Life

Used in:

- AI training
- Big data systems
- Image/video processing

---

# 🧠 🔟 OverflowError

## 📘 Scenario – Scientific Simulation

A physics simulation generates numbers too large to handle.

---

## ✅ Example

```python
try:
    huge_value = 1E250 ** 2
    print(huge_value)

except OverflowError:
    print("Number too large to process.")
```

---

## 🧠 Real Life

Used in:

- Astronomy calculations
- Scientific computing
- Financial simulations

---

# 🎯 Summary Table

| Exception | Real-Life Example |
|----------|------------------|
| ArithmeticError | Financial calculations |
| ZeroDivisionError | Average calculations |
| LookupError | Search systems |
| IndexError | Seat booking |
| KeyError | Database lookup |
| AssertionError | Security validation |
| ImportError | Missing software module |
| KeyboardInterrupt | Stopping servers |
| MemoryError | Big data loading |
| OverflowError | Scientific calculations |

---

# 🚀 Final Thought

Exception handling is not just for avoiding crashes.

It helps programs:

- Recover safely
- Protect data
- Improve user experience
- Detect dangerous situations early

Professional software systems rely heavily on strong exception handling.