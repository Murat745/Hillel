"""
Lesson 6, homework 5, task 4b solution.
"""

import random


def get_max_digit():
    number = random.randint(100000000000, 999999999999)
    print(number)
    maximum = 0

    while number:
        number, n = divmod(number, 10)
        maximum = max(maximum, n)

    return maximum


get_max_digit()
