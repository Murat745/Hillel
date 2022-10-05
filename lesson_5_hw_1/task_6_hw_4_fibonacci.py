"""
Lesson 5, homework 4, task 6 solution.
Finding the n-th Fibonacci number
"""


def fibonacci(n):
    seq1 = seq2 = 1
    n = int(n) - 3

    while n > 0:
        seq1, seq2 = seq2, seq1 + seq2
        n -= 1
    return seq2
