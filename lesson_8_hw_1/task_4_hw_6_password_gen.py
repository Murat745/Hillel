"""
Lesson 8, homework 6, task 4 solution
Creating a password generator.
"""

import random
import string


print('Your automatically generated password:')

length = 8
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = '_'
total = lower + upper + num + symbols
temp = random.sample(total, length)
password = "".join(temp)
while password:
    if (any(c.islower() for c in password) and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)):
        break

print(password)
