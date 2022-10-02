"""
Lesson 7, homework 6, task 3a solution
Creating a sorted list by first digit of the number.
"""

original_list = [472, 326, 1, '1101000', 9, '20', 863, '0']
print(sorted(original_list, key=lambda x: str(x)))
