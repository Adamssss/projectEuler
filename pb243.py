import math
import time

t1 = time.time()

N = 1000

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

def factorx(number):
    factx = []
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            factx.append(prime[i])
            count = 0
        i = i+1
    if number > 1:
        factx.append(int(number))
    return factx

def R(d):
    temp = [True]*(d+1)
    for i in factorx(d):
        j = i
        while j < d:
            temp[j] = False
            j += i
    count = 0
    for i in range(1,d):
        if temp[i]:
            count += 1
    return count/(d-1)

# R(d) = phi(d)/(d-1)
# from projecteuler problem 69
ps = [0,1]

# phi(m*n) = phi(m)*phi(n) if gcd(m,n) == 1
# prime phi(p) = p-1
def phi(number):
    result = 1
    i = 0
    t = prime[i]
    nr = math.floor(math.sqrt(number))
    while t <= nr:
        count = 0
        while number%t == 0:
            count += 1
            number = number//t
        nr = math.floor(math.sqrt(number))
        if count > 1:
            result *= int(math.pow(t,count-1))
        if count > 0:
            result *= ps[t]
        i += 1
        t = prime[i]
    if number > 1:
        result *=(int(number)-1)
    return result

for i in range(2,N):
    temp = phi(i)
    ps.append(temp)

def phiR(d):
    return phi(d)/(d-1)

lim = 15499/94744

i = 1
test = 2
while True:
    test *= prime[i]
    i += 1
    if phiR(test) < lim:
        break

m = prime[i-1]
test = test//m

for j in range(2,m+1):
    temp = test*j
    if phiR(temp) < lim:
        print(temp)
        break

print("time:",time.time()-t1)  


    
