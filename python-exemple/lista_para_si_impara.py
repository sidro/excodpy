def isEven(num):
    return num % 2 == 0


'''
partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''


def partition(list_, funct):
    return [[li for li in list_ if funct(li)],
            [li for li in list_ if not funct(li)]]


def part(list_, fnc):
    return [[list_.pop(list_.index(e)) for e in list_ if isEven(e)], list_]


print(isEven(3))
print(partition([1, 2, 3, 4], isEven))
print(part([1, 2, 3, 4, 6, 7, 8], isEven))
