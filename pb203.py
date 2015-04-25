import math
import time

t1 = time.time()

N = 51

pt = [[1]]
for i in range(2,N+1):
    temp = [1]
    for j in range(i//2-1):
        temp.append(pt[i-2][j]+pt[i-2][j+1])
    if i%2 == 1:
        temp.append(2*pt[i-2][-1])
    pt.append(temp)
    
test = []
test.append(1)
for i in pt:
    for j in range(2,len(i)):
        if i[j] >= N and not i[j] in test:
            test.append(i[j])

for i in range(2,N):
    test.append(i)

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

ul = int(math.sqrt(pt[-1][-1]))+30
primeSieve(ul)

def sf(number):
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count += 1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count >= 2:
            return False
        else:
            count = 0            
        i = i+1
    return True

total = 0
for i in test:
    if sf(i):
        #print(i)
        total += i

print(total)

print("time:",time.time()-t1)  


    
