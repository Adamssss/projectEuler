import math
import time

t1 = time.time()

prime = [2,3,5]
primen = 2

while prime[primen] < 1000000:
    b = prime[primen]
    t = 1
    while (t == 1):
        b = b+2
        i = 0
        t = 0
        while (prime[i]*prime[i] < b)and (t == 0):
            i=i+1
            if (b%prime[i] == 0):
                t = 1
               
        if (t == 0):
            primen += 1
            prime.append(b)


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
    


    
