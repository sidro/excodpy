#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:41:19 2018

@author: sidro
"""

class Mamaliga:
        
    def __init__(self, variabila = 0):
        self.variabila = variabila
        self.calc = 0
        
    def calcul(self):
        self.calc = self.calc + 5
        
    def returneaza(self):
        return self.calc

cl = Mamaliga(5)
cl.calcul()
print(cl.returneaza())