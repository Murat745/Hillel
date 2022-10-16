"""
Lesson 6, homework 5, task 2 solution.
Difference between max and min elements of the random list.
"""

import random


def diff_min_max(num_limit, lower_bound, upper_bound):
    my_list = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    return max(my_list) - min(my_list)


def main():
    num_limit = int(input('Введіть num_limit: ', ))
    lower_bound = int(input('Введіть lower_bound: ', ))
    upper_bound = int(input('Введіть upper_bound: ', ))
    result = diff_min_max(num_limit, lower_bound, upper_bound)
    print(result)


if __name__ == '__main__':
    main()
