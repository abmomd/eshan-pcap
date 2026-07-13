# Calendar Module.
# --> Display Calendar
# --> Working with weekdays
# --> Checking leap years
# . --> Date-related operations

import calendar

# Weekdays Numbering System in Python

# Monday -> 0
# Tuesday -> 1
# Wed -> 2
# Thurs -> 3
# Fri -> 4
# Sat -> 5
# Sun -> 6

print(calendar.weekday(2026,7,12))

# print(calendar.calendar(2026))
#
# # Another format to print calendar
#
# calendar.prcal(2025)

# Printing Monthly Calendar

# print(calendar.month(2026,7))
# calendar.prmonth(2026,7)

# Allows to change the first day of the week.
print(calendar.month(2026,7))
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2026,7))
print(calendar.weekday(2026,7,12))

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

day = calendar.weekday(2026,7,12)
print(days[day])

# From 3-8 --> Sun,Mon..
# From 9 - Max --> Prints full headers.
print(calendar.weekheader(9))

# Leap Year Checking --> isleap

print(calendar.isleap(2026))

# iterate in days function:

c = calendar.Calendar(3)

for day in c.iterweekdays():
    print(days[day],end=" ")


