# What is a Module ?
# --> A module is a simple .py file that contains reusable code.
# A module can contain:

# 1. Functions
# 2. Variables
# 3. Classes
# 4. Constants

# Banking App --> transactions ,loans, accounts, customers
# | -> transactions.py --> bank.deposit(), bank.withdraw()
# | -> accounts.py --> bank.check_bakance()
# | -> loans.py
# | -> main.py

# import math
# Variables and functions from the module must be accessed using the dot notation.

# print(math.sqrt(25))
# print(math.pi)


# import math, random, calendar, datetime

# from math import *  # --> This imports everything from math module and dot notation is not
# required.
# Not preferred method.
from math import sqrt,pi # This only imports sqrt()
print(sqrt(25))
print(pi)

def sqrt(x):
    # Customised function
    return x**(0.5)

# math.sqrt() --> So that it never creates confusion.

# Use aliases.
import math as m

# from math import sqrt as mathSqrtFunctionImported

print(m.sqrt(25))