import math
import time

t1 = time.time()

N = 1000200

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

primeSieve(N)

def S(pI):
    p1 = prime[pI]
    p2 = prime[pI+1]
    dig = math.floor(math.log10(p1))+1
    t = int(math.pow(10,dig))
    S = t+p1
    while S%p2 != 0:
        S += t
    return S

def fS(pI):
    p1 = prime[pI]
    p2 = prime[pI+1]
    t = 1
    while t < p1:
        t *= 10
    d = p2-p1
    r = t%p2
    # n*r - d = k*p2
    # S = n*t + p1
    return getnk(r,d,p2)[0]*t+p1

# for n*a-b = k*c
def getnk(a,b,c):
    if a == 1:
        return [c+b,1]
    if c == 1:
        n = 1
        k = a-b
        while k < 0:
            n += c
            k += a
        return [n,k]
    if a > c:
        na = a%c
        t = a//c
        # (na+t*c)*n-b = k*c
        # na*n-b = (k-t*n)*c
        temp = getnk(na,b,c)
        n = temp[0]
        k = temp[1]
        k += t*n
        while n >= c and k >= a:
            n -= c
            k -= a
        return [n,k]
    if c > a:
        nc = c%a
        t = c//a
        # a*n-b = k*(nc+t*a)
        # (n-k*t)*a-b = k*nc
        temp = getnk(a,b,nc)
        n = temp[0]
        k = temp[1]
        n += t*k
        while n >= c and k >= a:
            n -= c
            k -= a
        return [n,k]

# 78498 prime under 1000000
total = 0
for i in range(2,78498):
    total += fS(i)

print(total)

print("time:",time.time()-t1)  


    
