# 📦 Python Packages and Modules – Complete Notes

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- Understand the difference between modules and packages.
- Understand how Python imports modules.
- Learn about the `__pycache__` directory.
- Understand private variables and functions.
- Learn what a shebang (`#!`) is.
- Add custom package locations using `sys.path`.
- Understand the purpose of the `__init__.py` file.
- Import modules from packages.

---

# 🧠 1. Module vs Package

Many beginners confuse **modules** and **packages**.

They are related but different.

---

## Module

A **module** is a single Python file.

Example:

```text
math.py
```

or

```text
bank.py
```

A module can contain:

- Functions
- Variables
- Classes
- Constants

Example:

```python
# calculator.py

def add(a, b):
    return a + b
```

---

## Package

A **package** is a collection of related modules stored inside a directory.

Example:

```text
shopping/

    billing.py

    inventory.py

    payment.py

    shipping.py
```

Here,

```text
shopping
```

is the package.

The files inside are modules.

---

## Real-Life Example

Imagine an online shopping website.

Instead of putting everything into one huge file:

```text
shopping.py
```

we organize it.

```text
shopping/

    billing.py

    inventory.py

    payment.py

    customer.py

    reports.py
```

This makes the project:

- Easier to understand
- Easier to maintain
- Easier for teams to work together

---

# 📦 Module vs Package

| Module | Package |
|---------|----------|
| Single `.py` file | Directory containing modules |
| Contains functions/classes | Contains multiple modules |
| Small reusable unit | Larger reusable collection |

---

# 🧠 2. What Happens During Import?

Suppose you write:

```python
import math
```

Python performs several steps.

### Step 1

Looks for the module.

↓

### Step 2

Reads the source code.

↓

### Step 3

Compiles it into bytecode.

↓

### Step 4

Stores the compiled version inside:

```text
__pycache__
```

---

# 🗂️ The `__pycache__` Folder

Example project:

```text
project/

    main.py

    calculator.py

    __pycache__/

        calculator.cpython-312.pyc
```

---

## Why Does Python Create It?

Because compiled code loads faster than source code.

The next time the program runs,

Python directly loads:

```text
.pyc
```

instead of compiling again.

This improves performance.

---

## Real-Life Example

Imagine translating a book every time you read it.

Instead,

you translate it once,

save the translated version,

and reuse it forever.

That's exactly what `__pycache__` does.

---

# 🔒 3. Private Variables and Functions

Python does not truly support private members.

Instead,

it uses a naming convention.

---

## Single Underscore

```python
_balance = 1000
```

Means:

```text
Internal use only.
```

---

## Double Underscore

```python
__password = "secret"
```

Also indicates:

```text
Do not use outside the module/class.
```

---

## Important

Python **does not prevent access**.

It is only a recommendation for developers.

---

## Example

```python
# bank.py

_balance = 5000

def _calculate_interest():
    pass
```

Users should avoid calling:

```python
bank._calculate_interest()
```

although Python allows it.

---

## Why Use Private Members?

Suppose a banking module contains:

```python
calculate_interest()

verify_pin()

encrypt_password()

_internal_database_update()
```

Only the first three should be used publicly.

The fourth is meant only for the module itself.

---

# 🐧 4. Shebang (`#!`)

A **shebang** tells Unix/Linux which interpreter should execute the file.

Example:

```python
#!/usr/bin/python3
```

or

```python
#!/usr/bin/env python3
```

---

It always appears at the first line.

Example:

```python
#!/usr/bin/env python3

print("Hello")
```

---

## Other Names

All of these refer to the same thing.

- Shebang
- Shabang
- Hashbang
- Poundbang
- Hashpling

---

## Important

The shebang works only on:

- Linux
- macOS
- Unix

It has **no effect on Windows**.

---

## Real-Life Example

Suppose your computer has:

```text
Python 3.10

Python 3.12
```

The shebang tells Linux exactly which interpreter to use.

---

# 📂 5. Importing Packages from Custom Locations

Normally,

Python searches only a few predefined folders.

Example:

```python
import sys

print(sys.path)
```

Output:

```text
[
'C:\\Python312',
'project',
...
]
```

---

Suppose your package exists here:

```text
D:\Python\Project\Modules
```

Python cannot find it automatically.

You must add it.

---

## Example

```python
import sys

sys.path.append(r"D:\Python\Project\Modules")
```

Now Python will search this folder as well.

---

## Real-Life Example

Company projects often keep reusable packages in a shared directory.

Instead of copying files,

developers simply add the directory to:

```python
sys.path
```

---

# 📦 Importing from Packages

Suppose we have:

```text
Modules/

    abc/

        __init__.py

        def/

            __init__.py

            mymodule.py
```

Then we can write:

```python
from abc.def.mymodule import *
```

or

```python
import abc.def.mymodule
```

---

# 📄 6. The `__init__.py` File

Every package usually contains:

```text
__init__.py
```

Example:

```text
shopping/

    __init__.py

    billing.py

    inventory.py

    payment.py
```

---

## What Does It Do?

When Python imports the package,

it first executes:

```text
__init__.py
```

This file is used to:

- Initialize the package
- Import common modules
- Define package-level variables
- Perform setup tasks

---

## Example

```python
print("Shopping Package Loaded")
```

Whenever:

```python
import shopping
```

Python first prints:

```text
Shopping Package Loaded
```

---

## Can It Be Empty?

Yes.

Many packages contain:

```python
# __init__.py
```

with nothing inside.

Its existence simply tells Python:

```text
This directory is a package.
```

---

# 📊 Summary

## Module

```text
calculator.py
```

---

## Package

```text
shopping/

    billing.py

    payment.py

    inventory.py
```

---

## Import Process

```text
.py

↓

Compile

↓

.pyc

↓

Stored in __pycache__
```

---

# 🧪 Exercise 1

## Question

Prevent users from running your module directly.

### Answer

```python
if __name__ == "__main__":
    print("This module is not intended to be run directly.")
```

This block ensures that code inside it runs only when the file is executed directly, not when it is imported.

---

# 🧪 Exercise 2

## Question

Packages are stored in:

```text
D:\Python\Project\Modules
```

### Answer

```python
import sys

sys.path.append(r"D:\Python\Project\Modules")
```

---

# 🧪 Exercise 3

## Directory

```text
abc/

    def/

        mymodule.py
```

### Answer

```python
from abc.def.mymodule import *
```

or

```python
import abc.def.mymodule
```

---

# 🌍 Real-Life Applications

## Banking Software

```text
bank/

    accounts.py

    loans.py

    transactions.py
```

---

## E-Commerce

```text
shopping/

    billing.py

    inventory.py

    payment.py
```

---

## AI Projects

```text
ai/

    preprocessing.py

    training.py

    prediction.py
```

---

## Web Development

```text
website/

    routes.py

    database.py

    authentication.py
```

---

# ⚠️ Common Mistakes

### Forgetting `__init__.py`

Without it (in traditional package layouts), Python may not recognise the directory as a package.

---

### Modifying Private Members

Avoid using members beginning with:

```python
_
```

or

```python
__
```

unless you understand the package internals.

---

### Assuming `__pycache__` Should Be Edited

Never modify `.pyc` files manually.

Python generates them automatically.

---

### Hardcoding Import Paths

Prefer proper package structures.

Only use:

```python
sys.path.append()
```

when necessary.

---

# 🚀 Best Practices

- Organise related modules into packages.
- Keep reusable code inside packages.
- Use `__init__.py` to initialise packages.
- Treat `_` and `__` members as internal.
- Don't delete `__pycache__` unless troubleshooting.
- Use `sys.path.append()` only when working with custom package locations.

---

# 🎯 Final Summary

| Concept | Purpose |
|----------|---------|
| Module | Single Python file |
| Package | Collection of related modules |
| `__pycache__` | Stores compiled `.pyc` files |
| `_name` / `__name` | Marks members as internal/private by convention |
| Shebang (`#!`) | Specifies the interpreter on Unix-like systems |
| `sys.path.append()` | Adds custom module search locations |
| `__init__.py` | Initialises a package when imported |

---

# 🧠 Final Thought

Packages are what make large Python projects manageable. By grouping related modules together, using `__init__.py` for initialisation, and understanding how Python searches and caches modules, you can build applications that are organised, reusable, and easy to maintain.