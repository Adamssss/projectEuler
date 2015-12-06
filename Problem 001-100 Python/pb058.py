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

primeSieve(10000)

def genPrime():
    global prime
    b = prime[-1]
    while True:
        b = b+2
        i = 0
        t = True
        while (prime[i]*prime[i] < b):
            i=i+1
            if (b%prime[i] == 0):
                t = False
                break
        if t:
            prime.append(b)
            break
    return b

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
            t += genPrime()
    return True

# diagonal prime ratio
dpr = []
# first term: 1 is not a prime
dpr.append([0,1])

# generate the new diagonals
# put them into dpr
def gen(n):
    s = 2*n+1
    
    br = s*s
    bl = br-s+1
    tl = bl-s+1
    tr = tl-s+1

    global dpr
    tempdpr = dpr[n-1][:]
    tempdpr[1] += 4
    if isPrime(bl):
        tempdpr[0] += 1
    if isPrime(tl):
        tempdpr[0] += 1
    if isPrime(tr):
        tempdpr[0] += 1

    dpr.append(tempdpr)

def fallBelow(term):
    if term[0]/term[1] < 0.1:
        return True
    return False

gen(1)
i = 1

while not fallBelow(dpr[i]):
    i += 1
    gen(i)

print (i*2+1)

print("time:",time.time()-t1)
