import math
import time

t1 = time.time()

# generate prime with s seive

N = 1000000

n = (N+1)//2

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

print(len(prime))

print("time:",time.time()-t1)
