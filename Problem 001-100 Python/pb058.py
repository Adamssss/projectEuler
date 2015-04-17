import math
import time

t1 = time.time()

# define a method to check if it is a prime
def isPrime(num):
    if num%2 == 0:
        return False
    i = 3
    while i < math.sqrt(num):
        if num%i == 0:
            return False
        i += 2
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
