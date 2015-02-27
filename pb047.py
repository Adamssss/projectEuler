import math

prime = [2,3,5]
primen = 2
oddcom = []

N = 200000

while prime[primen] < N:
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
        if t == 1:
            oddcom.append(b)


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
