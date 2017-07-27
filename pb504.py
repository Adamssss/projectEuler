import math
import time

t1 = time.time()

def example():
    r = 0 
    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                for d in range(1,5):
                    l = 1
                    l += (a-1)+(b-1)+(c-1)+(d-1)
                    l += exampletri(a,b)
                    l += exampletri(b,c)
                    l += exampletri(c,d)
                    l += exampletri(d,a)
                    if l in [1,4,9,16,25,36,49,64]:
                        r += 1
    return r

def exampletri(x,y):
    r = 0
    for i in range(1,x):
        h = y - y*i/x
        r += math.ceil(h)-1
    return r


def answer():
    N = 100
    sl = []
    for i in range(1,2*N):
        sl.append(i*i)
    r = 0 
    for a in range(1,N+1):
        for b in range(1,N+1):
            for c in range(1,N+1):
                for d in range(1,N+1):
                    l = 1
                    l += (a-1)+(b-1)+(c-1)+(d-1)
                    l += answertri(a,b)
                    l += answertri(b,c)
                    l += answertri(c,d)
                    l += answertri(d,a)
                    if l in sl:
                        r += 1
    return r


ats = [-1]*10000

def answertri(x,y):
    global ats
    if x > y:
        return answertri(y,x)
    atsi = (x-1)*100+(y-1)
    if ats[atsi] >= 0:
        return ats[atsi]
    r = 0
    for i in range(1,x):
        h = y - y*i/x
        r += math.ceil(h)-1
    ats[atsi] = r
    return r


#print(example())

print(answer())

print("time:",time.time()-t1)  





