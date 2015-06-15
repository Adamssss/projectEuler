import math
import time

t1 = time.time()

def C(n,k):
    r = 1
    for i in range(k):
        r *= n-i
    for i in range(1,k+1):
        r = r//i
    return r

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

primeSieve(100000)

FS = [0]*1000000

def factorsum(number):
    on = number
    s = 0
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        if number < 1000000 and FS[number] > 0:
            return FS[number]+s
        while(number%prime[i] == 0):
            count=count+1
            number = number // prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            s += count*prime[i]
            count = 0
            
        i = i+1
    if number > 1:
        s += int(number)
    if on < 1000000:
        FS[on] = s
    return s

def fsc(n,k):
    r = 0
    for i in range(k):
        r += factorsum(n-i)
        r -= factorsum(i+1)
    return r

# C(20,15) = C(20,5)
print(fsc(20000000,5000000))

print("time:",time.time()-t1)
# time: 824.9201819896698


    
