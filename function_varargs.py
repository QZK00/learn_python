def total(a=5,*number,**phonebook):
    print('a', a)
    for single_term in number:
        print('single term ', single_term)
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)
print(total(3,4,1,4,Jack=1123,John=2231,Inge=1561))