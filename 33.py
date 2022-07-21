from fractions import Fraction
A = list (A for A in range (12, 50))
A.remove(20)
A.remove(40)
A.remove(30)
def prov (H):
    s = str(H[0])
    s0 = s[0]
    s1 = s[1]
    R = []
    r = []
    for i in H:
        y = str (i)
        if y == s:
            pass
        elif (s[0] in y) == True:
            a = int(y.replace(s[0],''))
            w1 = Fraction(H[0], i)
            w2 = Fraction(int(s[1]), a)
            if w1 == w2:
                r = [i , w2]
            R.append(r)
        elif (s[1] in y) == True:
            a = int(y.replace(s[1], ''))
            w1 = Fraction(H[0], i)
            w2 = Fraction(int(s[0]), a)
            if w1 == w2:
                r = [i , w2]
                R.append(r)
    if len(R) == 0 or R == [[]]:
        return 0
    else:
        return R
     
def cder (x):
    D = [x]
    for i in range(2, 10):
        p = x * i
        if p < 100 and p % 10 != 0:
            D.append(p)
    return D
Baza = []
for k in A:
    Q = cder(k)
    if len(Q) != 1:
        Baza.append(Q)
Baza2 = []

for i in Baza:
    L = prov(i)
    if L != 0 :
        print (i[0], L)
        Baza2.append(L)
