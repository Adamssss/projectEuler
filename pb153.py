import math
import time

t1 = time.time()

N = 100000000

def gcd(x,y):
    if x < y:
        temp = x
        x = y
        y = temp
    while y > 0:
        temp = x%y
        x = y
        y = temp

    return x

# integer factor
total = N
for i in range(2,N+1):
    t = math.floor(N/i)*i
    total += t

# 1+i factor
a = 1
c = 2
ac = 2
while(ac <= N):
    total += math.floor(N/ac)*2*a
    ac += c
    a += 1


# 1+ni and n+i factor    
ilim = math.floor(math.sqrt(N-1))+1
for i in range(2,ilim):
    c = i*i+1
    ac = c
    ai = i+1
    while(ac <= N):
        total += math.floor(N/ac)*2*ai
        ac += c
        ai += i+1

# others
ilim = math.floor(math.sqrt(N/2))+1
for i in range(2,ilim):
    jlim = math.floor(math.sqrt(N-i*i))+1
    for j in range(i+1,jlim):
        if gcd(j,i) == 1:
            c = i*i+j*j
            ac = c
            aij = i+j
            while (ac <= N):
                total += math.floor(N/ac)*2*aij
                ac += c
                aij += i+j
    
print(total)
       
print("time:",time.time()-t1)
# time: 489.46899604797363
                
