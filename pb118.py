import math
import time

t1 = time.time()

def QPL(mylist):
    if len(mylist) == 1:
        return [mylist]
    qpl = []
    for i in mylist:
        rest = mylist[:]
        rest.remove(i)
        for j in QPL(rest):
            qpl.append([i]+j)
    return qpl

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

primeSieve(round(math.sqrt(987654321)))

count = 0

# t for the number working with
# p for the previous prime
# s for the remaind set
def checkset(s,t,p):
    global count
    if len(s) == 0:
        if t == 0:
            count += 1
        return
    temp = t*10+s[0]
    s = s[1:]
    if isPrime(temp) and temp > p:
        checkset(s,0,temp)
    checkset(s,temp,p)

for i in QPL([1,2,3,4,5,6,7,8,9]):
    checkset(i,0,0)

print(count)


    

print("time:",time.time()-t1)  


    
