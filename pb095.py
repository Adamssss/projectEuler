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

def amichain(lst):
    num = lst[-1]
    l = len(lst)
    if num == 0 or num == 1:
        return 0
    if ami[num] >= 0:
        if l == 1:
            return ami[num]
        else:
            return 0
    nxt = spd(num)
    if nxt > N:
        return 0
    for i in range(0,l):
        if lst[i] == nxt:
            for j in range(i,l):
                ami[lst[j]] = l-i
            if i == 0:
                return l
            else:
                for j in range(0,i):
                    ami[lst[j]] = 0
                return 0
    lst.append(nxt)
    return amichain(lst)

longest = 0
for i in range(0,N+1):
    temp = amichain([i])
    ami[i] = temp
    if temp > longest:
        longest = temp
        result = i

print(result)

print("time:",time.time()-t1)  


    
