"""
Lesson 5, Task 3, homework 4.
2 circles intersection.
"""
import math


def circles_intersect(x0, y0, r0, x1, y1, r1):
    d = math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    if d > r1 + r0 or d < abs(r0 - r1):
        return False
    elif d == 0 and r1 == r0:  # Окружности не пересекаются, а совпадают
        return False
    else:
        return True


print(circles_intersect(1, 1, 3, 5, 5, 4))
