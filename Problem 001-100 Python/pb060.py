import math
import time

t1 = time.time()

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

primeSieve(10000)

# make two number concatenate
def seq(a,b):
    dig = math.floor(math.log10(b)+1)
    return a*math.pow(10,dig)+b

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

ps = [[3]]

def canadd(tset,num):
    for i in tset:
        if not isPrime(seq(i,num)):
            return False
        if not isPrime(seq(num,i)):
            return False
    return True

def getanswer():
    global ps
    for j in range(3,len(prime)):
        for k in ps:
            if canadd(k,prime[j]):
                ps.append(k+[prime[j]])
                if len(k) == 4:
                    print(sum(ps[-1]))
                    return
        if prime[j] < 20:
            ps.append([prime[j]])

getanswer()

print("time:",time.time()-t1)
