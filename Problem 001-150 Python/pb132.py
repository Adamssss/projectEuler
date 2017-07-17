import math
import time

t1 = time.time()

N = 1000000

def A(n):
    if n%2 == 0 or n%5 == 0:
        return 0
    count = 1
    r = 1
    while r != 0:
        while n > r:
            r = r*10+1
            count += 1
        r = r%n
    return count

# for i and k that gcd(i,k) == 1
# A(i*k) = lcm(A(i),A(k))
# for i^j
# A(i^j) = A(i)*i^(j-1)

# R(10) have factors R(2),R(5),R(10)

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

def pA(p):
    count = 1
    r = 1
    while r != 0:
        while p > r:
            r = r*10+1
            count += 1
        if count > p/2:
            return p-1
        r = r%p
    return count

def testR(k,p):
    # test if R(k)%p == 0
    r = 1
    k = k-1
    while k > 0:
        while r < p and k > 0:
            r = r*10+1
            k = k-1
        r = r%p
    return r == 0

def factorset(number):
    originNumber = number
    rs = [1]
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            ind = prime[i]
            ns = []
            for j in range(count):
                ns.append(ind)
                ind *= prime[i]
            nrs = rs[:]
            for a in rs:
                for b in ns:
                    nrs.append(a*b)
            count = 0
            rs = nrs[:]
            
        i = i+1

    if number > 1:
        nrs = rs[:]
        b = int(number)
        for a in rs:
            nrs.append(a*b)
        rs = nrs[:]

    return sorted(rs)

def tpA(p):
    f = p-1
    for i in factorset(f):
        if testR(i,p):
            return i

def testAf25(p,k):
    f = p-1
    rs = [1]
    f2 = 0
    while f%2 == 0:
        f = f//2
        f2 += 1
    t = 1
    for i in range(min(f2,k)):
        t *= 2
        rs.append(t)
    f5 = 0
    while f%5 == 0:
        f = f//5
        f5 += 1
    nrs = rs[:]
    for i in rs:
        t = i
        for j in range(min(f5,k)):
            t *= 5
            nrs.append(t)
    for i in nrs:
        if testR(i,p):
            return i
    return 0
    
# 11*41*271*9091

count = 0
total = 0
for i in range(4,len(prime)):
    # print(prime[i])
    temp = testAf25(prime[i],9)
    if temp > 0:
        total += prime[i]
        count += 1
        #print(prime[i],temp)
    if count == 40:
        print(total)
        break 

print("time:",time.time()-t1)


    
