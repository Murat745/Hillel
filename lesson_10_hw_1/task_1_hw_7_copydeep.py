"""
Lesson 10, homework 7, task 1 solution
Creating a deepcopy of something without import.
"""


def copydeep(data):
    if isinstance(data, list):
        return list(map(copydeep, data))
    elif isinstance(data, tuple):
        return tuple(map(copydeep, data))
    elif isinstance(data, dict):
        return {copydeep(key): copydeep(value) for key, value in data.items()}
    return data
