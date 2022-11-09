"""
Lesson 12, homework 9, task 2 solution.
Reading a text file and returning the list of surnames function.
"""


def surnames_from_file(file_name):
    list_of_surnames = []
    for i in open(file_name):
        list_of_surnames.append(i)

    for i in range(len(list_of_surnames)):
        list_of_surnames[i] = list_of_surnames[i].split()
        list_of_surnames[i] = list_of_surnames[i][1]

    return list_of_surnames


print(surnames_from_file("names.txt"))
