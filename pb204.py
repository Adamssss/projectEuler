import math
import time

t1 = time.time()

# ghc(num,fc) = ghc(num,fc-1)+ghc(num/factor,fc)
# ghc(20,1) = 5     1,2,4,8,16
# ghc(10,1) = 4 = ghc(10,0) + ghc(5,1)
# ghc(20,3) = 14    1,2,3,4,5,6,8,9,10,12,15,16,18,20
# ghc(20,2) = 10    1,2,3,4,6,8,9,12,16,18
# ghc(4,3) = 4      1,2,3,4

N = int(math.pow(10,9))

t = 100

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

primeSieve(t)

def ghc(a,b):
    if b == 1:
        return math.floor(math.log(a,2))+1
    if a <= 3:
        return a
    return ghc(a,b-1)+ghc(a//prime[b-1],b)

print(ghc(N,len(prime)))

print("time:",time.time()-t1)  


    
