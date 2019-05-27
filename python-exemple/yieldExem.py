a, b, c = 2, 3, 4


def multi_return():
    yield a
    yield b
    yield c


y = multi_return()

for i in range(3):
    print(y.__next__())
