import math
import time

t1 = time.time()

# k = gcd(a,b)
# a = kp,b = kq
# 1/a+1/b = (p+q)/p/q/k
# (p+q)/p/q/k*10^n is integer

# p,q,k for 10^1
# 1,1,(1,2,4,5,10,20)
# 1,2,(1,3,5,15)
# 1,5,(1,2,3,4,6,12)
# 1,10,(1,11)
# 2,5,(1,7)

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

primeSieve(1000000)

def factors(number):
    f = 1
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            f *= count+1
            count = 0
            
        i = i+1

    if number > 1:
        f *= 2
    return f

total = 0
for i in range(1,10):
    l = 10**i
    r = 0
    # 1,1/2/5/10
    for j in range(0,i+1):
        for k in range(0,i+1):
            q = 2**j*5**k
            r += factors((1+q)*l//q)
    # 2,5
    for j in range(1,i+1):
        p = 2**j
        for k in range(1,i+1):
            q = 5**k
            r += factors((p+q)*l//p//q)
    #print(r)
    total += r

print(total)

print("time:",time.time()-t1)  


    
