# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:46:28 2021

@author: Комп
"""

f1 = '123456789'
A = []
W = []
for k1 in f1:
    f2 = f1.replace(k1, '')
    for k2 in f2:
        f3 = f2.replace(k2, '')
        for k3 in f3:
            f4 = f3.replace(k3, '')
            for k4 in f4:
                f5 = f4.replace(k4, '') 
                for k5 in f5:
                    f6 = f5.replace(k5, '') 
                    s1 = str(int(k1) * int(k2 + k3 + k4 + k5))
                    s2 = str(int(k1 + k2) * int(k3 + k4 + k5))
                    ret1 = 0
                    ret2 = 0
                    for t in f6:
                        if s1.count(t) != 0 and len(s1) == 4:
                            ret1 +=1
                        if s2.count(t) != 0 and len(s2) == 4:
                            ret2 +=1
                    if ret1 == 4:
                        W = [k1, k2 + k3 + k4 + k5, s1]
                        A.append(W)
                    if ret2 == 4:
                        W = [k1 + k2, k3 + k4 + k5, s2]
                        A.append(W)
b = []
for i in A:
    b.append(int(i[2]))
symma = sum(list(set(b)))                    