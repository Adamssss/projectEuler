import math
import time

t1 = time.time()

N = 120000

# gcd(a,c) = 1
# b = c-a   a < c/2
# rad(abc) = rad(a)*rad(b)*rad(c) < c

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

primeSieve(int(math.sqrt(N))+30)

def rad(number):
    r = 1
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number)) 
        if count > 0:
            r *= prime[i]
            count = 0 
        i = i+1
    if number > 1:
        r *= int(number)
    return r

rd = [0,1]
for i in range(2,N):
    rd.append(rad(i))

# b > a >= 1
# rad(b) >= 2

total = 0

for c in range(3,N):
    rc = rd[c]
    if 2*rc >= c:
        continue
    for a in range(1,(c+1)//2):
        if gcd(a,c) > 1:
            continue
        b = c-a
        if rd[b]*rd[a]*rc < c:
            total += c

print(total)    

print("time:",time.time()-t1)  
# time: 1607.5969467859639

    
