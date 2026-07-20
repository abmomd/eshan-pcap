# 📚 Python Standard Library Modules (`dir`, `math`, `random`, `platform`)

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- Explore the contents of a module using `dir()`.
- Use commonly used functions from the `math` module.
- Generate pseudo-random numbers using the `random` module.
- Retrieve information about your computer using the `platform` module.
- Find and explore Python modules using the Python Module Index.

---

# 🧠 1. What is Python's Standard Library?

Python comes with hundreds of built-in modules that provide ready-to-use functionality.

These modules help you perform tasks like:

- Mathematical calculations
- Random number generation
- Operating system interaction
- Date and time operations
- Networking
- File handling
- Data compression
- JSON processing

Instead of writing everything from scratch, you simply import the module.

---

## Real-Life Example

Imagine building an **Online Shopping Website**.

Instead of writing your own:

- Square root calculator
- Random coupon generator
- Operating system detector

you simply import:

```python
import math
import random
import platform
```

---

# 🔍 2. Exploring Modules with `dir()`

Sometimes you don't know what functions a module provides.

Python offers:

```python
dir(module_name)
```

It returns all the functions, variables, constants, and classes inside a module.

---

## Example

```python
import math

print(dir(math))
```

Output (shortened):

```text
['acos',
 'asin',
 'atan',
 'ceil',
 'cos',
 'degrees',
 'e',
 'exp',
 'factorial',
 'floor',
 'gcd',
 'log',
 'pi',
 'pow',
 'radians',
 'sin',
 'sqrt',
 ...]
```

---

## Real-Life Example

A programmer joins a new project and finds an unfamiliar module.

Instead of opening documentation immediately, they use:

```python
dir(module)
```

to quickly explore available functions.

---

# ➗ 3. The `math` Module

The `math` module provides more than **50 mathematical functions and constants**.

Import it using:

```python
import math
```

---

# Common Constants

## π (Pi)

```python
import math

print(math.pi)
```

Output

```text
3.141592653589793
```

---

## Euler's Number

```python
print(math.e)
```

Output

```text
2.718281828459045
```

---

# Common Functions

## Square Root

```python
math.sqrt(49)
```

Output

```text
7.0
```

---

## Power

```python
math.pow(2,5)
```

Output

```text
32.0
```

---

## Factorial

```python
math.factorial(5)
```

Output

```text
120
```

---

## Ceiling

Rounds upward.

```python
math.ceil(4.2)
```

Output

```text
5
```

---

## Floor

Rounds downward.

```python
math.floor(4.9)
```

Output

```text
4
```

---

## Trigonometry

```python
math.sin()

math.cos()

math.tan()
```

---

## Exponential Function

```python
math.exp(1)
```

Output

```text
2.718281828...
```

Notice:

```python
math.exp(1) == math.e
```

returns

```python
True
```

---

## Real-Life Applications

- Scientific Calculators
- Engineering Software
- Machine Learning
- Finance
- Computer Graphics
- Robotics

---

# 🎲 4. The `random` Module

Computers cannot generate truly random numbers.

Instead, Python generates **pseudo-random numbers**.

Import:

```python
import random
```

---

# randint()

Generate an integer.

```python
random.randint(1,10)
```

Possible Output

```text
7
```

---

# random()

Returns a decimal between 0 and 1.

```python
random.random()
```

Example

```text
0.634812
```

---

# choice()

Selects one random item.

```python
colors = ["Red","Blue","Green"]

print(random.choice(colors))
```

Possible Output

```text
Blue
```

---

# shuffle()

Randomly rearranges a list.

```python
cards = [1,2,3,4,5]

random.shuffle(cards)

print(cards)
```

Possible Output

```text
[3,5,1,2,4]
```

---

# seed()

Sets the starting point of the random number generator.

```python
random.seed(100)
```

Now every execution produces the same sequence.

---

## Why Use `seed()`?

Useful for:

- Debugging
- Unit Testing
- Scientific Simulations
- Machine Learning Experiments

---

## Real-Life Example

An online exam system wants every student to receive the **same shuffled questions** during testing.

Using:

```python
random.seed(100)
```

ensures reproducible results.

---

# 🖥️ 5. The `platform` Module

This module provides information about your computer and operating system.

Import:

```python
import platform
```

---

# platform.system()

Returns the operating system.

```python
print(platform.system())
```

Example

```text
Windows
```

or

```text
Linux
```

---

# platform.release()

Returns the OS release.

```python
print(platform.release())
```

Example

```text
11
```

---

# platform.version()

Returns detailed OS version.

---

# platform.machine()

Returns processor architecture.

```python
print(platform.machine())
```

Example

```text
x86_64
```

---

# platform.processor()

Returns CPU name.

```python
print(platform.processor())
```

Example

```text
Intel64 Family 6 Model 165
```

---

# platform.python_version()

Returns Python version.

```python
print(platform.python_version())
```

Example

```text
3.12.4
```

---

# platform.python_version_tuple()

Returns version as a tuple.

```python
print(platform.python_version_tuple())
```

Output

```python
('3','12','4')
```

Length

```python
len(platform.python_version_tuple())
```

Output

```text
3
```

---

## Real-Life Applications

- Installers
- Software Updaters
- Cross-platform Applications
- Bug Reporting
- System Diagnostics

---

# 🌐 6. Python Module Index

Python provides an official directory of all standard library modules.

Documentation:

https://docs.python.org/3/py-modindex.html

Use it whenever you need a module for a particular task.

Examples include:

- `json`
- `csv`
- `datetime`
- `pathlib`
- `sqlite3`
- `zipfile`
- `statistics`

---

# 📊 Summary of Common Functions

## `math`

| Function | Purpose |
|-----------|---------|
| pi | Pi constant |
| e | Euler constant |
| sqrt() | Square root |
| pow() | Power |
| factorial() | Factorial |
| ceil() | Round up |
| floor() | Round down |
| exp() | Exponential |

---

## `random`

| Function | Purpose |
|-----------|---------|
| randint() | Random integer |
| random() | Random decimal |
| choice() | Random element |
| shuffle() | Shuffle list |
| seed() | Fixed random sequence |

---

## `platform`

| Function | Purpose |
|-----------|---------|
| system() | Operating System |
| release() | OS Release |
| version() | OS Version |
| machine() | Architecture |
| processor() | CPU Name |
| python_version() | Python Version |
| python_version_tuple() | Version Tuple |

---

# 🧪 Exercise 1

## Question

```python
import math

result = math.e == math.exp(1)
```

### Answer

```python
True
```

### Explanation

`math.exp(1)` computes **e¹**, which is exactly Euler's number (`math.e`).

---

# 🧪 Exercise 2

## Question

Setting the same seed every time guarantees that...

### Answer

The program generates **the same sequence of pseudo-random numbers** every time it runs.

---

# 🧪 Exercise 3

## Question

Which function returns the CPU name?

### Answer

```python
platform.processor()
```

---

# 🧪 Exercise 4

## Question

```python
import platform

print(len(platform.python_version_tuple()))
```

### Answer

```text
3
```

Because the tuple contains:

```python
('major', 'minor', 'patch')
```

For example:

```python
('3', '12', '4')
```

---

# ⚠️ Common Mistakes

### Forgetting the Module Prefix

❌

```python
sqrt(25)
```

✅

```python
math.sqrt(25)
```

---

### Assuming Random Numbers Are Truly Random

Python uses **pseudo-random algorithms**, not true randomness.

---

### Forgetting to Set a Seed for Reproducible Results

If consistent outputs are required (e.g., testing), always use:

```python
random.seed(42)
```

---

### Confusing `platform.machine()` and `platform.processor()`

- `machine()` → Hardware architecture (e.g., `x86_64`)
- `processor()` → CPU model/name

---

# 🚀 Best Practices

- Use `dir()` to explore unfamiliar modules.
- Prefer the `math` module over manually implementing mathematical functions.
- Use `random.seed()` for repeatable experiments and testing.
- Use the `platform` module when writing software that must work across different operating systems.
- Consult the **Python Module Index** before creating your own utility functions—there is often already a built-in module for the task.

---

# 🎯 Final Summary

| Module | Purpose |
|--------|---------|
| `dir()` | Explore module contents |
| `math` | Mathematical operations and constants |
| `random` | Pseudo-random number generation |
| `platform` | Retrieve OS, hardware, and Python information |
| Python Module Index | Discover available standard library modules |

---

# 🧠 Final Thought

The Python Standard Library is one of Python's greatest strengths. Learning how to explore modules with `dir()`, perform calculations with `math`, generate reproducible random values with `random`, and inspect the execution environment with `platform` will help you write more powerful, maintainable, and portable Python programs.