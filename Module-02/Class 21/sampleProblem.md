# 🚀 Space Tourism Launch Calendar

## 📘 Story

The year is 2045.

A company called **StarVoyage** offers commercial space tourism flights.

Customers can book trips to:

- The Moon
- Mars Orbit
- International Space Station

Mission planners need a scheduling system that can analyze launch dates and provide useful information.

---

## 🎯 Your Task

Create a program that helps mission planners analyze a launch date.

---

## Step 1: Input

Ask the user for:

```text
Mission Name
Launch Year
Launch Month
Launch Day
```

Example:

```text
Moon Explorer
2045
7
18
```

---

## Step 2: Display Launch Calendar

Display the calendar of the launch month.

Example:

```text
July 2045
Mo Tu We Th Fr Sa Su
...
```

---

## Step 3: Determine Launch Day

Determine the exact weekday of the launch date.

Example:

```text
Launch Day: Friday
```

---

## Step 4: Weekend Check

If launch date falls on:

```text
Saturday or Sunday
```

display:

```text
Weekend Launch
```

Otherwise display:

```text
Weekday Launch
```

---

## Step 5: Leap Year Check

Determine whether the launch year is a leap year.

Example:

```text
Leap Year: Yes
```

or

```text
Leap Year: No
```

---

## Step 6: Display Week Header

Display the week header using:

```python
calendar.weekheader()
```

Example:

```text
Mo Tu We Th Fr Sa Su
```

---

## ⚙️ Requirements

You must use:

- calendar.month()
- calendar.weekday()
- calendar.isleap()
- calendar.weekheader()

---

## Sample Input

```text
Moon Explorer
2045
7
18
```

---

## Sample Output

```text
Mission: Moon Explorer

July 2045 Calendar

<calendar here>

Launch Day: Wednesday

Weekday Launch

Leap Year: No

Week Header:
Mo Tu We Th Fr Sa Su
```