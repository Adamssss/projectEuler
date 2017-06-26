import math
import time

t1 = time.time()


N = 1000000


# mdrs(a*b) >= mdrs(a)+mdrs(b)

def dr(n):
    r = 0
    while n > 0:
        r += n%10
        n = n//10
    if r < 10:
        return r
    return dr(r)
        

mdrs = [0]*1000000

mdrs[1] = 1
mdrs[2] = 2
mdrs[3] = 3

for i in range(4,N):
    mdrs[i] = dr(i)
    for j in range(2,math.floor(math.sqrt(i))+1):
        if i%j == 0:
            m = mdrs[i//j]+mdrs[j]
            if m > mdrs[i]:
                mdrs[i] = m


s = 0
for i in range(2,N):
    t = mdrs[i]
    #print(i,t)
    s += t
    

print(s)

print("time:",time.time()-t1)  


    
