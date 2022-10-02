"""
Lesson 8, homework 6, task 2 solution
Creating a deepcopy of the list.
"""

lst = ['a', 1, 2.0, ['b']]


def copydeep(x):
    if not isinstance(x, list):
        return x
    else:
        return [copydeep(elem) for elem in x]
