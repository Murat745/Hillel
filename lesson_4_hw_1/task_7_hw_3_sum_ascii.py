# Сума цифр тризначного числа за допомогою ASCII коду


def sum_ascii(a):
    x = ord(a[0])
    y = ord(a[1])
    z = ord(a[2])
    return (x-48) + (y-48) + (z-48)


a = input('Введіть тризначне число: ', )
print('Сума цифр введеного числа = ', sum_ascii(a))
