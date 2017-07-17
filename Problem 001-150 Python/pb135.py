import math
import time

t1 = time.time()

# x^2-y^2-z^2 = n
# (a+2b)^2-(a+b)^2-a^2 = n
# 2ab+3b^2-a^2 = n

N = 1000000

sn = [0]*(N+1)

# a^2-2ab-3b^2 < 0
# a/b < 3
# a/3 < b

a = 1
while True:
    b = a//3 +1
    n = 2*a*b+3*b*b-a*a
    if n > 3*N:
        break
    if n <= N:
        sn[n] += 1
    while True:
        b += 1
        n = 2*a*b+3*b*b-a*a
        if n > N:
            break
        if n <= N:
            sn[n] += 1
    a += 1

count = 0
for i in range(N+1):
    if sn[i] == 10:
        count += 1

print(count)     

print("time:",time.time()-t1)  


    
