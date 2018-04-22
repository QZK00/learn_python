def print_lol(lists, indests=False, level=0):
    for iteams_each in lists:
        if isinstance(iteams_each, list):
            print_lol(iteams_each, indests, level+1)
        else:
            if indests:
                for tab_stop in range(level):
                    print('\t', end=' ')
            print(iteams_each)

case = ['dsda','gsaeas','adad',['dadf', 'gews', 'asdad']]
print_lol(case, True)
print_lol(case, True, 3)