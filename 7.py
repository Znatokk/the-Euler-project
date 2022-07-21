c = 3
t = 2
while t != 10001:
    c +=1
    if c % 2 == 0:
        continue
    for i in range (3, c, 2):
        if c % i == 0:
            continue
    print (c)
    t += 1
    