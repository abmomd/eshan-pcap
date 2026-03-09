# try:
# Tries some particular risky code (division by 0)
# except SomeException
# handling error code.
# else
    # RUNS IF NO EXCEPTION WAS FOUND.
# finally:
    # ALWAYS RUN : With or Without Exception


import math

try:
    print(math.sqrt(9))
except ValueError:
    print('Not Defined')
else:
    print('The Square root is possible.')
finally:
    print('The program is done.')



# To Capture Exception as an object.
# The exception object contatins :
# args -> tuple of arguments which is passed to an exception.

try:
    raise ValueError("Invalid Value", 404)
except ValueError as e:
    print(e.args[1])


# Creating Custom Exception Classes:

class NewValueError(ValueError):
    def __init__(self, name,code,state):
        self.data = (name,code,state) # Tuple is created.

try:

    raise NewValueError("Division by 0", 000, "Not Divisible")

except NewValueError as e:
    print(e.args) # This is not very helpful.
    print(f"Type of error is: {e.args[0]}")
    print(f"Code of error is: {e.args[1]}")
    print(f"State of error is: {e.args[2]}")
