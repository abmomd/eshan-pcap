# 🏢 Smart Company Employee System – OOP Challenge

You have been hired to design a **Smart Employee Management System** for a growing tech company. The company has different types of employees such as Developers, Managers, and HR Managers. All employees share some common properties like name and salary, but each role performs different types of work.

Your task is to build this system using **inheritance in Python**. You must design the class hierarchy properly, override methods where needed, use `super()` correctly, maintain a shared employee counter, and then use only `print()` statements to demonstrate that your system works correctly.

---

## 🎯 Your Task

### 🔹 1️⃣ Create the Base Class `Employee`

- Create instance variables:
  - `name`
  - `salary`
- Create a class variable:
  - `total_employees` (should count how many employee objects are created)
- The constructor must:
  - Accept `name` and `salary`
  - Increment `total_employees`
- Create a method:
  - `work()` → returns `"General employee working"`
- Override `__str__()` so that it returns:
  - `"Employee: <name>, Salary: <salary>"`

---

### 🔹 2️⃣ Create Class `Developer`

- Inherit from `Employee`
- Override `work()` → return `"Writing code"`
- Override `__str__()` using `super()` so output becomes:
  - `"Developer -> <parent __str__ output>"`

---

### 🔹 3️⃣ Create Class `Manager`

- Inherit from `Employee`
- Override `work()` → return `"Managing team"`
- Override `__str__()` using `super()`

---

### 🔹 4️⃣ Create Class `HRManager`

- Inherit from `Manager`
- Override `work()` → return `"Hiring employees"`
- Override `__str__()` using `super()`

---

### 🔹 5️⃣ Create the Following Objects

Create:

```
dev1 = Developer("Alice", 80000)
dev2 = Developer("Bob", 90000)
mgr1 = Manager("Charlie", 120000)
hr1 = HRManager("Diana", 110000)
```

---

## 🖨 Now, Using ONLY `print()` Statements, Display the Following:

### 🔹 String Representation
- Print:
  - `dev1`
  - `mgr1`
  - `hr1`

---

### 🔹 Inheritance Relationship Checks
Print:
- Is `Developer` a subclass of `Employee`?
- Is `HRManager` a subclass of `Manager`?
- Is `Manager` a subclass of `Developer`?

---

### 🔹 Instance Checks
Print:
- Is `dev1` an instance of `Employee`?
- Is `hr1` an instance of `Manager`?
- Is `mgr1` an instance of `Developer`?

---

### 🔹 Identity Checks
Print:
- `dev1 is dev2`
- `dev1 is dev1`

---

### 🔹 Class Variable
Print:
- The total number of employees created.

---

### 🔹 Polymorphism Test
Print:
- `dev1.work()`
- `mgr1.work()`
- `hr1.work()`

---

### 🔹 Final Dynamic Dispatch Test

Create:

```
company = [dev1, dev2, mgr1, hr1]
```

Using a loop, print:
- Each employee object
- Each employee’s `work()` output

---

## 🧠 Concepts This Assignment Tests

- Inheritance  
- Method overriding  
- `super()`  
- `__str__()`  
- Class vs Instance variables  
- `issubclass()`  
- `isinstance()`  
- `is` operator  
- Polymorphism  
- Dynamic method resolution  

---

### 🚀 Goal

Design clean, structured classes and demonstrate full understanding of Python inheritance using only `print()` statements.