"""
Lesson 5, homework 4, Task 4 solution.
Leap year.
"""

year = int(input('Введіть рік: ', ))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
