# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:31:42 2022

@author: Комп
"""

from fractions import Fraction

n = Fraction(5, 2)

a = 0
Rez = []
while a < 999:
    n = Fraction(2 * n + 1, n )
    Rez.append(n)
    a += 1

R = []
for n in Rez:
    a = str(Fraction(n + 1, n))
    
    R.append(a)

Rezult = []
for i in R:
    A = i.split('/')
    Q = list(map(len, A))
    if Q[0] > Q[1]:
        Rezult.append(A)
        
Itog = len(Rezult)