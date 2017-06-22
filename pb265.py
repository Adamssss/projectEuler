import math
import time

t1 = time.time()

# N = 3
# rd = [0,0,0,1,0,1,1,1]
# rc = [0,1,10,101,11,111,110,100]
# rv = [0,1,2,5,3,7,6,4]
# rvf = [0,0,1,2,1,3,3,2] (//2)
# rvl = [0,1,2,1,3,3,2,0] (%4)

N = 5
tp = [1,2,4,8,16,32]

def foo(n):
    M = tp[n]
    b = tp[n-1]
    test = [[0,1]]
    ntest = []
    r = []
    while True:
        for i in test:
            if len(i) == M and i[-1] == b:
                #print(i)
                r.append(i)
                continue
            j = i[-1]%b
            p = j*2
            if p not in i:
                ntest.append(i+[p])
            p += 1
            if p not in i:
                ntest.append(i+[p])
        if len(ntest) == 0:
            break
        test = ntest
        ntest = []
    return r

def tob(s,n):
    r = []
    M = tp[n]
    for i in s:
        rt = [0]*n
        for j in range(1,M-n+1):
            rt.append(i[j]%2)
        r.append(rt)
    return r

def tod(s):
    r = 0
    for i in s:
        t = 0
        for j in i:
            t = t*2+j
        #print(t)
        r += t
    return r
        
print(tod(tob(foo(N),N)))

print("time:",time.time()-t1)  


    
