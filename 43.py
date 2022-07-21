# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 15:50:40 2022

@author: Комп
"""

def panc_spisok (L):
    s = '0123456789'
    Rez = []
    for i in L:
        ss = s + ''
        for k in str(i):
            ss = ss.replace(k, '')
        for m in ss:
            a = str(i) + m
            Rez.append(a)
    return Rez
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while len(str(L[0])) != 10:
    T = []
    T = panc_spisok(L)
    L = T.copy()

def prov (x):
    D = [2, 3, 5, 7, 11, 13, 17]
    for i in range(7):
        if (int(x[i+1:i+4]) % D[i]) != 0 :
            return False
   
    return True
Summ = []
for y in L:
    if prov(y) == True:
       Summ.append(int(y)) 
Rezult = sum (Summ)
