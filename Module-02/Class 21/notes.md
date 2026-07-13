# 📅 Python `calendar` Module – Complete Notes

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- Display yearly and monthly calendars.
- Determine the day of the week for any date.
- Change the first day of the week.
- Check whether a year is a leap year.
- Generate weekday headers.
- Use the `Calendar` class and its iterators.

---

# 🧠 1. What is the Calendar Module?

The `calendar` module provides useful functions and classes for:

- Displaying calendars
- Working with weekdays
- Checking leap years
- Generating date-related information

---

## Importing the Module

```python
import calendar
```

---

# 📅 2. Weekday Numbering System

Python represents weekdays as integers.

| Day | Value |
|------|--------|
| Monday | 0 |
| Tuesday | 1 |
| Wednesday | 2 |
| Thursday | 3 |
| Friday | 4 |
| Saturday | 5 |
| Sunday | 6 |

---

## Example

```python
import calendar

print(calendar.weekday(2025, 7, 8))
```

Output:

```text
1
```

Meaning:

```text
Tuesday
```

---

# 🌍 Real-Life Example

A hospital booking system wants to know:

```text
Is 15-Aug-2025 a weekday or weekend?
```

The `weekday()` function can answer this.

---

# 📆 3. Displaying a Full Year Calendar

Use:

```python
calendar.calendar(year)
```

---

## Example

```python
import calendar

print(calendar.calendar(2025))
```

---

### Alternative

```python
calendar.prcal(2025)
```

No need for `print()`.

---

# 🌍 Real-Life Example

A school wants to print the academic calendar for an entire year.

---

# 📅 4. Displaying a Monthly Calendar

Use:

```python
calendar.month(year, month)
```

---

## Example

```python
import calendar

print(calendar.month(2025, 7))
```

Output:

```text
     July 2025
Mo Tu We Th Fr Sa Su
      1  2  3  4  5
 6  7  8  9 10 11 12
...
```

---

### Alternative

```python
calendar.prmonth(2025, 7)
```

---

# 🌍 Real-Life Example

A company displays the calendar for the current month on its employee dashboard.

---

# 🔄 5. Changing the First Day of the Week

By default:

```text
Monday
```

is the first day.

Use:

```python
calendar.setfirstweekday()
```

---

## Example

```python
import calendar

calendar.setfirstweekday(calendar.SUNDAY)

print(calendar.month(2025, 7))
```

---

## Common Values

| Value | First Day |
|---------|------------|
| 0 | Monday |
| 6 | Sunday |

---

# 🌍 Real-Life Example

Different countries start calendars differently.

For example:

- USA → Sunday
- UK → Monday

---

# 📌 6. Finding the Weekday of a Date

Use:

```python
calendar.weekday(year, month, day)
```

---

## Example

```python
import calendar

day = calendar.weekday(2025, 7, 8)

print(day)
```

Output:

```text
1
```

Tuesday.

---

## Convert to Name

```python
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

print(days[day])
```

Output:

```text
Tuesday
```

---

# 🌍 Real-Life Example

An airline system checks whether a flight departs on a weekend.

---

# 🏷️ 7. Week Headers

Use:

```python
calendar.weekheader(width)
```

---

## Example

```python
import calendar

print(calendar.weekheader(2))
```

Output:

```text
Mo Tu We Th Fr Sa Su
```

---

## Example

```python
print(calendar.weekheader(3))
```

Output:

```text
Mon Tue Wed Thu Fri Sat Sun
```

---

## Important

Even if width > 3:

```python
print(calendar.weekheader(10))
```

You still get abbreviated names.

---

# 🌍 Real-Life Example

A scheduling application uses weekday headers in a table.

---

# 🌱 8. Leap Year Checking

Use:

```python
calendar.isleap(year)
```

---

## Example

```python
import calendar

print(calendar.isleap(2024))
```

Output:

```text
True
```

---

## Example

```python
print(calendar.isleap(2025))
```

Output:

```text
False
```

---

# 🌍 Real-Life Example

A payroll system needs to know whether February has:

```text
28 days
or
29 days
```

---

# 📆 9. The Calendar Class

You can create your own calendar object.

---

## Example

```python
import calendar

c = calendar.Calendar()
```

---

## Custom First Day

```python
c = calendar.Calendar(firstweekday=2)
```

Meaning:

```text
Wednesday
```

becomes the first day.

---

# 🔄 iterweekdays()

Returns weekday numbers.

---

## Example

```python
import calendar

c = calendar.Calendar(2)

for day in c.iterweekdays():
    print(day, end=" ")
```

Output:

```text
2 3 4 5 6 0 1
```

---

## Meaning

```text
Wed Thu Fri Sat Sun Mon Tue
```

---

# 🌍 Real-Life Example

A shift scheduling system starts its work week on Wednesday.

---

# 📊 Useful Calendar Functions

| Function | Purpose |
|-----------|-----------|
| calendar() | Full year calendar |
| month() | Monthly calendar |
| prcal() | Print yearly calendar |
| prmonth() | Print monthly calendar |
| weekday() | Day number |
| weekheader() | Weekday headers |
| isleap() | Leap year check |
| setfirstweekday() | Change first day |
| Calendar() | Create calendar object |
| iterweekdays() | Iterate weekdays |

---

# 🧪 Exercise 1

## Code

```python
import calendar

print(calendar.weekday(2020, 9, 29))
```

Output:

```text
1
```

Meaning:

```text
Tuesday
```

---

# 🧪 Exercise 2

## Code

```python
import calendar

print(calendar.weekheader(2))
```

Output:

```text
Mo Tu We Th Fr Sa Su
```

---

# 🧪 Exercise 3

## Code

```python
import calendar

print(calendar.isleap(2020))
```

Output:

```text
True
```

---

# 🌍 Real-Life Applications

## 🏫 School Timetable System

Determine weekdays for exams.

---

## ✈️ Flight Booking System

Check weekend and weekday flights.

---

## 🏢 HR Attendance System

Generate monthly attendance calendars.

---

## 🏦 Payroll System

Handle leap years correctly.

---

## 🚀 Space Mission Scheduling

Determine launch windows and mission timelines.

---

# ⚠️ Common Mistakes

## Wrong Weekday Number Assumption

❌

```python
0 = Sunday
```

In Python:

```python
0 = Monday
```

---

## Forgetting to Import

❌

```python
print(month(2025, 7))
```

Must use:

```python
import calendar
```

---

## Invalid Month

❌

```python
calendar.month(2025, 13)
```

Raises:

```text
IllegalMonthError
```

---

# 🚀 Best Practices

✅ Use `weekday()` when only the day name is needed.

✅ Use `month()` for displaying monthly calendars.

✅ Use `isleap()` before February calculations.

✅ Use `Calendar()` for customized calendars.

---

# 🎯 Summary

| Concept | Function |
|----------|-----------|
| Year Calendar | `calendar()` |
| Month Calendar | `month()` |
| Print Year | `prcal()` |
| Print Month | `prmonth()` |
| Day Number | `weekday()` |
| Week Header | `weekheader()` |
| Leap Year | `isleap()` |
| First Weekday | `setfirstweekday()` |
| Calendar Object | `Calendar()` |
| Weekday Iterator | `iterweekdays()` |

---

# 🧠 Final Thought

The `calendar` module is extremely useful when building:

- Scheduling Systems
- Attendance Trackers
- Booking Platforms
- Payroll Applications
- Event Management Software
- Academic Timetable Systems

It provides a powerful yet simple way to work with calendars and weekdays in Python.
```**