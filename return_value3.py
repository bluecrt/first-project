def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
    #print(person)
engineer = build_person('junwang','wu')
print(engineer)
print(engineer['first'] + ' ' + engineer['last'] + ' is a great engineer')