"""
Lesson 10, homework 7, task 2 solution
Creating a function, that returns a list from any iterables.
"""


def lchain(*iterables):
    result_list = []
    for i in iterables:
        if isinstance(i, dict):
            for key, value in i.items():
                result_list.append(key)

        elif isinstance(i, list):
            for item in i:
                result_list.append(item)

        elif isinstance(i, tuple):
            for item in i:
                result_list.append(item)

        elif isinstance(i, (int, float, type(None), str, bool)):
            result_list.append(i)

        elif isinstance(i, range):
            for item in i:
                result_list.append(item)

        else:
            raise ValueError("unexpected type")

    return result_list
