"""
Lesson 8, homework 6, task 3a solution
Creating a sorted list by the value of the number.
"""

original_list = [5, '9', 0, '452', 6.5, '6', 1, 2]
print(sorted(original_list, key=lambda x: float(x)))
