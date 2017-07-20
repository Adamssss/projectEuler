import math
import time

t1 = time.time()

N = 2**50

# storage size of count
sc = 2**30

'''
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

primeSieve(math.floor(math.sqrt(N))+500)

def factors(number):
    factx = 0
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            factx += 1
            count = 0
            
        i = i+1
    if number > 1:
        factx  += 1
    return factx
'''
c = [0]*(sc+5)
c[1] = 1

def count(n):
    global c
    if n < sc and c[n] > 0:
        return c[n]
    r = n
    i = 2
    while True:
        t = i*i
        if t > n:
            break
        r -= count(n//t)
        #print(n,t,r)
        i += 1
    if n < sc:
        c[n] = r
    return r


def squarefree(n):
    result = 0
    for i in range(1,n+1):
        result += 1
        for j in prime:
            js = j*j
            if js > i:
                break
            if i%js == 0:
                result -= 1
                break
    return result



print(count(N))

#print(squarefree(N))
'''
for j in range(1,N+1):
    if c[j] > 0:
        print(j,c[j],squarefree(j))
'''        
print("time:",time.time()-t1)  
#684465067343069
#time: 1916.2673552036285

    
