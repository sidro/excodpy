def remove_negatives(args):
    return list(filter(lambda x: x >= 0, args))


list_ = [-1, 2, -3, 5, 6, -9, 4]
print(remove_negatives(list_))
