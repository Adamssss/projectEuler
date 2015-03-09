import math
import time

t1 = time.time()

N = 28124

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


# find the abudant numbers
abundant = []
for i in range(1,N):
    if spd(i)>i:
        abundant.append(i)

# 28124/2 = 14062
#print (abundant[3489],abundant[3490])        

#print("time:",time.time()-t1)

total = 0
p = []
for i in range(1,N):
    p.append(True)

l = len(abundant)
for i in range(0,3490):
    for j in range(i,l):
        n = abundant[i]+abundant[j]
        if n < N:
            p[n-1] = False

for i in range(1,N):
    if p[i-1]:
        total += i

print (total)

print("time:",time.time()-t1)    

    
    
    
        

            
