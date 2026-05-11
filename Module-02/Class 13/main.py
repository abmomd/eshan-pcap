

## Exceptions in Python

# What is an Exception ?
# --> Invalid Input, Division by Zero, File not found, Mathematical Errors, Accessing Invalid Indexes.


# print(10/0)  # ZeroDivisionError: division by zero

# try :
#     # risky code
#
# except Exception Type 1:
#
#     # Error Handling

# except Exception Type 2:
# except: # Final General exception


# -->  Executes Try Block --> No Error, Except Block is skipped --> If Error, Enters Except Block.


try:
    num = int(input("Enter a number: "))
    print(100 / num)

except ZeroDivisionError:
    print("You  have entered a Zero. ")

except : # Handles all the cases, when we don't know the type of exception
    print("Please enter a number.")


print("Program Continues as Expected.")


# Common Exceptions
# 1. ValueError -> Invalid Value
# 2. TypeError --> Wrong Data Type
# 3. ZeroDivisionError --> division by Zero
# 4. IndexError --> Invalid Index
# 5. KeyError --> Missing Dictionary Key
# 6. FileNotFoundError --> File Missing
# 7. AttributeError --> Invalid Attribute.

# ATM Withdrawal

try:
    amount = int(input("Enter Withdrawal amount: "))
    balance = 5000

    assert amount <= balance

except  AssertionError:
    print(f"Repeat The process, Enter a value below {balance}.")
except ValueError:
    print("Please enter a number.")


try:
    file = open("test.txt")
    print(file.read())
except FileNotFoundError:
    print("File not found.")


# Heirarchy

# BaseException
#  ├── Exception
#       ├── ArithmeticError
#       │     ├── ZeroDivisionError
#       │     └── OverflowError
#       │
#       ├── LookupError
#       │     ├── IndexError
#       │     └── KeyError
#       │
#       ├── ValueError
#       └── TypeError

try:
    num = int(input("Enter a number: "))
    print(100/num)

except ZeroDivisionError:
    print("You  have entered a 0")

except ArithmeticError :
    print("You  have entered a Arithmetic Error.")


age = -5

# if age < 0:
#     raise ValueError

# Assertion Error:

x = -10
assert x > 0