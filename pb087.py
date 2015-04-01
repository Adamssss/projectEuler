import math
import time

t1 = time.time()

N = 50000000

n = math.floor(math.sqrt(N))

p = [True]*(n)

i = 1
prime = [2]

while i < n:
    if p[i]:
        t = 2*i+1
        prime.append(t)
        j = i
        while j < n:
            p[j] = False
            j += t
    i += 1

count = 0

ppt = [False]*(N)

i1 = 0
a = prime[i1]*prime[i1]
temp = a
while temp < N:
    i2 = 0
    b = prime[i2]*prime[i2]*prime[i2]
    temp = a+b
    while temp < N:
        i3 = 0 
        c = prime[i3]*prime[i3]*prime[i3]*prime[i3]
        temp = a+b+c
        while temp < N:
            if temp < N and not ppt[temp-1]:
                ppt[temp-1] = True
                count += 1
                #print(temp)
            i3 += 1
            c = prime[i3]*prime[i3]*prime[i3]*prime[i3]
            temp = a+b+c
        i2 += 1
        b = prime[i2]*prime[i2]*prime[i2]
        temp = a+b
    i1 += 1
    a = prime[i1]*prime[i1]
    temp = a
        
print(count)
    
print("time:",time.time()-t1)
    


    
