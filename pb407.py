import math
import time

t1 = time.time()


def M(n):
    for a in range(n-1,0,-1):
        if (a*a)%n == a:
            return a
    return 0

# M(1) = 0

# a^2 = kn+a
# a(a-1) = kn (n>a)


# if n = p^q and a > 1, a = p^r , (a-1) != 0 mod p
# n = p^q: a = 1

# if n = 2*p^q and p > 2, a = p^q or a-1 = p^q
# p^q +1 > p^q, a = p^q +1

# if n = p1^q1*p2^q2*p3^q3....
# a or a-1 = k1*p1^q1
# a or a-1 = k2*q2^p2

N = 10**7

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

primeSieve(N+100)

def largestf(number):
    r = 1
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            t = prime[i]**count
            if t > r:
                r = t
            count = 0
            
        i = i+1
    if number > 1:
        t = int(number)
        if t > r:
            r = t
    return r

def nM(n):
    f = largestf(n)
    for a in range(n-f,0,-f):
        if ((a+1)*(a+1))%n == a+1:
            return a +1
        if (a*a)%n == a:
            return a
    return 0
    

Ml = [-1]*(N+1)

for i in prime:
    t = i
    while t <= N:
        Ml[t] = 1
        t = t*i

s = 0
for i in range(2,N+1):
    if Ml[i] >= 0:
        s += Ml[i]
    else:
        #t = M(i)
        t = nM(i)
        s += t

print(s)

print("time:",time.time()-t1)  





