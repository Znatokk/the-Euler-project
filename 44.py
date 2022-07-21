# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:23:36 2022

@author: Комп
"""
import math

def prov (m):
    n = (math.sqrt(1 + 24 * m) + 1)/6
    if int(n) == n:
        return True
    return False
D = [x * ((3 * x - 1)) /2 for x in range(1000, 10000)]
W = []

for i in range(len(D)):
    a = D[i]
    for b in D[i:]:
        if prov(a+b) == True and prov(b-a) == True:
            W.append([a, b, a + b, b - a])
            
        