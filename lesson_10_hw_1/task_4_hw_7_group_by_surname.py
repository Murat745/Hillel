"""
Lesson 10, homework 7, task 4 solution
Function that divides students to groups
"""


def group_by_surname(list_of_enrollees):
    a_i_group = []
    j_p_group = []
    q_t_group = []
    u_z_group = []
    index = 0
    while index < len(list_of_enrollees):
        enrollee = list_of_enrollees[index]
        name, surname = enrollee.split()
        if 'A' <= surname[0] <= 'I':
            a_i_group.append(enrollee)
        elif 'J' <= surname[0] <= 'P':
            j_p_group.append(enrollee)
        elif 'Q' <= surname[0] <= 'T':
            q_t_group.append(enrollee)
        elif 'U' <= surname[0] <= 'Z':
            u_z_group.append(enrollee)
        index += 1
    return len(a_i_group), len(j_p_group), len(q_t_group), len(u_z_group)


def main():
    list_of_enrollees = ['Ivan Muratov', 'Oleg Fesenko', 'Yulia Buriak',
                         'Olga Tarasova', 'Kateryna Antonova', 'Alexander Nestertsov',
                         'Alexander Romashko']
    group_a_i, group_j_p, group_q_t, group_u_z = group_by_surname(list_of_enrollees)
    print(f'"A-I" group: {group_a_i} enrollees.\n'
          f'"J-P" group: {group_j_p} enrollees.\n'
          f'"Q-T" group: {group_q_t} enrollees.\n'
          f'"U-Z" group: {group_u_z} enrollees.')


if __name__ == '__main__':
    main()
