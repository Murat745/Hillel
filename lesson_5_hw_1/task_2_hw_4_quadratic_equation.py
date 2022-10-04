"""
Lesson0 5, homework 4, task 2 solution.
Solution for the quadratic equation ax^2 + bx +c = 0.
"""
import math


def solve_quadratic_equation(a, b, c):
    if a != 0:
        d = (b ** 2) - (4 * a * c)
        if d < 0:
            return None
        elif d == 0:
            x = - b / (2 * a)
            return x
        else:
            sq_d = math.sqrt(d)
            x1 = (-b + sq_d) / (2 * a)
            x2 = (-b - sq_d) / (2 * a)
            return x1, x2
    else:
        return 'IT IS NOT A QUADRATIC FORMULA!'
