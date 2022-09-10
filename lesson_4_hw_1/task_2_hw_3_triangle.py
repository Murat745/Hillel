# Площа і периметр прямокутного трикутника.
class Triang:
    @staticmethod
    def perimeter(a, b):
        c = (a**2 + b**2)**0.5
        return a + b + c

    @staticmethod
    def square(a, b):
        return (a*b)/2


a = float(input("Введіть перший катет : "))
b = float(input("Введіть другий катет : "))
u = Triang()
print("Периметр трикутника становить : {0:.3f}".format(u.perimeter(a, b)))
print("Площа трикутника становить : {0:.3f}".format(u.square(a, b)))
