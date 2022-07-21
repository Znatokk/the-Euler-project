# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 00:31:58 2022

@author: Комп
"""

f = open('prost_chisla.txt', 'r') 
S = f.readline()
f.close()
T = list(S.split())
R = list(map(int, T))
R.insert(0, 2)


def ryad(a): # разложение числа на простые множетили
     r = []
     for i in R:
         if a == 1:
             return r
         elif a % i == 0:
             while True:
                 a = a/i
                 r.append(i)
                 if a% i != 0:
                     break

def prov(x): #проверка числа на количество простых множителей здесь 4 множ
    if len(set(ryad(x))) == 4:
        return True
    else:
        return False
    
a = 0
Rez = []

for n in range(100000, 1000000):
    #print (prov(n))
    if prov(n) == True:
        a = a + 1
       # print (a)
        Rez.append(n)
        if a == 4:
            break
    else:
        a = 0
        Rez = []
D = []
for i in Rez:
    W = ryad(i)
    D.append(W)
