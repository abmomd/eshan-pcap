# Triangle Class – Embedding the Point Class

Now we're going to embed the `Point` class (see previous lab) inside another class.  
Also, we're going to put three points into one class, which will let us define a triangle.

---

## Objective

Create a new class called `Triangle`.

---

## Requirements

The `Triangle` class should meet the following expectations:

- The constructor accepts **three arguments** – all of them are objects of the `Point` class.
- The points are stored inside the object as a **private list**.
- The class provides a parameterless method called:
  - `perimeter()`

The `perimeter()` method should calculate the perimeter of the triangle described by the three points.

> The perimeter is the sum of the lengths of all three sides.

---

## Note

You can copy the `Point` class code from the previous lab (the Cartesian coordinate system exercise).

---



## Expected Output

```text
3.414213562373095
```

Complete the template in the editor.  
Run your code and verify that the evaluated perimeter matches the expected output.

## Template

```python
import math


class Point:
    #
    # The code copied from the previous lab.
    #


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        #
        # Write code here
        #

    def perimeter(self):
        #
        # Write code here
        #


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
```
---
