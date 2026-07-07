# 🚀 Problem: Interplanetary Cargo Delivery Scheduler

## 📘 Story

The year is 2085.

A space logistics company called **Galactic Express** delivers cargo between Earth and various space stations.

Every cargo shipment has:

- Shipment ID
- Departure Date
- Estimated Delivery Date

Mission controllers want a system that can:

1. Record shipment information.
2. Calculate how many days remain until delivery.
3. Display the shipment schedule in a readable format.
4. Determine whether the shipment is:
   - Delivered
   - In Transit
   - Departing Today

---

## 🎯 Your Task

Create a program that:

### Step 1

Ask the user for:

```text
Shipment ID
Departure Date (YYYY-MM-DD)
Estimated Delivery Date (YYYY-MM-DD)
```

---

### Step 2

Display the shipment information using the format:

```text
Shipment ID : GX-101
Departure   : 08 Jul 2085
Delivery    : 20 Jul 2085
```

---

### Step 3

Calculate:

```text
Days Until Delivery
```

using today's date.

---

### Step 4

Display one of the following messages:

#### If delivery date is in the future

```text
Status: In Transit
```

#### If delivery date is today

```text
Status: Arriving Today
```

#### If delivery date has passed

```text
Status: Delivered
```

---

## ⚙️ Requirements

You must use:

- `date`
- `datetime`
- `timedelta`
- `strftime()`

---

## 🧪 Sample Input

```text
GX-101
2085-07-08
2085-07-20
```

---

## 🧪 Sample Output

```text
Shipment ID : GX-101
Departure   : 08 Jul 2085
Delivery    : 20 Jul 2085

Days Until Delivery : 12

Status: In Transit
```