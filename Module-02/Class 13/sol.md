# 🌍 Solutions – Advanced Real-Life Exception Handling Challenges

---

# 🏦 1. Smart ATM Banking System

## ✅ Solution

```python
try:
    pin = input("Enter PIN: ")

    if pin != "1234":
        raise ValueError("Invalid PIN")

    balance = 5000

    amount = float(input("Enter withdrawal amount: "))

    assert balance >= 0

    notes = int(input("Enter number of notes available: "))


    if amount > balance:
        raise ArithmeticError("Insufficient funds")

    balance -= amount

    print("Transaction successful")
    print("Remaining balance:", balance)

except ValueError as e:
    print("Value Error:", e)

except ZeroDivisionError:
    print("ATM cannot dispense zero notes.")

except AssertionError:
    print("Negative balance detected.")


except ArithmeticError as e:
    print("Arithmetic Error:", e)
```

---

# ✈️ 2. Airline Reservation System

## ✅ Solution

```python
flights = {
    "AI101": ["A1", "A2", "A3"]
}

try:
    code = input("Enter flight code: ")

    if code not in flights:
        raise KeyError("Flight not found")

    seats = flights[code]

    seat_index = int(input("Enter seat index: "))

    assert len(seats) <= 3

    print("Seat booked:", seats[seat_index])

except IndexError:
    print("Invalid seat number.")

except KeyError as e:
    print("Flight Error:", e)

except LookupError:
    print("Seat lookup failed.")

except AssertionError:
    print("Flight capacity exceeded.")
```

---

# 🏥 3. Hospital Patient Monitoring System

## ✅ Solution

```python
try:
    heart_rate = int(input("Enter heart rate: "))
    oxygen = int(input("Enter oxygen level: "))

    assert 30 <= heart_rate <= 200
    assert oxygen >= 70

    huge = 1E250 ** 2

    print("Patient stable.")

except ValueError:
    print("Invalid sensor reading.")

except AssertionError:
    print("Critical patient condition detected.")

except OverflowError:
    print("Sensor value overflow.")

except TypeError:
    print("Wrong sensor data type.")

except KeyboardInterrupt:
    print("\nEmergency shutdown activated.")
```

---

# ☁️ 4. Cloud File Storage System

## ✅ Solution

```python
try:
    filename = input("Enter file name: ")

    if filename == "":
        raise FileNotFoundError("File missing")

    file_size = int(input("Enter file size (MB): "))
    limit = 500

    remaining = limit - file_size

    assert remaining >= 0

    huge_storage = [0] * (10**8)

    print("File uploaded successfully.")

except FileNotFoundError as e:
    print("File Error:", e)

except MemoryError:
    print("System memory exceeded.")

except PermissionError:
    print("Access denied.")

except ImportError:
    print("Compression module missing.")

except AssertionError:
    print("Storage limit exceeded.")
```

---

# 🚗 5. Smart Self-Driving Car System

## ✅ Solution

```python
gps = {
    "Home": "Location A"
}

sensors = [20, 30, 40]

try:
    destination = input("Enter destination: ")

    print(gps[destination])

    sensor_index = int(input("Enter sensor index: "))
    print("Sensor reading:", sensors[sensor_index])

    speed = int(input("Enter speed: "))

    assert speed <= 120

    print("Navigation active.")

except LookupError:
    print("GPS lookup failed.")

except IndexError:
    print("Invalid sensor index.")

except ValueError:
    print("Invalid speed entered.")

except AssertionError:
    print("Unsafe speed detected.")

except KeyboardInterrupt:
    print("\nDriver manual override activated.")
```

---

# 🛒 6. E-Commerce Payment Gateway

## ✅ Solution

```python
inventory = {
    "Laptop": 5,
    "Phone": 10
}

try:
    product = input("Enter product: ")

    stock = inventory[product]

    amount = float(input("Enter payment amount: "))

    assert stock > 0

    huge = 1E250 ** 2

    card = input("Enter card number: ")

    if len(card) != 16:
        raise ValueError("Invalid card number")

    print("Payment successful.")

except ValueError as e:
    print("Value Error:", e)

except KeyError:
    print("Product not found.")

except ArithmeticError:
    print("Payment arithmetic issue.")

except AssertionError:
    print("Out of stock.")

except OverflowError:
    print("Payment value too large.")
```

---

# 🤖 7. AI Chatbot Deployment System

## ✅ Solution

```python
try:
    accuracy = float(input("Enter model accuracy: "))

    assert accuracy >= 0.80

    import math

    config = "GPU"

    if not isinstance(config, dict):
        raise TypeError("Configuration must be dictionary")

    huge_model = [0] * (10**9)

    print("AI model deployed successfully.")

except ImportError:
    print("AI module missing.")

except MemoryError:
    print("Insufficient memory for model.")

except TypeError as e:
    print("Type Error:", e)

except AssertionError:
    print("Model accuracy too low.")

except RuntimeError:
    print("Model execution failed.")
```

---

# 🎯 Concepts Used

| Concept | Used |
|--------|------|
| `try-except` | All programs |
| Multiple exceptions | Yes |
| `raise` | ATM, Payment |
| `assert` | Validation |
| Hierarchy | ArithmeticError, LookupError |
| Specific vs general exceptions | Yes |
| Real-world validation | Yes |

---

# 🚀 Final Thought

These examples simulate:

- Banking software
- Airline systems
- Hospital monitoring
- Cloud infrastructure
- Self-driving vehicles
- Payment gateways
- AI deployment systems

This is the type of exception handling used in real production systems.