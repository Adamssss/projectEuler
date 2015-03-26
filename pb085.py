import math
import time

t1 = time.time()

# in a m*n grid
# m*n + (m-1)*n + m*(n-1) + (n-1)*(m-1) + (m-2)*n .....
# (m + m-1 + m-2 +... + 1)*(n + n-1 + ... + 1)


# so recs equals sm*sn
# sm = m*(m+1)//2
# sn = n*(n+1)//2

def issn(num):
    temp = math.floor(math.sqrt(num*2))
    if temp*(temp+1)//2 == num:
        return True
    return False

N = 2000000

# check until sqrt of 2000000
root = math.floor(math.sqrt(N*2))

sm = []
i = 1
while True:
    temp = i*(i+1)//2
    if temp > root:
        break
    sm.append(temp)
    i += 1

def isrecs(num):
    i = 0
    r = math.floor(math.sqrt(num))
    while sm[i] <= r:
        temp = num/sm[i]
        if temp == int(temp):
            if issn(temp):
                return i
        i += 1
    return 0


i = 1
while True:
    temp = isrecs(N+i)
    if temp > 0:
        answer = N+i
        break
    temp = isrecs(N-i)
    if temp > 0:
        answer = N-i
        break
    i += 1

m = temp+1
num = answer/m/(m+1)*2
n = math.floor(math.sqrt(num*2))

print(m*n)

print("time:",time.time()-t1)
    
