"""
Lesson 7, homework 6, task 1 solution
Getting the index (first match) of the element in list.
"""

lst = ['a', 'b', 'c', 1, 2, 3, [3, 2, 1]]


def index(lst, elem):
    if elem in lst:
        for i, j in enumerate(lst):
            if j == elem:
                return i
    else:
        return 'None'
