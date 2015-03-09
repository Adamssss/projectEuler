import time

t1 = time.time()


prime = [2,3,5]
primen = 2

while prime[primen] < 10000:
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


number = 600851475143
i = 0
while number > 1:
    p = prime[i]
    if number%p == 0:
        number = number // p
        largestA = p

    i = i+1

print (largestA)

print("time:",time.time()-t1)


                
