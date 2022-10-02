"""
Lesson 8, homework 6, task 5 solution
Prime numbers list in range from 1 to 100.
"""


def gen_primes(n):
    result = list()
    selection = [True] * (n+1)
    for p in range(2, n+1):
        if selection[p] and selection[p] % 2 == 1:
            result.append(p)
            for i in range(p, n+1, p):
                selection[i] = False
    return result


print(gen_primes(100))
