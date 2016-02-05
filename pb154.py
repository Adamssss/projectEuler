import math
import time

t1 = time.time()

N = 200000
exp = 12

# calculate how many 5 and 2 factors each number contains and record them
ct = [0]*(N+1)
cf = [0]*(N+1)

for i in range(2,N+1):
    num = i
    temp = 0
    while num > 1:
        num = num//2
        temp += num
    ct[i] = temp
    num = i
    temp = 0
    while num > 1:
        num = num//5
        temp += num
    cf[i] = temp
    #print(i,ct[i],cf[i])

# the order of k and l doesn't matter
def cct(n,k,l,m):
    coot = ct[n]-ct[k]-ct[m]-ct[l]
    coof = cf[n]-cf[k]-cf[m]-cf[l]
    if coot >= exp and coof >= exp:
        return True
    return False

count = 0
# i <= j <= k
# i,j,k can be in any order
for i in range(N//3+1):
    k = N-i-i
    if cct(N,i,i,k):
        if k == i:
            count += 1
        else:
            count += 3
    for j in range(i+1,(N-i)//2+1):
        k = N-i-j
        if cct(N,i,j,k):
            if k == j:
                count += 3
            else:
                count += 6

print(count)
       
print("time:",time.time()-t1)
# time: 7120.084245920181
                
