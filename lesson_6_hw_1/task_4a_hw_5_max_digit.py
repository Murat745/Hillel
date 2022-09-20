"""
Lesson 6, homework 5, task 4a solution.
"""

import random


def get_max_digit():
    number = str(random.randint(100000000000, 999999999999))
    maxx = -1
    print(number)
    for n in number:
        i = int(n)
        if i > maxx:
            maxx = i
    return maxx


get_max_digit()
