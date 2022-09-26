"""
Lesson 6, homework 5, task 7 solution.
Random generated number guessing game.
"""

import random

number = random.randint(1, 10)
guessing = True
while guessing:
    guess = int(input('Вгадайте число від 1 до 10: '))
    if guess > number:
        print('Введене число більше від згенерованого...Спробуйте ще...')
    elif guess < number:
        print('Введене число менше від згенерованого...Спробуйте ще...')
    else:
        guessing = False
        print('Вітаю, Ви вгадали!')
print('Кінець гри!')
