import math
import time

t1 = time.time()

N = 20000

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

# for prime p >= 7
# according to Fermat's lttle theorem
# a^(p-1)-1  = 0 mod p
# (10^(p-1)-1)/9 = R(p-1)   A(p) <= p-1

# for prime p > 5   p-1 = k*A(p)
# for composite p^j
# A(p^j) = p^(j-1)*A(p)
# p-1 = -1 mod p
# p^(j-1) = 0 mod p
# so composite value can not be p^j

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

def gcd(x,y):
    if x < y:
        temp = x
        x = y
        y = temp
    while y > 0:
        temp = x%y
        x = y
        y = temp

    return x

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

# a method to isolate one prime factor out
# and then calculate the A value
# use cA to record the calculated value of A
cA = [0]*(N+1)
cA[1] = 1
cA[2] = 0
cA[3] = 3

def isoA(n):
    global cA
    on = n
    if n%2 == 0 or n%5 == 0:
        cA[n] = 0
        return False
    if n%3 == 0:
        n = n//3
        count = 1
        while n%3 == 0:
            n = n//3
            count += 1
        a = int(math.pow(3,count))
        b = cA[int(n)]
        cA[on] = a*b//gcd(a,b)
        return False
    nr = math.floor(math.sqrt(n))
    i = 3
    count = 0
    while prime[i] <= nr:
        while(n%prime[i] == 0):
            count=count+1
            n = n // prime[i]
        if count > 0:
            a = int(cA[prime[i]]*math.pow(prime[i],count-1))
            b = cA[int(n)]
            temp = a*b//gcd(a,b)
            cA[on] = temp
            return (on-1)%temp == 0
        i = i+1
    if n > 1:
        cA[on] = pA(n)
        return False

cv = []

for i in range(7,N):
    if isoA(i):
        cv.append(i)
        #print(i,cA[i])
    if len(cv) == 25:
        break

print(sum(cv))

print("time:",time.time()-t1)


    
