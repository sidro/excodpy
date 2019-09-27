def find_greater_numbers(list_):
    count = 0
    i = 0
    j = 1
    while i < len(list_):
        while j < len(list_):
            if list_[j] > list_[i]:
                count += 1
            j += 1
        j = i+1
        i += 1
    return count


print(find_greater_numbers([6, 1, 2, 3, 7]))
print(find_greater_numbers([5, 3, 2, 1]))
print(find_greater_numbers([3, 2, 1, 4]))
