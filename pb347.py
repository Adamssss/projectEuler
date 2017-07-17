import math
import time

t1 = time.time()

N = 10000000

prime = []

def primeSieve(n):
    global prime
    n = (n+1)//2
    p = [True]*(n)
    i = 1
    prime.append(2)
    while i < n:
        if p[i]:
            t = 2*i+1
            prime.append(t)
            p[i] = False
            j = 2*i*i+2*i
            while j < n:
                p[j] = False
                j += t
        i += 1
    return prime

primeSieve(N//2 + 100)

def S(n):
    result = 0
    for i in range(0,len(prime)-1):
        if prime[i]*prime[i] > n:
            break
        for j in range(i+1,len(prime)):
            if prime[i]*prime[j] > n:
                break
            result += M(prime[i],prime[j],n)
    return result

def M(p,q,n):
    if p*q > n:
        return 0
    m = p*q
    r = m*Mh(p,q,n//m)
    #print(p,q,n,r)
    return r

def Mh(p,q,n):
    if p > n and q > n:
        return 1
    t = 1
    c = 0
    while t <= n:
        t= p*t
        c += 1
    t = t//p
    c -= 1
    m = t
    while c > 0:
        t = t//p
        c -= 1
        if t*q <= n:
            t = t*q
            if t > m:
                m = t
    return m
    

print(S(N))



print("time:",time.time()-t1)  


    
