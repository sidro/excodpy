def isEven(num):
    return num % 2 == 0


'''
partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''


def partition(list_, funct):
    return [[li for li in list_ if funct(li)],
            [li for li in list_ if not funct(li)]]


print(isEven(3))
print(partition([1, 2, 3, 4], isEven))
