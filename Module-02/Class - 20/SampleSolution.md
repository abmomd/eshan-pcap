# 🚀 Solution: Interplanetary Cargo Delivery Scheduler

```python
from datetime import datetime, date

shipment_id = input("Enter Shipment ID: ")

departure_str = input(
    "Enter Departure Date (YYYY-MM-DD): "
)

delivery_str = input(
    "Enter Delivery Date (YYYY-MM-DD): "
)

departure_date = datetime.strptime(
    departure_str,
    "%Y-%m-%d"
).date()

delivery_date = datetime.strptime(
    delivery_str,
    "%Y-%m-%d"
).date()

today = date.today()

print("\nShipment Information")
print("-" * 30)

print(
    "Shipment ID :",
    shipment_id
)

print(
    "Departure   :",
    departure_date.strftime("%d %b %Y")
)

print(
    "Delivery    :",
    delivery_date.strftime("%d %b %Y")
)

days_remaining = (delivery_date - today).days

print()
print(
    "Days Until Delivery :",
    abs(days_remaining)
)

if delivery_date > today:
    print("Status: In Transit")

elif delivery_date == today:
    print("Status: Arriving Today")

else:
    print("Status: Delivered")
```

---

## Sample Run

```text
Enter Shipment ID: GX-101

Enter Departure Date (YYYY-MM-DD): 2085-07-08

Enter Delivery Date (YYYY-MM-DD): 2085-07-20


Shipment Information
------------------------------

Shipment ID : GX-101
Departure   : 08 Jul 2085
Delivery    : 20 Jul 2085

Days Until Delivery : 12

Status: In Transit
```

---

## Concepts Used

### date.today()

```python
today = date.today()
```

Gets the current date.

---

### datetime.strptime()

```python
datetime.strptime(
    delivery_str,
    "%Y-%m-%d"
)
```

Converts a string into a date.

---

### strftime()

```python
departure_date.strftime("%d %b %Y")
```

Formats:

```text
2085-07-08
```

as:

```text
08 Jul 2085
```

---

### timedelta

```python
delivery_date - today
```

returns:

```text
12 days, 0:00:00
```

and we use:

```python
.days
```

to get the number of days.

---

## Skills Practiced

✅ date

✅ datetime

✅ timedelta

✅ strftime()

✅ Date Arithmetic

✅ User Input

✅ Real-world Scheduling System
```