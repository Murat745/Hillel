a = str(input('Введите любое целое число: ', ))
sum = 0
for elem in a:    # Решил применить цикл:)
    if elem.isdigit():
        sum += int(elem)
print('Сумма цифр Вашего числа равна: ', sum)

