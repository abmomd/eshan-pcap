# 🌍 Solutions – Advanced Real-Life String Challenges

---

# 🧾 1. Digital Billboard Formatter

## ✅ Solution

```python
def billboard(text):
    words = text.split()
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) <= 10:
            current_line.append(word)
            current_length += len(word)
        else:
            print(" ".join(current_line))
            current_line = [word]
            current_length = len(word)

    if current_line:
        print(" ".join(current_line))


billboard("Big sale today only hurry up")
```

---

## 🧠 Explanation

- `split()` → get words
- Track current line length
- Use `" ".join()` to print lines
- Prevent breaking words

---

# 🔐 2. License Key Validator

## ✅ Solution

```python
def validate_key(key):
    parts = key.split("-")

    if len(parts) != 3:
        return False

    for part in parts:
        if len(part) != 4 or not part.isalnum() or not part.upper() == part:
            return False

    return True


print(validate_key("AB12-CD34-EF56"))  # True
print(validate_key("ab12-CD34-EF56"))  # False
```

---

## 🧠 Explanation

- `split("-")` → break groups
- `isalnum()` → only letters/digits
- `upper()` → ensure uppercase

---

# 🏥 3. Medical Report Analyzer

## ✅ Solution

```python
def extract_report(report):
    parts = report.split()

    name = parts[1]
    age = parts[3]
    bp = parts[5]

    print("Name:", name)
    print("Age:", age)
    print("BP:", bp)


extract_report("Patient: John Age: 45 BP: 120/80 Status: stable")
```

---

## 🧠 Explanation

- Split string
- Extract fixed positions
- Simple parsing logic

---

# 🧠 4. Secret Pattern Generator

## ✅ Solution

```python
def pattern(word):
    for i in range(len(word), 0, -1):
        print(" ".join(word[:i]))


pattern("GAME")
```

---

## 🧠 Explanation

- Slice string → `word[:i]`
- Use `" ".join()` for spacing
- Loop in reverse

---

# 🚗 5. Smart Parking Slot Decoder

## ✅ Solution

```python
def decode_slots(data):
    slots = data.split(",")

    for slot in slots:
        zone = ""
        number = ""

        for ch in slot:
            if ch.isalpha():
                zone += ch
            elif ch.isdigit():
                number += ch

        print(f"Zone {zone} → Slot {number}")


decode_slots("A1,B2,C3,D4,E5")
```

---

## 🧠 Explanation

- Split using `,`
- Use `isalpha()` and `isdigit()`
- Build formatted output

---

# 🎯 Key Concepts Used

| Concept | Used In |
|--------|--------|
| `split()` | All problems |
| `join()` | Pattern & Billboard |
| `isalpha()` | Parking decoder |
| `isdigit()` | Parking decoder |
| `isalnum()` | License validator |
| `upper()` | License validator |
| slicing | Pattern generator |
| formatting | All outputs |

---
