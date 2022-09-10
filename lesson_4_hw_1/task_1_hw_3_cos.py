# cos кута в радіанах за допомогою ряду Тейлора
from decimal import getcontext
from math import pi


def degrees_to_rads(deg):
    return (deg * pi) / 180.0


def cos(x):
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i - 1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s


print(cos(degrees_to_rads(40)))
print(cos(degrees_to_rads(45)))
print(cos(degrees_to_rads(60)))
