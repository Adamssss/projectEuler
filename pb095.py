import math
import time

t1 = time.time()

N = 1000000

ami = [-1] *(N+1)

# prime 
n = math.floor(math.sqrt(N))+1

p = [True]*(n)

i = 1
prime = [2]

while i < n:
    if p[i]:
        t = 2*i+1
        prime.append(t)
        j = i
        while j < n:
            p[j] = False
            j += t
    i += 1

# sum of proper divisor
def spd(num):
    onum = num
    spd = 1
    i = 0
    while prime[i]*prime[i] <= num:
        count = 0
        while num%prime[i] == 0:
            count += 1
            num = num/prime[i]

        if count > 0:
            spdtemp = (math.pow(prime[i],count+1)-1)/(prime[i]-1)
            spd *= spdtemp

        i += 1

    if num > 1:
        spd *= (num+1)

    return int(spd-onum)

longestchain = []
llc = 0

def amichain(num):
    global llc,longestchain
    if ami[num] > 0:
        return ami[num]
    chain = [num]
    count = 1
    temp = num
    while True:
        temp = spd(temp)
        if temp == 1 or temp == 0:
            count = 1
            break
        if temp > N:
            count = 1
            break
        if ami[temp] > count:
            count = 1
            break    
        if temp in chain:
            if temp == chain[0]:
                if len(chain) > llc:
                    longestchain = chain[:]
                    llc = len(chain)
                break
            count = 0
            break
        chain.append(temp)
        count += 1
    for i in chain:
        ami[i] = count

for i in range(0,N+1):
    amichain(i)

smallest = N
for i in longestchain:
    if i < smallest:
        smallest = i
        
print(smallest)

print("time:",time.time()-t1)  


    
