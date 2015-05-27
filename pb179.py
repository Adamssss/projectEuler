import math
import time

t1 = time.time()

N = int(math.pow(10,7))

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

primeSieve(int(math.sqrt(N))+20)

def factors(number):
    factx = 1
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            factx *= (count+1)
            count = 0
            
        i = i+1
    if number > 1:
        factx *= 2
    return factx

count = 0
last = 2

for i in range(3,N+1):
    temp = factors(i)
    if temp == last:
        count += 1
    last = temp

print(count)    

print("time:",time.time()-t1)  
# time: 651.0113861560822

    
