"""
Lesson 6, homework 5, task 3 solution.
"""

import random


def diff_odd_even(num_limit, lower_bound, upper_bound):
    my_list = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    sum_even = sum(i for i in my_list if not i % 2)
    sum_odd = sum(i for i in my_list if i % 2)
    return sum_even - sum_odd


def main():
    num_limit = int(input('Введіть num_limit: ', ))
    lower_bound = int(input('Введіть lower_bound: ', ))
    upper_bound = int(input('Введіть upper_bound: ', ))
    result = diff_odd_even(num_limit, lower_bound, upper_bound)
    print(result)


if __name__ == '__main__':
    main()
