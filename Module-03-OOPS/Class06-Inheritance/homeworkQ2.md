# 🎓 Smart University Role System – Advanced OOP Challenge

You are hired to design a **Smart University Management System**.  
The university has different types of people working and studying in it.

All people share some common properties, but their responsibilities differ.

You must design the class hierarchy properly using **inheritance**, override methods correctly, use `super()` wherever required, maintain shared counters, and demonstrate polymorphism using only `print()` statements.

This challenge is slightly more complex than a basic inheritance example.

---

# 🎯 Your Task

## 🔹 1️⃣ Create the Base Class: `Person`

- Instance variables:
  - `name`
  - `age`

- Class variable:
  - `total_people` (counts all created people)

- Constructor:
  - Accepts `name` and `age`
  - Increments `total_people`

- Method:
  - `get_role()` → returns `"Person"`

- Method:
  - `activity()` → returns `"Doing general activities"`

- Override `__str__()`:
  - `"Person: <name>, Age: <age>"`

---

## 🔹 2️⃣ Create Class: `Student`

- Inherit from `Person`
- Add instance variable:
  - `major`

- Override:
  - `get_role()` → `"Student"`
  - `activity()` → `"Studying <major>"`

- Override `__str__()` using `super()` so it becomes:
  - `"Student -> <Parent __str__ output>, Major: <major>"`

---

## 🔹 3️⃣ Create Class: `Professor`

- Inherit from `Person`
- Add instance variable:
  - `department`

- Override:
  - `get_role()` → `"Professor"`
  - `activity()` → `"Teaching in <department> department"`

- Override `__str__()` using `super()`

---

## 🔹 4️⃣ Create Class: `ResearchProfessor`

- Inherit from `Professor`
- Add instance variable:
  - `research_field`

- Override:
  - `get_role()` → `"Research Professor"`
  - `activity()` → `"Researching <research_field>"`

- Override `__str__()` using `super()`

---

# 🧪 Create the Following Objects

```
s1 = Student("Alice", 20, "Computer Science")
s2 = Student("Bob", 22, "Mathematics")
p1 = Professor("Dr. Smith", 45, "Physics")
rp1 = ResearchProfessor("Dr. Brown", 50, "Biology", "Genetics")
```

---

# 🖨 Now, Using ONLY `print()` Statements, Display the Following

---

## 🔹 Part 1 – String Representation

Print:
- `s1`
- `p1`
- `rp1`

---

## 🔹 Part 2 – Class Relationships

Print:
- Is `Student` a subclass of `Person`?
- Is `ResearchProfessor` a subclass of `Professor`?
- Is `Professor` a subclass of `Student`?

---

## 🔹 Part 3 – Instance Checks

Print:
- Is `s1` an instance of `Person`?
- Is `rp1` an instance of `Professor`?
- Is `p1` an instance of `Student`?

---

## 🔹 Part 4 – Identity Checks

Print:
- `s1 is s2`
- `s1 is s1`

---

## 🔹 Part 5 – Class Variable Tracking

Print:
- Total number of people created.

Explain (in comments) how this number is calculated.

---

## 🔹 Part 6 – Polymorphism in Action

Print:
- `s1.activity()`
- `p1.activity()`
- `rp1.activity()`

Explain why different outputs are produced even though the method name is the same.

---

## 🔹 Part 7 – Dynamic Dispatch Test

Create:

```
university = [s1, s2, p1, rp1]
```

Using a loop, print:
- Each person object
- Each person's role using `get_role()`
- Each person's activity

Observe how Python automatically selects the correct overridden method.

---

# 🧠 Concepts This Assignment Tests

- Multi-level inheritance  
- Method overriding  
- `super()`  
- `__str__()`  
- Class variables  
- Instance variables  
- `issubclass()`  
- `isinstance()`  
- `is` operator  
- Polymorphism  
- Dynamic method binding  

---

# 🚀 Goal

Design a clean inheritance hierarchy and demonstrate deep understanding of:

- Object identity  
- Runtime polymorphism  
- Method resolution  
- Shared vs individual state  

This is a complete real-world OOP modeling challenge.