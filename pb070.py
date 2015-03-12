import math
import time

t1 = time.time()

prime = [2,3]
b = 3

while True:

    if b > 3400:
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

# wikipedia phi function

ps = [0,1]

# phi(m*n) = phi(m)*phi(n) if gcd(m,n) == 1
# prime phi(p) = p-1
def phi(number):
    root = math.floor(math.sqrt(number))
    result = 1
    i = 0
    t = prime[i]
    while t <= root:
        count = 0
        while number%t == 0:
            count += 1
            number = number//t
        if count > 1:
            result *= int(math.pow(t,count-1))
        if count > 0:
            result *= ps[t]
            return result*ps[number]
        i += 1
        t = prime[i]
    return (number-1)

def isPermutation(a,b):
    na = []
    while a > 0:
        na.append(a%10)
        a = a//10
    nb = []
    while b > 0:
        nb.append(b%10)
        b = b//10
    if len(na) != len(nb):
        return False
    for i in nb:
        if i in na:
            na.remove(i)
        else:
            return False
    return True

pps = []
for i in range(2,10000001):
    temp = phi(i)
    ps.append(temp)
    if isPermutation(temp,i):
        pps.append(i)

mimn = 999999
mimr = 99
for i in pps:
    r = i/ps[i]
    if r < mimr:
        mimr = r
        mimn = i

print(mimn)
              
print("time:",time.time()-t1)
                
