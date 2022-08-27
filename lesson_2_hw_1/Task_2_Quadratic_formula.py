import decimal
from decimal import Decimal
a = Decimal(1)
b = Decimal(5)
c = Decimal(4)
x = round((- b + (b**2 - 4*a*c) ** Decimal(0.5)) / (2 * a))
y = round((- b - (b**2 - 4*a*c) ** Decimal(0.5)) / (2 * a))
print ('X1 = ', x)
print('X2 = ', y)
