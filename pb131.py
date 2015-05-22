import math
import time

t1 = time.time()

# n^3+n^2*p = t^3
# n+p = t^3/n^2
# t = a/b*n
# p = ((a/b)^3-1)n
# if b == 1:
# p = a^3-1 and n = 1
# a = 2, ========>> 1^3+1^2*7 = 2^3
# else:
# n = kb^3
# p = (a^3-b^3)k
# k == 1
# p = (a-b)(aa+ab+bb)
# a = b+1
# p = 3bb+3b+1  <======
# n = b^3       <======
# t = b^3+b^2   <======

# 7 is when b = 1

N = 1000000

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

primeSieve(int(math.sqrt(N))+20)

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

count = 0
b = 1
while True:
    p = 3*b*b+3*b+1
    if p > N:
        break
    if isPrime(p):
        count += 1
    b += 1

print(count)

print("time:",time.time()-t1)  


    
