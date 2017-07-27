import math
import time

t1 = time.time()


# x^y mod z
def mod(x,y,z):
    if y == 0:
        return 1
    if y == 1:
        return x%z
    if x == 1:
        return 1
    t = x
    n = 1
    while t < z:
        t *= x
        n += 1
        if n >= y:
            return (x**y)%z
    a = y//n
    b = y%n
    return (mod(t%z,a,z)*mod(x,b,z))%z
'''
fac = [1]
for i in range(1,30000):
    fac.append(fac[i-1]*i)

def collapse(l):
    result = []
    for i in l:
        exist = False
        for j in result:
            if i[0] == j[0]:
                exist = True
                j[1] += i[1]
        if not exist:
            result.append([i[0],i[1]])
    return result

def c(n,k):
    return fac[n]//fac[k]//fac[n-k]

def csubs(cur,choices):
    if len(choices)==0:
        return cur
    ncur = []
    for i in range(choices[0][1]+1):
        ci = c(choices[0][1],i)
        for j in cur:
            r = (j[0]+choices[0][0]*i)%250
            sc = (j[1]*ci)%(10**16)
            ncur.append([r,sc])
    nchoices = choices[1:]
    return csubs(collapse(ncur),nchoices)

def answer():
    a =[[0,1]]
    b = collapse(remainder)[:]
    #print(b)
    csubsr = csubs(a,b)
    #print(csubsr)
    for j in csubsr:
        if j[0] == 0:
            result = j[1]
            break
    return result-1

#print(answer())
'''

def solve():
    N = 250250
    modn = 10**16
        
    s = [0]*(250)
    s[0] = 1
    for i in range(1,N+1):
        r = mod(i,i,250)
        s = progress(s,r,modn)
    return s[0]-1

def progress(s,r,modn):
    ns = s[:] 
    for i in range(250):
        ni = (r+i)%250
        ns[ni] =(ns[ni]+ s[i])% modn
    return ns

print(solve())

print("time:",time.time()-t1)  





