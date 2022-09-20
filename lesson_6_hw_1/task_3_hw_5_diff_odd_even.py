"""
Lesson 6, homework 5, task 3 solution.
"""

import random


def diff_odd_even():
    num_limit = int(input('Enter the list size: ', ))
    lower_bound = int(input('Enter the lower_bound: ', ))
    upper_bound = int(input('Enter the upper_bound: ', ))
    my_list = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    print(my_list)
    sum_even = sum(i for i in my_list if not i % 2)
    sum_odd = sum(i for i in my_list if i % 2)
    return sum_even - sum_odd


diff_odd_even()
