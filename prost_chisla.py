# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 18:15:24 2022

@author: Комп"""

M = [ x for x in range(3, 500000, 2)]

def otsev(x):
    r = []
    for i in range(len(L)):
        if x**2 > L[i]:
            r.append(L[i])
        elif L[i] % x != 0:
            r.append(L[i])
    return r
L = M.copy()
n = 0
a = L[n]
while  a < L[-1]:
    L = otsev(a)
    n +=1
    a = L[n]

S = str(L)
S = S[1:-1]
S = S.replace(',', '')

F = open('prost_chisla.txt', 'w+')
F.write(S)
F.close()