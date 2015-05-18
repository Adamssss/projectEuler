import math
import time

t1 = time.time()

# 0th ring is 1
# 1th ring is 2-7
# 2th ring is 8-19
# 3th ring is 20-37
# 4th ring is 38-61
# nth ring is 2+(n-1)n*3 - 1+n(n+1)*3

# for a at edge of a ring
# a-1 and a+1 is around
# b-1 and b / c-1 and c contains two even number
# the max pd(a) =2
# 1 o'clock edge
# 1,6n-1,6n,6(n+1),12n-7,6n+5
# pd(a): check 6n-1,6n+5,12n-7

# for a at vertex of a ring
# 12 o'clock vertex
# 1,6(n-1),6n,6n-1,6n+1,12n+5
# pd(a): check 6n-1,6n+1,12n+5
# other vertex
# 2/6/10 o'clock contains c-1,c+1,1,1 two even 
# 4/7 o'clock
# inner ring and outer ring contains two even
# and 1,1 max pd(a) = 2

# pd(1) = 3  2,3,5
# pd(2) = 3  5,7,17
# pd(3) = 2
# pd(4) = 2
# pd(5) = 0
# pd(6) = 2
# pd(7) = 2
pd = [1,2]

N = 50000

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

# a >= 8
# n >= 2
for n in range(2,100000):
    if len(pd) >= 2000:
        print(pd[1999])
        break
    if not isPrime(6*n-1):
        continue
    if isPrime(6*n+1) and isPrime(12*n+5):
        pd.append(2+(n-1)*n*3)
    if isPrime(6*n+5) and isPrime(12*n-7):
        pd.append(1+n*(n+1)*3)

print("time:",time.time()-t1)  


    
