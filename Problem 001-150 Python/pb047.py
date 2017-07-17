import math
import time

t1 = time.time()

N = 200000

n = math.floor(math.sqrt(N))+1

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


# the distinct factors
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
            factx += 1
            count = 0
            
        i = i+1
    if number == 1:
        factx -= 1
    return factx


# consective numbers to have the exact factors
def consect(num,fac):
    for i in range(0,fac):
        if factors(num+i) != fac:
            return False
    return True

for i in range(1,N):
    if consect(i,4):
        print (i)
        break

print("time:",time.time()-t1)
