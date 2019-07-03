def extract_full_name(names):
    ''' *SOLUTIA NUMARUL 1* '''
    return list(map(lambda x: " ".join(x), (i.values() for i in names)))


def extract_full_name2(names):
    ''' *SOLUTIA NUMARUL 2* '''

    return list(map(lambda x: " ".join(iter(x.values())), names))


def extract_full_name3(names):
    ''' *SOLUTIA NUMARUL 3* '''

    return list(
        map(lambda val: "{} {}".format(val['first'], val['last']), names)
    )


names = [
    {'first': 'Elie', 'last': 'Schoppik'},
    {'first': 'Colt', 'last': 'Steele'}
]

extract = extract_full_name(names)  # ['Elie Schoppik', 'Colt Steele']
print(extract)

extract2 = extract_full_name2(names)  # ['Elie Schoppik', 'Colt Steele']
print(extract2)

extract3 = extract_full_name3(names)  # ['Elie Schoppik', 'Colt Steele']
print(extract3)
