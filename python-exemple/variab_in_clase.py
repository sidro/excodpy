#! /usr/bin/env python


class Variabile:
    global fred, pete
    fred = 1
    pete = 2

    def variabile(self):
        self.dave = fred + pete
        return vars()

v = Variabile()
print(v.variabile())
print(v.dave)
