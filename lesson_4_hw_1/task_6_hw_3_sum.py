"""
Lesson 4, homework 3, task 6 solution.
Fixed
"""


def my_sum(*args, start=0):
    if not args:
        return start
    else:
        return sum(args, start)
