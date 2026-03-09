# Point Class – Cartesian Coordinate System

Let's visit a very special place – a plane with the Cartesian coordinate system
(you can learn more about this concept here:
https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

Each point located on the plane can be described as a pair of coordinates customarily called `x` and `y`.

We expect that you are able to write a Python class which:

- Stores both coordinates as **float numbers**
- Evaluates the distances between any two points situated on the plane

---

## Hint

Use the function `hypot()` from the `math` module.

It evaluates the length of the hypotenuse of a right triangle:

- https://en.wikipedia.org/wiki/Hypotenuse
- https://docs.python.org/3.7/library/math.html#trigonometric-functions

---

## Class Requirements

The class should meet the following specifications:

- It is called `Point`
- Its constructor accepts two arguments (`x` and `y` respectively), both default to zero
- All properties should be **private**
- The class contains two parameterless methods:
  - `getx()` – returns the x coordinate
  - `gety()` – returns the y coordinate
- The class provides a method:
  - `distance_from_xy(x, y)` – calculates and returns the distance between the stored point and another point given as two floats
- The class provides another method:
  - `distance_from_point(point)` – calculates the distance between the stored point and another `Point` object

---

## Template

```python
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        #
        # Write code here
        #

    def getx(self):
        #
        # Write code here
        #

    def gety(self):
        #
        # Write code here
        #

    def distance_from_xy(self, x, y):
        #
        # Write code here
        #

    def distance_from_point(self, point):
        #
        # Write code here
        #


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
```

---


