import math
import time

t1 = time.time()

N = int(math.pow(10,8))

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

twof = []

def twofactorSieve(n):
    global twof
    tf = [True]*(n+1)
    for i in prime:
        tf[i] = False
    i = 3
    while i <= n:
        if tf[i]:
            twof.append(i)
            j = i
            while j <= n:
                tf[j] = False
                j += i
        i += 1
    return twof

twofactorSieve(N)

print(len(twof))

print("time:",time.time()-t1)  
# time: 246.348867893219

    
