import math
import time

t1 = time.time()

N = 100000

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

def gennum(dig,num,run):
    if dig == run:
        temp = [num]*run
        return [temp]
    if dig == 1:
        temp = []
        for i in range(10):
            temp.append([i])
        return temp
    if run == 0:
        result = []
        for i in gennum(dig-1,num,run):
            for j in range(10):
                result.append([j]+i)
        return result
    result = []
    for i in gennum(dig-1,num,run-1):
        result.append([num]+i)
    for i in gennum(dig-1,num,run):
        for j in range(10):
            result.append([j]+i)
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

def tonum(lst):
    if lst[0] == 0:
        return 4
    result = 0
    for i in lst:
        result = result*10+i
    return result

def pb(digs,num):
    run = digs
    while True:
        test = gennum(digs,num,run)
        result = []
        for i in test:
            temp = tonum(i)
            if isPrime(temp):
                result.append(temp)
        if len(result) > 0:
            return result
        run -= 1

def S(digs,num):
    return sum(pb(digs,num))

primeSieve(N)
total = 0

for i in range(10):
    total += S(10,i)

print(total)

print("time:",time.time()-t1)  


    
