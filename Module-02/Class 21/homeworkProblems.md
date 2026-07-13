# 🏠 Homework 1: International Conference Planner

## 📘 Story

A global technology company organizes conferences around the world.

The event manager wants a program that can analyze any conference date and generate useful scheduling information.

---

## 🎯 Your Task

Ask the user for:

- Conference Name
- Year
- Month
- Day

---

## The Program Should

1. Display the calendar of that month.
2. Determine the day of the week.
3. Determine whether the event occurs on a weekend.
4. Determine whether the year is a leap year.
5. Display all weekdays using `weekheader()`.

---

## Concepts

- calendar.month()
- calendar.weekday()
- calendar.isleap()
- calendar.weekheader()


# 🏠 Homework 2: School Exam Scheduler

## 📘 Story

A school is planning final examinations.

Students want to know:

- What day the exam falls on.
- Whether the exam is on a weekend.
- How many Mondays exist in that month.

---

## 🎯 Your Task

Ask the user for:

- Subject Name
- Exam Year
- Exam Month
- Exam Day

---

## The Program Should

1. Display the exam month's calendar.
2. Display the exam day.
3. Determine whether the exam falls on a weekend.
4. Count the number of Mondays in the month.

---

## Concepts

- Calendar class
- weekday()
- monthcalendar()


# 🏠 Homework 3: Mars Colony Work Shift Generator

## 📘 Story

A Mars colony begins its work week on Wednesday instead of Monday.

Engineers need a custom calendar.

---

## 🎯 Your Task

Create a calendar object whose first weekday is Wednesday.

Display:

1. The weekday numbers returned by `iterweekdays()`.
2. The month's calendar.
3. The order of weekdays.

---

## Example Output

```text
Weekday Order:
Wed Thu Fri Sat Sun Mon Tue
```

---

## Concepts

- Calendar()
- iterweekdays()
- firstweekday


# 🏠 Homework 4: Olympic Games Date Analyzer

## 📘 Story

The Olympic Committee is selecting dates for future events.

Some events should preferably be held on weekends to maximize attendance.

---

## 🎯 Your Task

Ask the user for:

- Event Name
- Event Date

---

## The Program Should

Display:

1. Event weekday.
2. Whether it is a weekend.
3. The full calendar for that month.
4. Whether the year is a leap year.
5. The weekday number.

---

## Concepts

- weekday()
- month()
- isleap()

# 🏠 Homework 5: Hotel Booking Calendar

## 📘 Story

A hotel manager wants to analyze booking dates.

Customers frequently ask:

- What day they are checking in.
- Whether their stay begins on a weekend.
- Whether the month contains five weekends.

---

## 🎯 Your Task

Ask the user for:

- Customer Name
- Check-in Date

---

## The Program Should

1. Display the month's calendar.
2. Display the weekday of check-in.
3. Count Saturdays and Sundays in the month.
4. Display whether the month has at least five weekends.

---

## Concepts

- monthcalendar()
- weekday()
- Calendar class


# 🏠 Homework 6: Space Launch Window Analyzer

## 📘 Story

A private space company is planning rocket launches.

Launches are preferred on:

```text
Tuesday
Wednesday
Thursday
```

due to lower air traffic and better scheduling.

---

## 🎯 Your Task

Ask the user for:

- Mission Name
- Launch Date

---

## The Program Should

1. Display the launch month's calendar.
2. Determine the weekday.
3. Display:

### If Tuesday/Wednesday/Thursday

```text
Preferred Launch Window
```

### Otherwise

```text
Non-Preferred Launch Window
```

4. Display the week header.
5. Display whether the launch year is a leap year.

---

## Concepts

- weekday()
- weekheader()
- month()
- isleap()

