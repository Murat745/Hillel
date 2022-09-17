"""
Lesson 5, homework 4, task 6 solution.
Finding the n-th Fibonacci number
"""


def fibonacci(n):
    if n in (2, 3):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input('Enter the number\'s position in the Fibonacci\'s sequense: ', ))
print(fibonacci(n))
