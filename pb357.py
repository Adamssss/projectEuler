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
            p[i] = False
            j = 2*i*i+2*i
            while j < n:
                p[j] = False
                j += t
        i += 1
    return prime

primeSieve(N)

# greatly conbimed method 3.5
# improved to be most efficient
def satisfy(number):
    origin = number
    result = []
    i = 0
    count = 0
    root = math.floor(math.sqrt(number))
    nr = root
    p = 2
    while p <= nr:
        while(number%p == 0):
            count=count+1
            number = number / p
        nr = math.floor(math.sqrt(number))

        t = p
        while count > 0:
            if not test(origin,t):
                return False
            tr = []
            for j in result:
                tjt = j*t
                if tjt <= root and not test(origin,tjt):
                    return False
                tr += [tjt]
            tr += [t]
            count -= 1
            t *= p
        result += tr
            
        i = i+1
        p = prime[i]
    if number > 1:
        n = int(number)
        if not test(origin,n):
            return False
        for j in result:
            tn = j*n
            if tn <= root and not test(origin,tn):
                return False
    return True

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

def test(n,d):
    return isPrime(d+n//d)

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
# time: 196.90803408622742
