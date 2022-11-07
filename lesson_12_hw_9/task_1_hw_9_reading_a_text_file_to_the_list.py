"""
Lesson 12, homework 9, task 1 solution.
Reading a text file to the list.
"""


def from_file_to_list(file_name):
    list_of_domains = []
    for i in open(str(file_name)):
        list_of_domains.append(i)

    for i in range(len(list_of_domains)):
        list_of_domains[i] = list_of_domains[i][1:]
        list_of_domains[i] = list_of_domains[i].strip()

    print(list_of_domains)


from_file_to_list("domains.txt")
