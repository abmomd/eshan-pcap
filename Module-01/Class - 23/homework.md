# 🏠 Homework 1: University Student Management System

## 📘 Story

A university wants to organize its student management software using Python packages.

Instead of writing everything in one file, the software should be divided into different modules.

---

## 📂 Create the following project structure

```
University/

│
├── university/
│   ├── __init__.py
│   ├── students.py
│   ├── courses.py
│   └── grades.py
│
└── main.py
```

---

## Your Tasks

### students.py

Implement:

- add_student(name)
- remove_student(name)

---

### courses.py

Implement:

- enroll_course(student, course)
- display_courses()

---

### grades.py

Implement:

- assign_grade(student, grade)
- display_grades()

---

### main.py

Import the modules correctly and simulate the following:

1. Add two students.
2. Enroll them into courses.
3. Assign grades.
4. Display all information.

---

## Requirements

- Use at least one module alias.
- Import one function using `from ... import ...`.
- Include an `__init__.py` file.

# 🏠 Homework 2: Smart Restaurant Ordering System

## 📘 Story

A restaurant is developing a command-line ordering application.

The project should be organized into packages.

---

## 📂 Project Structure

```
Restaurant/

│
├── restaurant/
│   ├── __init__.py
│   ├── menu.py
│   ├── orders.py
│   └── billing.py
│
└── main.py
```

---

## Implement

### menu.py

- display_menu()

---

### orders.py

- place_order(item)
- cancel_order(item)

---

### billing.py

- generate_bill(order_list)
- calculate_tax(total)

---

### main.py

Create a complete ordering flow:

1. Display menu.
2. Take multiple orders.
3. Generate the bill.
4. Calculate tax.
5. Display the final payable amount.

---

## Requirements

- Use proper package imports.
- Use aliases wherever appropriate.
- Create meaningful functions.

# 🏠 Homework 3: Space Mission Control Package

## 📘 Story

A space agency is building software to manage rocket launches.

Different responsibilities are separated into different modules.

---

## 📂 Project Structure

```
MissionControl/

│
├── mission/
│   ├── __init__.py
│   ├── astronauts.py
│   ├── rockets.py
│   ├── launch.py
│   └── telemetry.py
│
└── main.py
```

---

## Implement

### astronauts.py

- assign_astronaut(name)

---

### rockets.py

- prepare_rocket()

---

### launch.py

- launch_mission()

---

### telemetry.py

- display_status()

---

### main.py

Create a mission sequence:

1. Assign astronauts.
2. Prepare rocket.
3. Launch mission.
4. Display telemetry.

---

## Bonus

Create a private helper function named:

```
_log_internal_data()
```

Use it inside the module but do not call it directly from `main.py`.


# 🏠 Homework 4: Hospital Management Package

## 📘 Story

A hospital wants to manage patients, doctors, and appointments using modular software.

---

## 📂 Project Structure

```
Hospital/

│
├── hospital/
│   ├── __init__.py
│   ├── patients.py
│   ├── doctors.py
│   ├── appointments.py
│   └── reports.py
│
└── main.py
```

---

## Implement

### patients.py

- admit_patient(name)
- discharge_patient(name)

---

### doctors.py

- add_doctor(name)

---

### appointments.py

- book_appointment(patient, doctor)

---

### reports.py

- generate_report()

---

### main.py

Create a complete simulation that:

1. Admits patients.
2. Adds doctors.
3. Books appointments.
4. Generates a hospital report.

---

## Requirements

- Use package imports.
- Import at least one function using an alias.
- Demonstrate why private functions should not be called directly.


# 🏠 Homework 5: Online Shopping Package

## 📘 Story

You are developing a small e-commerce application. To keep the project maintainable, the code should be split into packages.

---

## 📂 Project Structure

```
Shop/

│
├── shop/
│   ├── __init__.py
│   ├── products.py
│   ├── cart.py
│   ├── payment.py
│   └── delivery.py
│
└── main.py
```

---

## Implement

### products.py

- display_products()

---

### cart.py

- add_to_cart(product)
- remove_from_cart(product)

---

### payment.py

- process_payment(amount)

---

### delivery.py

- schedule_delivery(address)

---

### main.py

Simulate a shopping experience:

1. Display products.
2. Add multiple items to the cart.
3. Remove one item.
4. Process payment.
5. Schedule delivery.

---

## Bonus Challenge

Create a custom directory named:

```
SharedModules/
```

Move the `shop` package into it and modify `sys.path` so that your program can still import the package successfully.

---

## Concepts Covered

- Packages
- Modules
- `__init__.py`
- `sys.path.append()`
- `import`
- `from ... import ...`
- Module aliases
- Package organization
- Private helper functions
- Real-world software architecture

