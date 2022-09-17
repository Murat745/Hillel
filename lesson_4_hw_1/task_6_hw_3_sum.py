"""
Lesson 4, homework 3, task 6 solution.
Fixed
"""


def my_sum(*nmbrs):
    start = 0
    for n in nmbrs:
        start += n
    return start


print(my_sum(1, 2, 3))
