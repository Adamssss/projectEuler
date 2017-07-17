import math
import time

t1 = time.time()

# n mod 3 1/2
# n mod 2 0
# n mod 5 0
# n mod 7 3/4

N = 150000000

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

total = 0

def check(n):
    if n%3 == 0:
        return False
    i = 3
    p = prime[i]
    while p < n:
        r = n%p
        r = r*r
        for j in [1,3,7,9,13,27]:
            temp = r+j
            if temp%p == 0:
                return False
        if p < prime[-1]:
            i += 1
            p = prime[i]
        else:
            p += 2
    n2 = n*n
    if isPrime(n2+11) or isPrime(n2+17) or isPrime(n2+19) or isPrime(n2+21) or isPrime(n2+23):
        return False
    return True     

for i in range(10,N,10):
    if check(i):
        print(i)
        total += i

print(total)
        
print("time:",time.time()-t1)  
# time: 427.4263880252838

    
