def intersect(list_1, list_2):
    return list(set(list_1) & set(list_2))


print(intersect([1, 2, 3], [2, 3, 4]))
print(intersect(['a', 'v', 'z', 'c'], ['a', 'c', 'x']))
