# Homework – Queue Using Class (OOP + DSA Focus)

## 1. Core Queue Implementation
Write a Python class `Queue` using a list as the underlying data structure.
The class must support the following methods:

- `put(val)`: insert `val` at the rear of the queue
- `get()`: remove and return the front element of the queue
- `peek()`: return the front element without removing it
- `is_empty()`: return True if the queue is empty, otherwise False
- `size()`: return the number of elements in the queue

Ensure that the queue follows the FIFO (First In First Out) principle.

## 2. Handling Underflow (Edge Case)
Extend the `Queue` class such that:

- `get()` prints "Queue is empty" and returns None if the queue has no elements
- `peek()` returns None if the queue is empty

Demonstrate the behavior by calling get() and peek() on an empty queue.

## 3. Real-Life Queue Simulation
Use the `Queue` class to simulate a queue at a hospital registration desk.

- Patients enter the queue using `put(name)`
- Patients are served using `get()`
- Print the order in which patients are served

`Example:`

put("Amit"), put("Sara"), put("John")
Serving order should be: Amit → Sara → John

## 4. Queue vs Stack (Conceptual + Code)
Write a short Python program with comments that:

- Uses a Queue class to show FIFO behavior
- Explains (using comments) one difference between a stack and a queue


## 5. Practice Problem – Queue Reversal
Given a queue implemented using the `Queue` class, write a program to reverse the queue.

Rules:
- You may use only one extra stack
- Use `put(value)` and `get()` methods for queue operations
- After reversal, the front of the queue should become the rear

Example:
Original Queue: 10 20 30
Reversed Queue: 30 20 10
