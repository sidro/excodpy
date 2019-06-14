def interleave(name_1, name_2):
    '''solution 1. '''
    zipy = zip(name_1, name_2) # create a zip Iterable object
    string =""
    for n in zipy:
        string += "".join(n) 
    return string

print(interleave('hi', 'ha'))
print(interleave('aaa', 'zzz'))



def interleave2(name_1, name_2):
    '''solution 2. '''
    return "".join("".join(x) for x in zip(name_1, name_2))


print(interleave2('hi', 'ha'))
print(interleave2('aaa', 'zzz'))
