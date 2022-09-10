# Площа поверхні і об'єм конусу.
from math import pi


class Cone:
    @staticmethod
    def area(r, h):
        a = pi * r**2 
        b = pi * r * (r**2 + h**2)**0.5
        return a + b

    @staticmethod
    def volume(r, h):
        c = pi * r ** 2 * h
        return c/3


r = float(input("Введіть радіус конусу : "))
h = float(input("Введіть висоту конусу : "))
u = Cone()
print("Площа поверхні конуса становить : {0:.3f}".format(u.area(r, h)))
print("Об'єм конуса становить : {0:.3f}".format(u.volume(r, h)))
