# Преобразование слов из snake_case в camelCase
snake = input('Введите 3 слова в формате snake_case:', )
x = snake.split('_')
camel = x[0] +''.join(ele.title() for ele in x[1:])
print('Ваше слово в формате CamelCase: ', '' + str(camel))


