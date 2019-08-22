#!/usb/bin/python3


class Exemplu:

    def __init__(self, num):
        self.num = num

    def addToNum(self):
        self.num += 1
        return self

    def classicAdd(self):
        self.num += 1


e = Exemplu(2)
e.addToNum().addToNum().addToNum()
print(e.num)
# e.classicAdd()
# e.classicAdd().classicAdd()
# print(e.num)
