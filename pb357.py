import math
import time

t1 = time.time()

N = 100000000

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

primeSieve(N)

def factorset(number):
    originNumber = number
    result = [1]
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    p = 2
    while p <= nr:
        while(number%p == 0):
            count=count+1
            number = number / p
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            nrt = result[:]
            l = len(nrt)
            for k in range(count):
                for j in range(l):
                    nrt[j] *= p
                result += nrt[:]
            count = 0
            
        i = i+1
        p = prime[i]
    if number > 1:
        n = int(number)
        nrt = result[:]
        for j in range(len(nrt)):
            nrt[j] *= n
        result += nrt
    return result

def isPrime(item):
    root = math.floor(math.sqrt(item))
    i = 0
    t = prime[i]
    while t <= root:
        if item%t == 0:
            return False
        if t < prime[-1]:
            i += 1
            t = prime[i]
        else:
            t += 2
    return True

def satisfy(n):
    temp = factorset(n)
    for i in range(len(temp)):
        d = temp[i]
        if not isPrime(d+n//d):
            return False
    return True

total = 1
l = len(prime)
i = 1
while i < l:
    n = prime[i]-1
    if satisfy(n):
        total += n
    i += 1

print(total)

print("time:",time.time()-t1)  


    
