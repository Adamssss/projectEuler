import math
import time

t1 = time.time()

N = 64000000

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

primeSieve(math.floor(math.sqrt(N))+20)

def pds(number):
    originNumber = number
    r = [1]
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        rt = []
        lrt = 1
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
            lrt = lrt*prime[i]
            rt.append(lrt)
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            rtemp = []
            for j in rt:
                for k in r:
                    rtemp.append(j*k)
            r = r+rtemp
            count = 0
            
        i = i+1

    if number > 1:
        lrt = int(number)
        rtemp = []
        for j in r:
            rtemp.append(j*lrt)
        return r+rtemp

    return r

def xt(n):
    r = 0
    for i in pds(n):
        r += i*i
    return r

total = 0
for i in range(1,N):
    t = xt(i)
    tt = math.sqrt(t)
    if round(tt) == tt:
        total += i
        #print(i,t,tt,math.sqrt(i),pds(i))

print(total)

print("time:",time.time()-t1)
# time: 11551.987301111221


    
