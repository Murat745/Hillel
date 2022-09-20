"""
Lesson 6, homework 5, task 7 solution.
Random generated number guessing game.
"""

import random

number = random.randint(1, 100)
guessing = True
while guessing:
    guess = int(input('Вгадайте ціле число: '))
    if guess > number:
        print('Введене число більше від згенерованого...Спробуйте ще...')
    elif guess < number:
        print('Введене число менше від згенерованого...Спробуйте ще...')
    else:
        guessing = False
        print('Вітаю, Ви вгадали!')
print('Кінець гри!')
