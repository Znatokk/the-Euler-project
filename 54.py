# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:00:20 2022

@author: Комп
"""

def nachalo():
    global Pari
    f = open('poker.txt', 'r')
    L = []
    while True:
        line = f.readline()
        if not line:
            break
        L.append(line)
    f.close()
    Pari = []
    for H in L:
        A = [H[0: 14], H[15: 30]]
        Pari.append(A)
    return Pari
    
def mast(s): # определение масти набора карт, если одинакове то True
    mat = ''
    for i in range(1, 14, 3):
        mat += s[i]
        a = s[i]
    
    if mat.count(a) == 5:
        return True
    else:
        return False
    
    
def znach(s): # создание списка набора карт в виде численных значений
    Baza = { 'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
    Z = []
    for i in range(0, 14, 3):
        if s[i] in Baza:
            Z.append(Baza[s[i]])
        else:
            Z.append(int(s[i]))
    Z.sort(reverse=True)
    return Z

def prov_posled (X): # определение ряда как последовательности 
    for i in range(len(X)-1):
        if (X[i] - X[i+1]) != 1:
            return False
    return True    

def opred_mast(X): # определение группы карт одной масти по вариантам
    if prov_posled(X) == False:
        R = [6, 0, 0, 0, 0]+ X
        return R
    if prov_posled(X) == True and X[0] == 14:
        R = [10]
        return R
    else:
        R = [9, 0, 0, 0, 0] + X
        return R

def  yrov_nemast(Sp, Sl): # определение группы карт разхной масти - вспомогательная
    if len(Sl) == 5:
        R = [1, 0, 0, 0, 0] + Sp
        return R
    elif 4 in Sl.values():
        for items in Sl.items():
            if items[1] == 4:
                a = items[0]
            else:
                b = items[0]
        R = [8, a, 0, 0, 0, b]
        return R
    elif 3 in Sl.values() and 2 in  Sl.values():
        for items in Sl.items():
            if items[1] == 3:
                a = items[0]
            else:
                b = items[0]
        R = [7, 0, a, b, 0, 0]
        return R
    elif 3 in Sl.values():
        r = []
        for items in Sl.items():
            
            if items[1] == 3:
                a = items[0]
            else:
                b = items[0]
                r.append(b)
        r.sort(reverse=True)
        R = [4, 0, a, 0, 0]+ r
        return R
    elif 2 in Sl.values() and len(Sl) == 4:
        r = []
        for items in Sl.items():
            
            if items[1] == 2:
                a = items[0]
            else:
                b = items[0]
                r.append(b)
        r.sort(reverse=True)
        R = [2, 0, 0, a, 0] + r
        return R
    else:
        r = []
        for items in Sl.items():
            k = 0
            if items[1] == 2 and k == 0:
                a = items[0]
                k = 1
                r.append(a)
            elif items[1] == 2 and k != 0:
                c = items[0]
                r.append(c)
                r.sort(reverse=True)
            else:
                b = items[0]
                r.append(b)
        r.sort(reverse=True)
        R = [3, 0, 0, r[0], r[1], b]
        return R
        
def opred_nemast(V): # определение группы 
    if prov_posled(V) == True:
        R = [5, 0, 0, 0, 0] + V
        return R
    else:
        Vrem = {}
        for i in V:
            Vrem[i] = Vrem.get(i, 0) + 1
        R = yrov_nemast(V, Vrem)    
    return R
        
def partia(L): # определения значения партии
    Ryad = znach(L)
    if mast(L) == True:
        Rez = opred_mast(Ryad)
    else:
        Rez = opred_nemast(Ryad)
    return Rez


def sravnenie(R):
    if R[0][0] > R[1][0]:
        return '1-й игрок'
    elif R[0][0] < R[1][0]:
        return '2-й игрок'
    else:
        for i in range(len(R[0])):
           if R[0][i] > R[1][i]:
               return '1-й игрок'
           elif  R[0][i] < R[1][i]:
               return '2-й игрок'
        return 'они равны'
           



def main ():
    global Pari, Partiya_itog
    Pari = nachalo()
    Partiya_itog = []
    for K in Pari:
        Partiya = []
        for T in K:
            Rasclad = partia (T)
            Partiya.append(Rasclad)
        itog = sravnenie(Partiya)
        Pr = [K, itog]
        Partiya_itog.append(Pr)
    return Partiya_itog

if __name__ == '__main__':
    main()


