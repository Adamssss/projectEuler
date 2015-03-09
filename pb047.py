import math
import time

t1 = time.time()

N = 200000

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
        
    if b > N:
        break


# the distinct factors
def factors(number):
    factx = 0
    i = 0
    count = 0
    while number >1:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
            
        if count > 0:
            factx += 1
            count = 0
            
        i = i+1

    return factx


# consective numbers to have the exact factors
def consect(num,fac):
    for i in range(0,fac):
        if factors(num+i) != fac:
            return False
    return True

for i in range(1,N):
    if consect(i,4):
        print (i)
        break

print("time:",time.time()-t1)
