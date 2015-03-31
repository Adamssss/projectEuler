import math
import time

t1 = time.time()

n = 1000000

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

def isPrime(item):
    root = math.floor(math.sqrt(item))
    i = 0
    while prime[i] <= root:
        if item%prime[i] == 0:
            return False
        i += 1
    return True

# the digit change cases
# the last dig can not be possible to change to satisfy 8 family
# one or two digit at the same time can't be true
# as 3/10 would be the product of 3
# four digit would also be a bad idea
# so it leaves 3 digit at the same time

def changeable(origin):
    if origin < 56003:
        return False
    temp = origin
    dig = []
    while temp > 0:
        dig.append(temp%10)
        temp = temp//10
    ti = False
    test = dig[:]
    test.pop(0)
    for i in range(0,10):
        if test.count(i)>=3:
            thedig = i
            ti = True
    if not ti:
        return ti
    changenumber = 0
    for i in range(1,len(dig)):
        if dig[i] == thedig:
            changenumber += math.pow(10,i)
    strike = 0
    maxium = pow(10,len(dig))
    for i in range(1,10):
        newnum = origin + i*changenumber
        if newnum > maxium:
            strike += 1
        elif not isPrime(newnum):
            strike += 1
        if strike == 3:
            return False
        
    print (origin)
    return True

for i in range(0,len(prime)):
    if changeable(prime[i]):
        break
    
print("time:",time.time()-t1)
    


    
