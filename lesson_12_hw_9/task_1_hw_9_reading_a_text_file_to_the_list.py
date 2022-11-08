"""
Lesson 12, homework 9, task 1 solution.
Reading a text file to the list.
"""


def from_file_to_list(file_name):
    list_of_data = []
    for i in open(file_name):
        list_of_data.append(i)

    for i in range(len(list_of_data)):
        list_of_data[i] = list_of_data[i][1:]
        list_of_data[i] = list_of_data[i].strip()

    return list_of_data


print(from_file_to_list("domains.txt"))
