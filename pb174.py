import math
import time

t1 = time.time()

# a^2-b^2
# (a+b)(a-b)
# when a = 2p 
# b = 2q    p > q >= 1
# 4(p-q)(p+q)
# when 2 = 2p+1
# b = 2q+1  p > q >= 0
# 4(p-q)(q+q+1)

N = 1000000

tc = [0]*(N+1)
lim = N//4

# a = 2p, b = 2q
q = 1
while True:
    p = q+1
    if p+q > lim:
        break
    t = (p+q)*(p-q)*4
    while t <= N:
        tc[t] += 1
        p += 1
        t = (p+q)*(p-q)*4
    q += 1

# a = 2p+1, b = 2q+1
q = 0
while True:
    p = q+1
    if p+q+1 > lim:
        break
    t = (p+q+1)*(p-q)*4
    while t <= N:
        tc[t] += 1
        p += 1
        t = (p+q+1)*(p-q)*4
    q += 1

total = 0
for i in range(1,N+1):
    t = tc[i]
    if t >= 1 and t <= 10:
        total += 1

print(total)
        
print("time:",time.time()-t1)  


    
