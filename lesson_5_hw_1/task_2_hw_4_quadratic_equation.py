"""
Lesson0 5, homework 4, task 2 solution.
Solution for the quadratic equation ax^2 + bx +c = 0.
"""
import math


def solve_quadratic_equation():
    d = b**2 - 4*a*c
    if b**2 > 4*a*c:
        x1 = round(math.sqrt(-b + d) / 2*a)
        x2 = round(math.sqrt(-b - d) / 2*a)
        print('X1 = ', x1)
        print('X2 = ', x2)
    elif b**2 == 4*a*c:
        x = round(-b / 2*a)
        print('X = ', x)
    else:
        print('No real number roots')
        return None


a = int(input('Input the "a" coefficient: ', ))
b = int(input('Input the "b" coefficient: ', ))
c = int(input('Input the "c" coefficient: ', ))
if a == 0:
    print('Input the correct value of "a" coefficient!')
else:
    solve_quadratic_equation()
