"""
Lesson 5, Task 3, homework 4.
2 circles intersection.
"""
import math


def circles_intersect():
    d = math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    if d > r1 + r0 or d < abs(r0 - r1):
        print('Два кола не перетинаються.')
    elif d == 0 and r1 == r0:
        print('Два кола співпадають!')
    else:
        print('Два кола перетинаються або мають спільну точку.')


x0 = int(input('Введіть координату центра x першого кола: ', ))
y0 = int(input('Введіть координату центра y першого кола: ', ))
r0 = int(input('Введіть радіус першого кола: ', ))
x1 = int(input('Введіть координату центра x другого кола: ', ))
y1 = int(input('Введіть координату центра y другого кола: ', ))
r1 = int(input('Введіть радіус другого кола: ', ))
circles_intersect()
