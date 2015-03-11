import math
import time

t1 = time.time()

N = 1000000

prime = [2,3]
b = 3
n = math.floor(math.sqrt(N))
while True:

    if b > n:
        break
    
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

def isPrime(item):
    if item == 1:
        return False
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

# the prime dig are 2,3,5,7
# the last can not be 3,7

# the first dig must be 2,3,5,7

# no mid dig can be 0/2/4/6/8 or 5

def isTruncatable(num):
    if not isPrime(num):
        return False
    if num%10 != 3 and num%10 != 7:
        return False
    temp = num
    dig = 1
    lh = 0
    while temp > 9:
        dig += 1
        d = temp%10
        temp = temp//10
        if d==0 or d==2 or d==4 or d==6 or d==8 or d==5:
            return False
        if not isPrime(temp):
            return False
        lh = lh + d*math.pow(10,dig-2)
        if not isPrime(lh):
            return False
        
    #print (num,dig)
    return True

total = 0
for i in range(11,N,2):
    if isTruncatable(i):
        total += i

print(total)

print("time:",time.time()-t1)
