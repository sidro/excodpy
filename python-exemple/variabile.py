#! /usr/bin/env python
fred = 1
pete = 2


def box():
    global fred, pete
    dave = fred + pete
    return vars()

print(vars())
print(box())

