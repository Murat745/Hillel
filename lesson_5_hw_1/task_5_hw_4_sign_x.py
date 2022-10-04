"""
Lesson 5, homework 4, Task 5 solution.
Sign(x) definition.
"""


def sign(x):
    if x > 0:
        result = 1
    elif x < 0:
        result = -1
    else:
        result = 0
    return result
