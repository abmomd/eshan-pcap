# 🐾 Inheritance Exercises – PCAP Practice (10 Questions)

## 📘 Scenario

Assume that the following piece of code has been successfully executed:

```python
class Device:
    total_devices = 0

    def __init__(self, brand):
        self.brand = brand
        Device.total_devices += 1

    def __str__(self):
        return self.brand + " device is powered on."


class Smartphone(Device):
    def __str__(self):
        return super().__str__() + " Making calls and browsing."


class Laptop(Device):
    def __str__(self):
        return super().__str__() + " Running heavy applications."


phone = Smartphone("Apple")
computer = Laptop("Dell")
```

---

# 📝 Question 1

What is the expected output?

```python
print(phone)
print(computer)
```

---

# 📝 Question 2

What is the output?

```python
print(issubclass(Smartphone, Device), issubclass(Laptop, Smartphone))
```

---

# 📝 Question 3

What is the output?

```python
print(isinstance(phone, Device), isinstance(phone, Laptop))
```

---

# 📝 Question 4

What is the output?

```python
print(phone is phone, phone is computer)
```

---

# 📝 Question 5

What is the output?

```python
print(Device.total_devices)
```

---

# 📝 Question 6

What is the output?

```python
another_phone = Smartphone("Samsung")
print(Device.total_devices)
```

---

# 📝 Question 7

What is the output?

```python
print(type(phone) == Smartphone)
print(type(phone) == Device)
```

---

# 📝 Question 8

What is the output?

```python
print(isinstance(computer, Device))
print(isinstance(computer, Smartphone))
```

---

# 📝 Question 9

Define a subclass of `Laptop` named `GamingLaptop`.

Override the `__str__()` method so that it returns:

```
High performance gaming machine!
```

Write the class definition.

---

# 📝 Question 10 (Conceptual – Attribute Lookup)

If the following code is added:

```python
class Tablet(Device):
    pass

tab = Tablet("Lenovo")
print(tab.brand)
```

Explain why `tab.brand` works even though `Tablet` does not define `brand`.

---

# 🚀 Concepts Covered

- Inheritance
- Method Overriding
- `super()`
- Class variables
- `issubclass()`
- `isinstance()`
- `is` operator
- `type()` comparison
- Attribute lookup order
- Object identity

---

# 🎯 PCAP Strategy Reminder

When solving inheritance problems:

1. Trace object creation carefully.
2. Track class variable increments.
3. Understand method overriding.
4. Distinguish between:
   - `is`
   - `==`
   - `type()`
   - `isinstance()`
5. Remember attribute lookup order:
   - Object → Class → Parent → Error

---

Practice these carefully — inheritance questions are common in PCAP.