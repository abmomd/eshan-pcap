# ✈️ Smart Airline Reservation System – Advanced Exception Handling Challenge

You are hired to build a **Smart Airline Reservation System**.  
The system must handle seat bookings safely and professionally using advanced exception handling.

The airline wants robust validation and meaningful error reporting.

You must design the system using:

- Custom exception classes
- Inheriting from built-in exceptions
- Exception objects (`as e`)
- Accessing `.args`
- Multiple `except` blocks
- `else`
- `finally`
- Optional exception chaining

---

# 🎯 System Requirements

---

## 🔹 1️⃣ Create Custom Exceptions

Create the following exception classes:

### 1. `InvalidSeatNumberError`
- Inherit from `ValueError`
- Raised when seat number is outside valid range

### 2. `SeatAlreadyBookedError`
- Inherit from `Exception`
- Must store:
  - seat number
  - passenger name who already booked it
- Pass a meaningful message to the base class

### 3. `InvalidPassengerNameError`
- Inherit from `ValueError`
- Raised when passenger name is empty or invalid

---

## 🔹 2️⃣ Create Class: `Flight`

The class must contain:

- Instance variables:
  - `flight_number`
  - `total_seats`
  - `booked_seats` (dictionary mapping seat_number → passenger_name)

---

### Required Method:

```
book_seat(seat_number, passenger_name)
```

The method must:

- Raise `InvalidPassengerNameError` if name is empty
- Raise `InvalidSeatNumberError` if seat number is not within range
- Raise `SeatAlreadyBookedError` if seat is already booked
- Otherwise:
  - Add booking to dictionary
  - Return a confirmation message

---

## 🔹 3️⃣ Create Function: `process_booking(flight, seat_number, passenger_name)`

This function must:

- Print a message indicating booking attempt
- Use a `try` block to call `flight.book_seat()`

Include exception handling:

- Catch `InvalidPassengerNameError`
- Catch `InvalidSeatNumberError`
- Catch `SeatAlreadyBookedError`
  - Print all arguments using `.args`
  - Print stored seat number from the exception object
- Catch any unexpected exception

Use:

- `else` → print booking success message
- `finally` → print:
  ```
  Booking session ended.
  ```

---

## 🔹 4️⃣ Testing Scenario

Create:

```
flight = Flight("AI-202", 5)
```

Then test:

```
process_booking(flight, 2, "Alice")
process_booking(flight, 2, "Bob")
process_booking(flight, 7, "Charlie")
process_booking(flight, 3, "")
```

---


