import math
import time

t1 = time.time()

prime = [2,3]
total = 5

while True:
    b = prime[-1]

    
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
        
    if b > 10000:
        break

# to find out the sum of the proper divsor
def spd(number):
    originNumber = number
    spd = 1
    i = 0
    count = 0
    while number > 1:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
            
        if count > 0:
            spdtemp = (math.pow(prime[i],count+1)-1)//(prime[i]-1)
                            
            spd *= spdtemp
            count = 0
            
        i = i+1

    return spd - originNumber


totalspd = 0
for i in range(2,10000):
    temp = spd(i)
    if temp > 10000:
        continue
    if temp == i:
        continue
    if spd(temp) == i:
        totalspd += i

print (totalspd)

print("time:",time.time()-t1)

    
    
    
        

            
