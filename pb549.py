import math
import time

t1 = time.time()

def s(n):
    r = 2
    t = 2
    while t%n != 0:
        r += 1
        t *= r
    return r

def S(n):
    r = 0
    for i in range(2,n+1):
        t = s(i)
        r += t
    return r

def example():
    print(s(10))
    print(s(25))
    print(S(100))

#example()

N = 10**8

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

primeSieve(N+100)

def pfs(number):
    r = 0
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            t = mcf(prime[i],count)
            if t > r:
                r = t
            count = 0
            
        i = i+1
    if number > 1:
        t = int(number)
        if t > r:
            r = t
    return r

def mcf(f,c):
    r = f*c
    while not cf(r,f) < c:
        r -= f
    return r + f

def cf(n,f):
    r = 0
    while n > 0:
        n = n//f
        r += n
    return r

def answer():
    r = 0
    for i in range(2,N+1):
        r += pfs(i)
    return r

print(answer())

print("time:",time.time()-t1)
#476001479068717
#time: 13646.954889059067





