# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 10:36:09 2022

@author: Комп
"""

f = open('prost_chisla.txt', 'r') 
S = f.readline()
f.close()
T = list(S.split())
Prostie_chisla= list(map(int, T))

def prost_ch (F):
    d = 0
    for y in F:
        if y in Prostie_chisla:
            d += 1
    return d

test = 0.3
i = 2
a = 3
Diaog = []
c = 0
while test >= 0.1:
    L = [a + i * k for k in range(4)]
    a = L[3] + i + 2
    Diaog += L[0 : 3]
    c += prost_ch(L[0 : 3])
    test = c /  len(Diaog)
    i += 2
    
storona = int(i/2 - 2)    
