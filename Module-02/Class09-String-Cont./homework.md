# 🌍 Advanced Real-Life String Challenges (Medium Level)

These problems simulate **real-world systems** and require you to use:

- String methods
- Iteration
- Pattern building
- Validation logic
- Formatting

---

# 🧾 1. Digital Billboard Formatter (Advertising System)

A digital billboard displays messages, but it has a constraint:

- Each line can only hold **10 characters**
- Words should NOT break across lines

### Task

Given a sentence:

```
"Big sale today only hurry up"
```

Display it like:

```
Big sale
today only
hurry up
```

---

### Requirements

- Split words properly
- Combine words using `join()`
- Maintain word integrity
- Ignore extra spaces

---

# 🔐 2. License Key Validator (Software Activation System)

A software license key must follow this format:

```
XXXX-XXXX-XXXX
```

Where:
- Each X is **uppercase letter or digit**
- Exactly **3 groups**
- Each group has **4 characters**

---

### Task

Validate whether a given key is valid:

```
AB12-CD34-EF56
```

---

### Requirements

- Check format
- Check characters
- Check length of each part

---


# 🏥 3. Medical Report Analyzer (Hospital System)

A patient report contains:

```
"Patient: John Age: 45 BP: 120/80 Status: stable"
```

---

### Task

Extract:

- Patient Name
- Age
- Blood Pressure

---

### Expected Output

```
Name: John
Age: 45
BP: 120/80
```


---

# 🧠 4. Secret Pattern Generator (Game System)

A game generates a secret visual pattern using characters.

Given input:

```
"GAME"
```

Generate pattern:

```
G A M E
G A M
G A
G
```

---

### Requirements

- Use string slicing
- Print decreasing pattern
- Maintain spacing


---

# 🚗 5. Smart Parking Slot Decoder (IoT System)

A parking system stores slots like:

```
"A1,B2,C3,D4,E5"
```

Each slot has:

- Letter → Parking zone
- Number → Slot number

---

### Task

Convert into:

```
Zone A → Slot 1
Zone B → Slot 2
Zone C → Slot 3
Zone D → Slot 4
Zone E → Slot 5
```

---

### Requirements

- Parse each entry
- Separate letters and numbers
- Format output properly


---

