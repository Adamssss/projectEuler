import math
import time

t1 = time.time()

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
            j = i
            while j < n:
                p[j] = False
                j += t
        i += 1
    return prime

def factors(number):
    factx = 1
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            factx *= (count+1)
            count = 0
            
        i = i+1
    if number > 1:
        factx *= 2
    return factx

target = 500500
lim = target*100
primeSieve(lim)

coe = []
for i in prime:
    coe.append(i)
    t = 1
    n = int(math.pow(i,math.pow(2,t)))
    while n <= lim:
        coe.append(n)
        t += 1
        n = int(math.pow(i,math.pow(2,t)))

coe.sort()
#print(len(coe))
f = 0
r = 1
for i in coe:
    r = r*i
    f += 1
    r = r%500500507
    if f >= target:
        break

print(r)

print("time:",time.time()-t1)  


    
