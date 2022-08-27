import decimal
from decimal import Decimal
uah = input('Введіть суму гривень для обміну: ', )
usd = round(((Decimal(uah)) / Decimal(41.2)), 2)
print('Станом на 28.08.2022 р. введена Вами сума дорівнює', usd, 'дол. США.')

