# Weeker Class – Days of the Week Manipulation

Your task is to implement a class called `Weeker`. Yes, your eyes don't deceive you – this name comes from the fact that objects of that class will be able to store and manipulate the days of the week.

---

## Constructor

The class constructor accepts **one argument – a string**.

The string represents the name of the day of the week and the only acceptable values must come from the following set:

```
Mon Tue Wed Thu Fri Sat Sun
```

Invoking the constructor with an argument from outside this set should raise the `WeekDayError` exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon).

---

## Required Facilities

The class should provide the following:

- Objects of the class should be **"printable"**, i.e., they should be able to implicitly convert themselves into strings of the same form as the constructor arguments.
- The class should be equipped with **one-parameter methods** called:
  - `add_days(n)`
  - `subtract_days(n)`

Where `n` is an integer number, and the method updates the day of the week stored inside the object to reflect the change of date by the indicated number of days (forward or backward).

---

## Additional Requirements

- All object's properties should be **private**.

---

## Final Step

Complete the template provided in the editor.  
Run your code and check whether your output looks the same as expected.

---

## Expected Output

```text
Mon
Tue
Sun
Sorry, I can't serve your request.
```
