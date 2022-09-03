a = str(input('Введите имя, даты рождения и смерти:', ))
name = a[:-22]
life = a[-21:]
age = int(life[11:15]) - int(life[0:4])
print('Name: ', name)
print('Age: ', age, 'years')
