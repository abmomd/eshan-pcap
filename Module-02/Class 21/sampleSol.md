# 🚀 Solution: Space Tourism Launch Calendar

```python
import calendar

mission = input("Enter Mission Name: ")

year = int(input("Enter Launch Year: "))
month = int(input("Enter Launch Month: "))
day = int(input("Enter Launch Day: "))

print("\nMission:", mission)

print("\nLaunch Calendar")
print("-" * 30)

print(calendar.month(year, month))

weekday_num = calendar.weekday(year, month, day)

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

print("Launch Day:", days[weekday_num])

if weekday_num >= 5:
    print("Weekend Launch")
else:
    print("Weekday Launch")

if calendar.isleap(year):
    print("Leap Year: Yes")
else:
    print("Leap Year: No")

print("\nWeek Header:")
print(calendar.weekheader(2))
```

---

## Sample Run

```text
Enter Mission Name: Moon Explorer

Enter Launch Year: 2045
Enter Launch Month: 7
Enter Launch Day: 18

Mission: Moon Explorer

Launch Calendar

     July 2045
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

Launch Day: Wednesday

Weekday Launch

Leap Year: No

Week Header:
Mo Tu We Th Fr Sa Su
```

---

## Concepts Used

### Display Month Calendar

```python
calendar.month(year, month)
```

Displays a month's calendar.

---

### Find Weekday

```python
calendar.weekday(year, month, day)
```

Returns:

```text
0 = Monday
...
6 = Sunday
```

---

### Leap Year Check

```python
calendar.isleap(year)
```

Returns:

```python
True
```

or

```python
False
```

---

### Week Header

```python
calendar.weekheader(2)
```

Returns:

```text
Mo Tu We Th Fr Sa Su
```

---

## Skills Practiced

✅ calendar.month()

✅ calendar.weekday()

✅ calendar.isleap()

✅ calendar.weekheader()

✅ Conditional Logic

✅ Lists

✅ Real-world Scheduling Applications
```
