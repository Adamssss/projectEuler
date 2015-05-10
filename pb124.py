import math
import time

t1 = time.time()

N = 100000
exp = N//10

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
            j = i
            while j < n:
                p[j] = False
                j += t
        i += 1
    return prime

def rad(number):
    r = 1
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            r *= prime[i]
            count = 0
            
        i = i+1
    if number > 1:
        r *= int(number)
    return r

def bubbleSort(L):
    l = len(L)
    for i in range(l):
        for j in range(l-i-1):
            if L[j] > L[j+1]:
                temp = L[j+1]
                L[j+1] = L[j]
                L[j] = temp
    return L

primeSieve(N)
Lst = [[0,0]]
for i in range(1,N+1):
    Lst.append([rad(i),i])

Lst = bubbleSort(Lst)

print(Lst[exp][1])

print("time:",time.time()-t1)
# time: 1475.4133920669556


    
