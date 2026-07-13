# 🏥 Problem 1: Hospital Appointment Management System

## 📘 Story

A hospital manages thousands of patient appointments every month.

Doctors want a system that can determine how many days remain until a patient's appointment and whether the appointment is overdue.

---

## 🎯 Your Task

Ask the user for:

- Patient Name
- Appointment Date (YYYY-MM-DD)

---

## The Program Should

1. Display today's date.
2. Display the appointment date in a readable format.
3. Calculate the number of days remaining.
4. Display one of the following:

### Future Appointment

```text
Status: Upcoming Appointment
```

### Appointment Today

```text
Status: Appointment Today
```

### Past Appointment

```text
Status: Missed Appointment
```

---

## Sample Input

```text
John Smith
2026-08-15
```

---

## Sample Output

```text
Patient: John Smith
Appointment: 15 Aug 2026

Days Remaining: 38

Status: Upcoming Appointment
```

# ✈️ Problem 2: Flight Countdown Tracker

## 📘 Story

An airline wants passengers to know exactly how long remains before their flight departs.

---

## 🎯 Your Task

Ask the user for:

- Flight Number
- Departure Date & Time

Format:

```text
YYYY-MM-DD HH:MM
```

---

## The Program Should

Calculate:

- Days remaining
- Hours remaining
- Minutes remaining

---

## Display

```text
Flight: AI302

Departure:
20 Jul 2026 14:30

Time Remaining:
12 days
5 hours
18 minutes
```

---

## Concepts

- datetime
- timedelta
- strftime
# 🎓 Problem 3: University Exam Countdown

## 📘 Story

A university wants students to know how much preparation time remains before exams.

---

## 🎯 Your Task

Ask the user for:

- Subject Name
- Exam Date

---

## The Program Should

Calculate:

```text
Days Until Exam
```

Then display:

### More than 30 days

```text
Preparation Status: Plenty of Time
```

### Between 10 and 30 days

```text
Preparation Status: Start Revision
```

### Less than 10 days

```text
Preparation Status: Intensive Revision Needed
```

---

## Sample Output

```text
Subject: Physics

Exam Date:
12 Sep 2026

Days Remaining:
8

Preparation Status:
Intensive Revision Needed
```

# 🚚 Problem 4: E-Commerce Delivery Tracker

## 📘 Story

A customer has ordered a product online.

The logistics company wants to provide delivery updates.

---

## 🎯 Your Task

Ask the user for:

- Order ID
- Order Date
- Estimated Delivery Date

---

## The Program Should

Display:

```text
Order ID
Order Date
Delivery Date
Transit Time
```

---

## Example

```text
Order ID: ORD1024

Order Date:
01 Jul 2026

Delivery Date:
08 Jul 2026

Transit Time:
7 Days
```

---

## Bonus

Display:

```text
Delivered
```

or

```text
In Transit
```

based on today's date.


# 🎮 Problem 5: Gaming Tournament Scheduler

## 📘 Story

An international gaming tournament is approaching.

Players want a countdown timer showing how long remains until the event starts.

---

## 🎯 Your Task

Ask the user for:

- Tournament Name
- Tournament Date & Time

---

## The Program Should

Display:

```text
Tournament:
World Championship

Starts On:
20 Dec 2026 18:00
```

---

## Calculate

```text
Days Remaining
Hours Remaining
Minutes Remaining
```

---

## Bonus

If less than 7 days remain:

```text
Tournament Week Has Started!
```


# 🚀 Problem 6: Mars Colony Supply Mission Planner

## 📘 Story

A cargo spacecraft transports food and supplies from Earth to a Mars colony.

Mission control needs a planner to monitor mission duration.

---

## 🎯 Your Task

Ask the user for:

- Mission Name
- Launch Date
- Expected Arrival Date

---

## The Program Should

Calculate:

### Mission Duration

```text
Launch → Arrival
```

in days.

---

### Mission Progress

Based on today's date:

```text
Not Started
```

or

```text
In Progress
```

or

```text
Mission Completed
```

---

## Sample Output

```text
Mission: RedSupply-12

Launch Date:
01 Jan 2027

Arrival Date:
15 Feb 2027

Mission Duration:
45 Days

Status:
In Progress
```

---

## Concepts

- date
- datetime
- timedelta
- strftime
- date comparison