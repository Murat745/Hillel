"""
Lesson 6, homework 5, task 2 solution.
Difference between max and min elements of the random list.
"""

import random


def diff_min_max():
    num_limit = int(input('Enter the list size: ', ))
    lower_bound = int(input('Enter the lower_bound: ', ))
    upper_bound = int(input('Enter the upper_bound: ', ))
    my_list = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    print(my_list)
    return max(my_list) - min(my_list)


diff_min_max()
