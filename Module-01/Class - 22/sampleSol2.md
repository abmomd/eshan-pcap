# 🛰️ Solution: System Diagnostics Dashboard

```python
import math
import random
import platform

print("=" * 40)
print("SYSTEM DIAGNOSTICS")
print("=" * 40)

# -----------------------------
# Part 1
# -----------------------------
print("\nAvailable Functions in math Module\n")
print(dir(math))

# -----------------------------
# Part 2
# -----------------------------
print("\nMathematical Calculations")
print("-" * 30)

print("Pi:", math.pi)
print("Euler Number:", math.e)
print("Square Root of 625:", math.sqrt(625))
print("Factorial of 7:", math.factorial(7))
print("3^8:", math.pow(3, 8))

# -----------------------------
# Part 3
# -----------------------------
print("\nLucky Coupon Generator")
print("-" * 30)

coupon = random.randint(1000, 9999)
print("Coupon Number:", coupon)

customers = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emma"
]

winner = random.choice(customers)
print("Lucky Customer:", winner)

prizes = [
    "Gold",
    "Silver",
    "Bronze",
    "Gift Card",
    "Holiday Package"
]

random.shuffle(prizes)

print("\nPrize Boxes")
print(prizes)

# -----------------------------
# Part 4
# -----------------------------
print("\nReproducible Random Numbers")
print("-" * 30)

random.seed(42)

for _ in range(5):
    print(random.randint(1, 100))

# -----------------------------
# Part 5
# -----------------------------
print("\nSystem Information")
print("-" * 30)

print("Operating System :", platform.system())
print("Release          :", platform.release())
print("Architecture     :", platform.machine())
print("Processor        :", platform.processor())
print("Python Version   :", platform.python_version())
```

---

# Concepts Used

## Explore a Module

```python
dir(math)
```

Displays all available functions, constants, and classes in the `math` module.

---

## Mathematical Operations

```python
math.sqrt()
math.factorial()
math.pow()
math.pi
math.e
```

---

## Random Module

```python
random.randint()
random.choice()
random.shuffle()
random.seed()
```

---

## Platform Module

```python
platform.system()
platform.release()
platform.machine()
platform.processor()
platform.python_version()
```

---

# Skills Practiced

- Exploring module contents with `dir()`
- Performing mathematical calculations
- Working with pseudo-random numbers
- Creating reproducible random sequences using `seed()`
- Retrieving operating system and hardware information
- Combining multiple standard library modules in a single real-world application