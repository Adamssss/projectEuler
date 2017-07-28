import math
import time

t1 = time.time()

# similar to problem 172

# 0~9 counts 0~2 ==>3^10
# remainder 0~10 

lc = [-1]*((3**10)*100+100)

def counts(l,r):
    global lc
    lci = toi(l,r)
    if lc[lci] >= 0:
        return lc[lci]
    lcn = ton(l)
    if lcn == 20:
        if r % 11 == 0:
            lc[lci] = 1
            return 1
        else:
            lc[lci] = 0
            return 0
    result = 0
    for i in range(10):
        if l[i] < 2:
            nl = l[:]
            nl[i] += 1
            nr = (r*10+i)%11
            result += counts(nl,nr)
    lc[lci] = result
    return result

def toi(l,r):
    i = 0
    for j in l:
        i = i*3+j
    return i*100+r

def ton(l):
    return sum(l)

def answer():
    l = [0]*10
    r = 0
    for i in range(1,10):
        nl = l[:]
        nl[i] += 1
        r += counts(nl,i)
    return r

print(answer())

print("time:",time.time()-t1)  





