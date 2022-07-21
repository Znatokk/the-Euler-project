# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:15:54 2022

@author: Комп
"""
f = open('59.txt', 'r')
S = f.read()
f.close()
D = S.split(',')
D = list(map(int, D))

simvo = 'qazwsxedcrfvtgbyhnujmikolp'
Baza = 'QAZWSXEDCRFVTGBYHNUJMIKOLP '
simvol = list(simvo)
Baza = Baza + simvo + '"' + "'" + ','


Stroka1 = [D[i] for i in range (0, 1455, 3)]
Stroka2 = [D[i] for i in range (1, 1455, 3)]
Stroka3 = [D[i] for i in range (2, 1455, 3)]
Q = [Stroka1, Stroka2, Stroka3]
W = []

for k in simvo:
    for k2 in simvo:
        if k2 == k:
            continue
        for k3 in simvo:
            if k3 == k or k3 == k2:
                continue
            w = [k, k2, k3]
            W.append(w)

Nabor =[]            
for K in W:
    K = list(map(ord, K))            
    Nabor.append(K)        

def decoder (kod, text):
    p = 1
    Rez = []
    for i in text:
        if p == 1:
           # Rez = Rez + chr(i^kod[0])
            a = chr(i^kod[0])
            Rez.append(a)
            p = 2
        elif p == 2:
           # Rez = Rez + chr(i^kod[1])
            a = chr(i^kod[1])
            Rez.append(a)
            p = 3
        elif p == 3:
           # Rez = Rez + chr(i^kod[2])
            a = chr(i^kod[2])
            Rez.append(a)
            p = 1
    return Rez
m = 0            
for i in Nabor:
    Spisok = decoder(i, D)
    for i in Spisok:
        if i not in Baza:
            m = 0
            break
    if m != 0:
        print ('fdbv')
        break
