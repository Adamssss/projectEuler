import math
import time

t1 = time.time()

N = 999966663333

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

primeSieve(math.ceil(math.sqrt(N))+ 1000)

r = 0
for i in range(0,len(prime)-1):
    p = prime[i]
    rs = p*p
    if rs > N:
        break
    q = prime[i+1]
    re = q*q
    if re > N+1:
        re = N+1
    t = rs + p
    while True:
        if t >= re:
            break
        if not t% q == 0:
            r += t
            #print(t)
        t += p
    t = rs + q - rs%q
    while True:
        if t >= re:
            break
        if not t%p == 0:
            r += t
            #print(t)
        t += q
        
print(r)

print("time:",time.time()-t1)



    
