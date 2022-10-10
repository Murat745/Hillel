"""
Lesson 10, homework 7, task 2 solution
Creating a function, that returns a list from any iterables.
"""
import itertools


def lchain(*iterables):
    return list(itertools.chain(*iterables))


def main():
    print(lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)))


if __name__ == '__main__':
    lchain()
    main()
