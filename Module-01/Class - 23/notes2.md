# 📦 Installing Packages with pip – Complete Notes

# 🎯 Learning Objectives

By the end of this module, you will be able to:

- Understand what PyPI is.
- Learn what pip is and why it is used.
- Check the installed version of pip.
- Install, update, and uninstall Python packages.
- View package information and dependencies.
- Understand user-level vs system-wide installations.
- Learn common pip commands used in real projects.

---

# 🧠 1. What is PyPI?

**PyPI** stands for:

> **Python Package Index**

It is the official online repository for Python packages.

Think of it as an **App Store** or **Play Store** for Python libraries.

Whenever developers create useful Python packages, they can upload them to PyPI so that other developers can install and use them.

---

## Website

```
https://pypi.org/
```

---

## Another Name

PyPI is also known as:

> **The Cheese Shop**

This nickname comes from a famous comedy sketch and has become a long-standing nickname for the Python Package Index.

---

## Real-Life Example

Suppose you want to:

- Build websites
- Perform machine learning
- Read Excel files
- Create games
- Work with images

Instead of writing everything from scratch, you simply install packages from PyPI.

Examples:

| Package | Purpose |
|----------|---------|
| numpy | Numerical Computing |
| pandas | Data Analysis |
| matplotlib | Graphs and Charts |
| requests | HTTP Requests |
| flask | Web Development |
| pygame | Game Development |

---

# 🛠️ 2. What is pip?

**pip** is Python's package manager.

It downloads packages from PyPI and installs them on your computer.

Without pip, you would need to manually download, extract, and configure every package.

---

## Think of pip Like This

| App Store | Python |
|------------|--------|
| Google Play | PyPI |
| Install Button | pip install |

---

## Example

Instead of manually downloading the **requests** library,

simply type:

```bash
pip install requests
```

pip automatically:

- Downloads the package
- Installs it
- Installs any required dependencies

---

# 🖥️ 3. Checking pip Version

Before using pip, verify that it is installed.

Run either of the following commands:

```bash
pip --version
```

or

```bash
pip3 --version
```

---

## Example Output

```text
pip 25.1 from ...
```

---

## Why Two Commands?

Different operating systems configure Python differently.

Some systems use:

```bash
pip
```

Others use:

```bash
pip3
```

Check which one works on your machine.

---

# 📋 4. Common pip Commands

---

## View Help

```bash
pip help
```

Displays the available pip commands.

---

## List Installed Packages

```bash
pip list
```

Example:

```text
numpy
pandas
matplotlib
requests
```

---

## View Package Information

```bash
pip show requests
```

Example output:

```text
Name: requests
Version: 2.x.x
Location: ...
Requires: certifi, urllib3
```

Useful information includes:

- Version
- Installation location
- Dependencies
- Author
- License

---

## Search for Packages

```bash
pip search excel
```

Searches PyPI for packages whose names contain the specified keyword.

---

## Install a Package

```bash
pip install requests
```

Downloads and installs the package.

---

## Install for Current User Only

```bash
pip install --user requests
```

Use this when you do not have administrator privileges.

The package is installed only for your user account.

---

## Upgrade a Package

```bash
pip install -U requests
```

or

```bash
pip install --upgrade requests
```

Updates the package to the latest available version.

---

## Uninstall a Package

```bash
pip uninstall requests
```

Removes the package from your system.

---

# 📦 What Happens During Installation?

Suppose you run:

```bash
pip install requests
```

The process is:

```
User Command

↓

pip contacts PyPI

↓

Downloads package

↓

Downloads dependencies

↓

Installs package

↓

Ready to use
```

---

# 📂 Package Dependencies

Many packages depend on other packages.

Example:

```
requests

├── urllib3
├── certifi
├── charset-normalizer
└── idna
```

pip automatically installs all required dependencies.

---

# 👤 User Installation vs System Installation

## System-Wide Installation

```bash
pip install package_name
```

- Available to all users.
- Usually requires administrator rights.

---

## User Installation

```bash
pip install --user package_name
```

- Available only to the current user.
- Does not require administrator rights.

---

# 🌍 Real-Life Examples

## Data Science

```bash
pip install pandas
```

Used for:

- Reading CSV files
- Data cleaning
- Data analysis

---

## Machine Learning

```bash
pip install scikit-learn
```

Used to build machine learning models.

---

## Web Development

```bash
pip install flask
```

Used to create web applications.

---

## Image Processing

```bash
pip install pillow
```

Used for image editing and manipulation.

---

## HTTP Requests

```bash
pip install requests
```

Used to communicate with web APIs and websites.

---

# 🧪 Exercise 1

## Question

Where does the name **The Cheese Shop** come from?

### Answer

It is the nickname of the **Python Package Index (PyPI)**.

---

# 🧪 Exercise 2

## Question

Why should you check whether `pip` or `pip3` works?

### Answer

Different operating systems configure Python differently.

Some use:

```bash
pip
```

while others require:

```bash
pip3
```

You should use whichever command is recognised on your system.

---

# 🧪 Exercise 3

## Question

How can you determine whether pip works with Python 2 or Python 3?

### Answer

Run:

```bash
pip --version
```

or

```bash
pip3 --version
```

The output shows the associated Python version.

---

# 🧪 Exercise 4

## Question

You do not have administrator rights.

How can you install a package?

### Answer

Use:

```bash
pip install --user package_name
```

This installs the package only for your user account.

---

# ⚠️ Common Mistakes

## Forgetting Internet Connection

pip downloads packages from PyPI.

No internet means installation will fail.

---

## Using the Wrong Command

Some systems recognise:

```bash
pip
```

Others require:

```bash
pip3
```

---

## Installing Without Permissions

System-wide installation may fail without administrator rights.

Use:

```bash
pip install --user package_name
```

instead.

---

## Forgetting to Upgrade

Older package versions may lack new features or bug fixes.

Upgrade using:

```bash
pip install -U package_name
```

---

# 🚀 Best Practices

- Install packages only from trusted sources such as PyPI.
- Keep packages updated.
- Use `pip show` to inspect package details.
- Use `pip list` to review installed packages.
- Use `--user` if administrator privileges are unavailable.
- Remove unused packages to keep your environment clean.

---

# 📊 Summary of Common Commands

| Command | Purpose |
|----------|---------|
| `pip --version` | Check installed pip version |
| `pip help` | Display pip help |
| `pip list` | List installed packages |
| `pip show package_name` | Display package details |
| `pip search keyword` | Search PyPI for packages |
| `pip install package_name` | Install a package |
| `pip install --user package_name` | Install for current user only |
| `pip install -U package_name` | Upgrade a package |
| `pip uninstall package_name` | Remove a package |

---

# 🎯 Final Summary

- **PyPI** is the official repository for Python packages.
- **The Cheese Shop** is another name for PyPI.
- **pip** is the package manager used to install Python libraries.
- Use `pip --version` or `pip3 --version` to verify your installation.
- `pip list` displays installed packages.
- `pip show` provides package information.
- `pip install` installs packages.
- `pip install --user` installs packages without administrator rights.
- `pip install -U` updates packages.
- `pip uninstall` removes packages.

---

# 💡 Final Thought

One of Python's greatest strengths is its vast ecosystem of open-source libraries. Learning to use **pip** and **PyPI** allows you to quickly add powerful functionality to your projects without writing everything from scratch.