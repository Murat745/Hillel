"""
Lesson 6, homework 5, task 6 solution.
Unicode symbols codes sum.
"""


def sum_symbol_codes(first, last):
    start_code = ord(str(first))
    stop_code = ord(str(last))
    if start_code < stop_code:
        code_range = sum(range(start_code, stop_code + 1))
        return code_range
    else:
        code_range = sum(range(stop_code, start_code + 1))
        return code_range


def main():
    first_symbol = input('Enter first symbol: ')
    last_symbol = input('Enter last symbol: ')
    print('The Unicode symbol codes sum is: ', sum_symbol_codes(first_symbol, last_symbol))


if __name__ == '__main__':
    main()
