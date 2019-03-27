#! /usr/bin/env    python3.6


class Variabile:

    global fred, pete, maria
    maria = 5
    fred = 1
    pete = 2

    def vari(self):
        self.maria = 3
        self.dave = fred + pete + self.maria
        print(pete)
        # return

    print(maria)


v = Variabile()
v.vari()
print(v.dave)
print(v.maria)
