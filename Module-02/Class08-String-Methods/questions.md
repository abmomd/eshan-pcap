# 🌍 Real-Life String Processing Problems

These exercises simulate **real-world applications** where string manipulation is required.  
Use appropriate Python string methods to solve them.

---

# 🧾 1. Customer Name Formatter (Bank System)

A bank stores customer names entered by users.  
However, users sometimes enter names with:

- Extra spaces
- Wrong capitalization

Example input:

```
"   aLIce   jOhNsOn   "
```

### Task

Write a program that:

- Removes extra spaces
- Converts the name into proper format

Expected output:

```
Alice Johnson
```



---

# 📧 2. Email Domain Analyzer (Cybersecurity System)

A cybersecurity system needs to detect whether an email belongs to the company domain.

Example emails:

```
alice@company.com
bob@gmail.com
charlie@company.com
```

### Task

Write a program that:

- Extracts the domain of each email
- Counts how many belong to `"company.com"`

### Expected Output

```
Company emails: 2
```


---

# 🛒 3. Product Code Validator (E-commerce System)

An online store generates product codes such as:

```
AB123
A12
12345
XY99Z
```

### Task

A valid product code must:

- Contain **letters and digits only**
- Start with **two letters**
- Have total length **5**

Print valid product codes only.



---

# 📱 4. Phone Number Cleaner (Contact App)

Users sometimes save phone numbers like:

```
"+91-98765-43210"
"98765 43210"
"(98765)43210"
```

### Task

Convert them into standard format:

```
9876543210
```



---

# 🧑‍💻 5. Username Generator (Social Media App)

Given a user's full name:

```
"John Michael Doe"
```

Generate a username using:

- First name
- First letter of middle name
- Last name

Expected username:

```
john_m_doe
```


---

# 📊 6. Log File Error Counter (DevOps Monitoring)

A system log contains entries:

```
INFO Server started
ERROR Database connection failed
WARNING Memory usage high
ERROR File not found
INFO Backup completed
```

### Task

Count how many log entries contain `"ERROR"`.


---

# 🎓 7. Student Data Parser (School Database)

Student data arrives as:

```
"John,Math,85"
"Sarah,Physics,90"
"Mike,Math,78"
```

### Task

Extract and print **only students enrolled in Math**.

Expected output:

```
John
Mike
```

---

# 🔐 8. Password Strength Checker (Security System)

A password is valid if:

- Contains at least **one uppercase letter**
- Contains at least **one lowercase letter**
- Contains at least **one digit**

Example:

```
Password123
```

### Task

Check whether the password is valid.


---

# 🚗 9. License Plate Formatter (Traffic System)

License plates are entered inconsistently:

```
"ka01ab1234"
"KA 01 AB 1234"
"ka-01-ab-1234"
```

Convert them into:

```
KA01AB1234
```


---

# 🧠 10. Secret Message Decoder (Game System)

A secret message contains random capitalization:

```
"hElLo WoRLd"
```

Your program should **swap letter cases**.

Expected output:

```
HeLlO wOrlD
```

---

# ⭐ Bonus Challenge – Text Analyzer

Given a paragraph:

```
Python is powerful. Python is easy to learn. Python is widely used.
```

Write a program that prints:

- Number of words
- Number of times `"Python"` appears
- The word with the highest Unicode value



---

# 🎯 Goal of These Exercises

These problems help practice:

- Real-world text processing
- String validation
- Data cleaning
- Security checks
- Log analysis
- User input formatting
- Automation scripts

Mastering string methods is essential for:

- Web development
- Data science
- Cybersecurity
- Backend engineering
- Automation tools