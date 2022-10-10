"""
Lesson 10, homework 7, task 1 solution
Creating a deepcopy of something without import.
"""


def copydeep(smthng):

    if isinstance(smthng, dict):
        result = {}
        for key, value in smthng.items():
            result[key] = copydeep(value)

        assert id(result) != id(smthng)

    elif isinstance(smthng, list):
        result = []
        for item in smthng:
            result.append(copydeep(item))

        assert id(result) != id(smthng)

    elif isinstance(smthng, tuple):
        aux = []
        for item in smthng:
            aux.append(copydeep(item))
        result = tuple(aux)

        assert id(result) != id(smthng)

    elif isinstance(smthng, (int, float, type(None), str, bool)):
        result = smthng
    else:
        raise ValueError("unexpected type")

    return result
