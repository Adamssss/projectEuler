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

count = 0
lim = N//4

# a = 2p, b = 2q
q = 1
while True:
    p = q+1
    if p+q > lim:
        break
    while (p+q)*(p-q) <= lim:
        count += 1
        p += 1
    q += 1

# a = 2p+1, b = 2q+1
q = 0
while True:
    p = q+1
    if p+q+1 > lim:
        break
    while (p+q+1)*(p-q) <= lim:
        count += 1
        p += 1
    q += 1

print(count)  
        
print("time:",time.time()-t1)  


    
