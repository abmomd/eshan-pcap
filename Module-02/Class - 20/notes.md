# 🕒 Python `datetime` and `time` Modules – Complete Notes

## 🎯 Learning Objectives

By the end of this module, you should be able to:

* Create and manipulate dates and times.
* Get the current date and time.
* Work with Unix timestamps.
* Pause program execution.
* Format dates and times using `strftime()`.
* Perform calculations using dates and times.
* Use `timedelta` objects for date arithmetic.

---

# 🧠 1. Why Do We Need Date and Time Modules?

Almost every real-world application works with time:

* Banking transactions
* Flight bookings
* Attendance systems
* Social media posts
* Delivery tracking
* Event scheduling

Python provides two important modules:

```python
import datetime
import time
```

---

# 📅 2. The `date` Class

A `date` object stores:

* Year
* Month
* Day

---

## Creating a Date

```python
from datetime import date

d = date(2025, 7, 8)

print(d)
```

### Output

```text
2025-07-08
```

---

## Accessing Attributes

```python
from datetime import date

d = date(2025, 7, 8)

print("Year:", d.year)
print("Month:", d.month)
print("Day:", d.day)
```

### Output

```text
Year: 2025
Month: 7
Day: 8
```

---

## Important

These attributes are:

```text
Read Only
```

You cannot do:

```python
d.year = 2030
```

---

# 🌍 Real-Life Example

A university stores:

```text
Admission Date
Exam Date
Graduation Date
```

using date objects.

---

# 📅 3. Getting Today's Date

Use:

```python
date.today()
```

---

## Example

```python
from datetime import date

today = date.today()

print(today)
```

### Output

```text
2025-07-08
```

(Current date)

---

# 🌍 Real-Life Example

An attendance system automatically records:

```python
attendance_date = date.today()
```

---

# ⏳ 4. Unix Timestamp

A timestamp represents:

```text
Number of seconds since
January 1, 1970
00:00:00 UTC
```

This date is called:

```text
Unix Epoch
```

---

## Current Timestamp

```python
import time

print(time.time())
```

### Example Output

```text
1751940000.234
```

---

## Convert Timestamp to Date

```python
from datetime import date
import time

timestamp = time.time()

d = date.fromtimestamp(timestamp)

print(d)
```

---

# 🌍 Real-Life Example

Instagram stores:

```text
Post Created Time
```

as timestamps.

---

# ⌚ 5. The `time` Class

Used when only time is required.

Stores:

* Hour
* Minute
* Second

---

## Creating a Time Object

```python
from datetime import time

t = time(13, 22, 20)

print(t)
```

### Output

```text
13:22:20
```

---

## Accessing Attributes

```python
print(t.hour)
print(t.minute)
print(t.second)
```

---

### Output

```text
13
22
20
```

---

# 🌍 Real-Life Example

A movie booking system stores:

```text
Show Time
```

without needing a date.

---

# 😴 6. The `sleep()` Function

Used to pause program execution.

---

## Syntax

```python
time.sleep(seconds)
```

---

## Example

```python
import time

print("Starting...")

time.sleep(5)

print("Finished")
```

---

### Output

```text
Starting...

(wait 5 seconds)

Finished
```

---

# 🌍 Real-Life Example

Traffic light simulation:

```python
Green → wait
Yellow → wait
Red → wait
```

---

# 🚦 Countdown Example

```python
import time

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("Launch!")
```

---

# 📆 7. The `datetime` Class

Combines:

```text
Date + Time
```

into a single object.

---

## Creating a Datetime

```python
from datetime import datetime

dt = datetime(
    2025,
    7,
    8,
    15,
    30,
    45
)

print(dt)
```

---

### Output

```text
2025-07-08 15:30:45
```

---

## Access Attributes

```python
print(dt.year)
print(dt.month)
print(dt.day)

print(dt.hour)
print(dt.minute)
print(dt.second)
```

---

# 🌍 Real-Life Example

Online shopping:

```text
Order Placed:
2025-07-08 15:30:45
```

---

# 📋 8. Formatting Dates with `strftime()`

By default:

```python
2025-07-08
```

Sometimes we want:

```python
08/07/2025
```

or

```python
July 08, 2025
```

---

## Syntax

```python
object.strftime(format)
```

---

## Example

```python
from datetime import date

d = date(2025, 7, 8)

print(d.strftime("%Y/%m/%d"))
```

### Output

```text
2025/07/08
```

---

# Important Directives

| Directive | Meaning | Example |
| --------- | ------- | ------- |
| %Y        | Year    | 2025    |
| %m        | Month   | 07      |
| %d        | Day     | 08      |
| %H        | Hour    | 15      |
| %M        | Minute  | 30      |
| %S        | Second  | 45      |

---

## Example

```python
from datetime import datetime

now = datetime.now()

print(now.strftime("%d-%m-%Y"))
```

Output:

```text
08-07-2025
```

---

## Example

```python
print(now.strftime("%H:%M:%S"))
```

Output:

```text
15:30:45
```

---

# 🧪 Exercise 1

## Code

```python
from datetime import time

t = time(14, 53)

print(
    t.strftime("%H:%M:%S")
)
```

---

### Output

```text
14:53:00
```

Why?

Because:

```python
second = 0
```

by default.

---

# ➖ 9. Date Arithmetic

Dates can be subtracted.

---

## Example

```python
from datetime import date

d1 = date(2025, 7, 8)
d2 = date(2025, 7, 1)

difference = d1 - d2

print(difference)
```

---

### Output

```text
7 days, 0:00:00
```

---

# Result Type

The result is:

```python
timedelta
```

object.

---

# 📦 10. The `timedelta` Object

Represents:

```text
Difference Between Dates
```

---

## Example

```python
from datetime import date

d1 = date(2025, 12, 31)
d2 = date(2025, 1, 1)

delta = d1 - d2

print(delta.days)
```

---

### Output

```text
364
```

---

## Multiplication

```python
print(delta * 2)
```

Output:

```text
728 days, 0:00:00
```

---

# 🧪 Exercise 2

## Code

```python
from datetime import datetime

dt1 = datetime(
    2020, 9, 29,
    14, 41, 0
)

dt2 = datetime(
    2020, 9, 28,
    14, 41, 0
)

print(dt1 - dt2)
```

---

### Output

```text
1 day, 0:00:00
```

---

# 🌍 Real-Life Examples

---

## 🏦 Banking System

```python
transaction_time = datetime.now()
```

Store transaction timestamps.

---

## ✈️ Flight Booking System

```python
departure_date
arrival_date
```

Calculate journey duration.

---

## 🎓 Attendance System

```python
date.today()
```

Store attendance date.

---

## 🚚 Delivery Tracking

```python
expected_date - order_date
```

Calculate delivery time.

---

## 🎮 Game Cooldown Timer

```python
time.sleep(10)
```

Wait before next action.

---

# ⚠️ Common Mistakes

---

## Forgetting Imports

❌

```python
today = date.today()
```

Without importing `date`.

---

## Invalid Date

❌

```python
date(2025, 13, 1)
```

Month 13 doesn't exist.

---

## Negative Sleep

❌

```python
time.sleep(-5)
```

Raises:

```python
ValueError
```

---

# 🚀 Best Practices

✅ Use `datetime` when both date and time are needed.

✅ Use `date` when only the calendar date matters.

✅ Store timestamps for databases and logs.

✅ Format output with `strftime()`.

✅ Use `timedelta` for calculations.

---

# 🎯 Summary

| Class/Function         | Purpose            |
| ---------------------- | ------------------ |
| `date()`               | Create date        |
| `date.today()`         | Current date       |
| `time()`               | Create time        |
| `datetime()`           | Create date + time |
| `time.time()`          | Current timestamp  |
| `date.fromtimestamp()` | Timestamp → Date   |
| `strftime()`           | Format date/time   |
| `sleep()`              | Pause execution    |
| `timedelta`            | Date difference    |

---

# 🧠 Final Thought

Date and time handling is everywhere:

* Banking
* Healthcare
* Airlines
* E-Commerce
* Social Media
* Gaming
* Data Analytics

Mastering `datetime` and `time` is essential for building real-world Python applications.
