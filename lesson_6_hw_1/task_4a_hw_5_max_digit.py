"""
Lesson 6, homework 5, task 4a solution.
"""
import random
number = str(random.randint(100000000000, 999999999999))


def get_max_digit(number):
    maxx = -1

    for n in number:
        i = int(n)
        if i > maxx:
            maxx = i
    return maxx


def main():
    print(get_max_digit(number))


if __name__ == '__main__':
    main()
