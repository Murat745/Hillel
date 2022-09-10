# Не понял задачу. Не смог сделать функцией:(
summa = 0
while True:
    n = input("Введіть число або 'стоп' для виходу: ")
    if str(n) == "стоп":
        print("Вихід з програми!")
        break  # вихід
    else:
        summa = summa + int(n)
        print(summa)
