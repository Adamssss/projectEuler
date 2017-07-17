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

# a-1  = -1 mod a
# a+1  = 1 mod a

# r = (a-1)^n+(a+1)^n
# when n is odd
# = na-1+na+1   mod a^2 (binary series)
# = 2*n*a
# when n is even
# = -na+1+na+1
# = 2   mod a^2

# even n remainder is way too small
# for n is odd
def remainder(p,n):
    return (n*2%p)*p

primeSieve(1000000)
limit = int(math.pow(10,10))

i = 1
while True:
    temp = remainder(prime[i-1],i)
    if temp > limit:
        print(i)
        break
    i += 2

print("time:",time.time()-t1)  


    
