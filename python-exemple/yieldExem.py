a, b, c = 2, 3, 4


def multiReturn():
    yield a
    yield b
    yield c


y = multiReturn()

for i in range(3):
    print(y.__next__())
