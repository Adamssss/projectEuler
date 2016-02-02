import math
import time
import random

t1 = time.time()

# repunit in base a
# n = 1+a+a^2+...a^k
# n = (a^(k+1)-1)/(a-1)

# all number n is 11 in base n-1

N = 1000000000000

r = [1]

for b in range(2,math.ceil(math.sqrt(N))):
    t = b*b+b+1
    while t <= N:
        r.append(t)
        t = t*b+1

total = 0
r.sort()
for i in range(len(r)-1):
    if r[i] != r[i+1]:
        total += r[i]

total +=r[-1]
print(total)

print("time:",time.time()-t1)  


    
