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
            p[i] = False
            j = 2*i*i+2*i
            while j < n:
                p[j] = False
                j += t
        i += 1
    return prime

primeSieve(10**6)

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

# cap at 23
# 2*3*5*~*29=6469693230 > 10**9

def admissible(cap):
    results = [[]]
    t = 1
    while True:
        t *= 2
        if t >= cap:
            break
        results[0].append(t)
    for pi in range(1,10):
        p = prime[pi]
        mpc = cap//(results[-1][0])
        pt = []
        t = 1
        while True:
            t *= p
            if t > mpc:
                break
            pt.append(t)
        if len(pt) == 0:
            break
        results.append([])
        for i in results[-2]:
            for j in pt:
                t = i*j
                if t >= cap:
                    break
                results[-1].append(t)
    return results

def pF(n):
    M = 3
    while True:
        if isPrime(n+M):
            return M
        M += 2

def answer():
    A = admissible(10**9)
    result = []
    for i in A:
        for j in i:
            M = pF(j)
            if not M in result:
                result.append(M)
    return sum(result)


print(answer())

print("time:",time.time()-t1)  





