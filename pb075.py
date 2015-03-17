import math
import time

t1 = time.time()

# Euclid's formula

# m-n is odd
# gcd(m,n)=1
# a = m^2-n^2, b = 2mn, c = m^2+n^2

N = 1500000

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

t = [0]*(N+1)

root = math.floor(math.sqrt(N/2))

for i in range(2,root+1):
    for j in range(1,i):
        if (i+j)%2 == 0:
            continue
        if gcd(i,j) > 1:
            continue
        #a = i*i-j*j
        #b = 2*i*j
        #c = i*i+j*j
        s = 2*i*(i+j)
        p = s
        while p <= N:
            t[p] += 1
            p += s


total = 0
for i in range(0,N+1):
    if t[i] == 1:
        total += 1

print(total)

print("time:",time.time()-t1)

