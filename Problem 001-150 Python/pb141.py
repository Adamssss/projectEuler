import math
import time

t1 = time.time()

def isSquare(n):
    r = math.sqrt(n)
    return r == int(r)

# a,b,c
# kss,kst,ktt
# s<t
# n = dq+r
# r < d
# kksttt+kss/kksstt+kst
# ks(kttt+s)/kst(kst+1)
# ks(kttt+s) = n = l^2

N = int(math.pow(10,12))

# s >= 1
# t > s
# k >= 1
# k < sqrt(N/8)

pset = []

for k in range(1,math.ceil(math.sqrt(N/8))):
    for t in range(1,math.ceil(math.pow(N/k/k,1/3))):
        for s in range(1,t):
            n = k*s*(k*t*t*t+s)
            if n < N and not n in pset and isSquare(n):
                pset.append(n)
                #print(n,k*s*s,k*s*t,k*t*t)

print(sum(pset))
        
print("time:",time.time()-t1)  


    
