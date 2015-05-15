import math
import time

t1 = time.time()

N = 13

def rnivenn(d):
    if d == 1:
        return [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    result = []
    for i in rnivenn(d-1):
        for j in range(10):
            temp = i+[j]
            if harshad(temp):
                result.append(temp)
    return result

def harshad(num):
    dt = sum(num)
    n = tonum(num)
    temp = n/dt
    if temp == int(temp):
        return True
    return False

def tonum(lst):
    result = 0
    for i in lst:
        result = result*10+i
    return result

def isStrong(num):
    n = tonum(num)
    dt = sum(num)
    temp = n//dt
    return isPrime(temp)

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

def isPrime(item):
    if item == 1:
        return False
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

primeSieve(int(math.pow(10,N/2)))

def sumofp(num):
    count = 0
    for i in [1,3,7,9]:
        temp = tonum(num+[i])
        if isPrime(temp):
            #print(temp)
            count += temp
    return count

total = 0
for j in range(1,N+1):
    for i in rnivenn(j):
        if isStrong(i):
            total += sumofp(i)

print(total)


print("time:",time.time()-t1)  


    
