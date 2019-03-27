#! /usr/bin/env python

global fred, pete
fred = 1
pete = 2


def box():
    dave = fred + pete
    return dave


print(box())
