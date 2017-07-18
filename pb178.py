import math
import time

t1 = time.time()

c = [-1]*1025000

def count(s,d,l):
    ci = toi(s,d,l)
    if c[ci] > 0:
        return c[ci]
    t = testwhatever(s,d,l)
    if t> 0:
        c[ci] = t
        return c[ci]
    if l == 0:
        return 0
    r = 0
    if d+1 < 10:
        ns = s[:]
        ns[d+1] = True
        r += count(ns,d+1,l-1)
    if d-1 >= 0:
        ns = s[:]
        ns[d-1] = True
        r += count(ns,d-1,l-1)
    c[ci] = r
    return c[ci]

def toi(s,d,l):
    i = 0
    for j in s:
        i *= 2
        if j:
            i += 1
    return i*1000+l*10+d
    

def testwhatever(s,d,l):
    for i in s:
        if not i:
            return -1
    return whatever(d,l)

w = [-1]*500

def whatever(d,l):
    global w
    i = l*10+d
    if w[i] > 0:
        return w[i]
    if l == 0:
        return 1
    r = 0
    if d+1 < 10:
        r += whatever(d+1,l-1)
    if d-1 >= 0:
        r += whatever(d-1,l-1)
    w[i] = r
    return w[i]

def answer(n):
    si = [False,False,False,False,False,False,False,False,False,False]
    r = 0
    for l in range(10,n+1):
        for sd in range(1,10):
            nsi = si[:]
            nsi[sd] = True
            r += count(nsi,sd,l-1)
    return r

print(answer(40))        

print("time:",time.time()-t1)  





