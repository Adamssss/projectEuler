import math
import time

t1 = time.time()

prime = [2,3]
b = 3

while True:

    
    while True:
        b = b+2
        i = 0
        t = True
        while (prime[i]*prime[i] < b):
            i=i+1
            if (b%prime[i] == 0):
                t = False
                break
                
        if t:
            prime.append(b)
            break
        
    if b > 1000:
        break

def isPrime(item):
    root = math.floor(math.sqrt(item))
    i = 0
    t = prime[i]
    while t <= root:
        if item%t == 0:
            return False
        if t < prime[-1]:
            i += 1
            t = prime[i]
        else:
            t += 2
    return True

# a[167] is 997 < 1000
# when n = 0 num = n^2+an+b =b
# so b must be a prime
# when n = b num = n^2+an+b = b(b+a+1)
# so the max is restricted by b

coe = []
for i in range(-999,1000):
    coe.append([i,2])
    
# if b is odd then a has to be odd
# for 1+a+b to be a prime
t = -999
while t < 1000:
    for i in range(1,168):
        coe.append([t,prime[i]])
    t += 2

n = 1
while len(coe) > 1:

    # print (len(coe))
    
    i = 0
    while i < len(coe):
        a = coe[i][0]
        b = coe[i][1]
        num = (n*n+n*a+b)
        if num > 0 and isPrime(num):
            i += 1
        else:
            coe.pop(i)

    n += 1

print(coe[0][0]*coe[0][1])     

print("time:",time.time()-t1)
