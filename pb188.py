import math
import time

t1 = time.time()

N = int(math.pow(10,8))

# 1777^1250000 % 10^8 = 1
# thus 1777^(10^8) % 10^8 = 1

r = 1777
c = 1
while r > 1:
    r = r*1777
    r = r%N
    c += 1
    
#print(c)

t = 1
for i in range(1855):
    t = pow(1777,t,N)

print(t)

print("time:",time.time()-t1)  


    
