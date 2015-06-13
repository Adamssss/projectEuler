import math
import time

t1 = time.time()

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n*fact(n-1)

def slowS(p):
    temp = 0
    for i in range(1,6):
        t =  fact(p-i)%p
        #print(p,i,t,gst(p,i))
        temp += t
    return temp%p

# with some guesstimate and deduction of the mode
# with the theory of wilson's theorem
# that (p-1)! = p-1 mod p
# (p-2)! = 1 mod p
def gst(p,i):
    if i == 1:
        return p-1
    if i == 2:
        return 1
    if i == 3:
        return (p-1)//2
    if i == 4:
        t = gst(p,3)+1
        while t%3 > 0:
            t += p
        return t//3
    if i == 5:
        t = p - gst(p,4)
        while t%4 > 0:
            t += p
        return t//4

# faster S
# use the conclusion of gst(p,i)
def S(p):
    a = (p-1)//2
    temp = a
    a += 1
    while a%3 > 0:
        a += p
    a = a//3
    temp += a
    a = p-a
    while a%4 > 0:
        a += p
    temp += a//4
    return temp%p

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

primeSieve(int(math.pow(10,8)))

total = 0
for i in range(2,len(prime)):
    t = S(prime[i])
    total += t
    #print(prime[i],t)

print(total)

print("time:",time.time()-t1)  


    
