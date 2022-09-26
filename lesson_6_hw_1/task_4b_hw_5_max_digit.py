"""
Lesson 6, homework 5, task 4b solution.
"""

import random
number = random.randint(100000000000, 999999999999)


def get_max_digit(number):
    print(number)  # Для наглядності
    maximum = 0

    while number:
        number, n = divmod(number, 10)
        maximum = max(maximum, n)

    return maximum


result = get_max_digit(number)
print(result)
