"""
Lesson 11, homework 8, task 1 solution
Decorator
"""
import functools


class UnexpectedTypeException(Exception):
    pass


def expected(*expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_variable = func(*args, **kwargs)
            if not isinstance(func_variable, expected_types):
                raise UnexpectedTypeException('Was expecting types int, str, float, dict')
            else:
                print(func(*args, **kwargs))
        return wrapper
    return decorator


@expected(int, str, float, list)
def function(value):
    return value


function({'Argentina': 5, 'Jamaica': 0})  # UnexpectedTypeException: Was expecting types int, str, float, dict
