import math
import time

t1 = time.time()

# un = 1-n+n2-n3+n4-n5+n6-n7+n8-n9+n10

un = []
for i in range(1,12):
    temp = 1
    for j in range(1,11):
        temp += math.pow(-1,j)*math.pow(i,j)
    un.append(int(temp))

# the k op simulation is the kth derivative
# for 1,8,27
# the first derivative is 7,19
# the second derivative is 12
# FIT[0] = 1
# FIT[1] = 15 = 8+7
# FIT[2] = 58 = 27+19+12

d = []
d.append(un)
for i in range(1,10):
    temp = []
    for j in range(0,10-i):
        temp.append(d[i-1][j+1]-d[i-1][j])
    d.append(temp[:])

def fit(n):
    total = 0
    for i in range(n+1):
        total += d[i][n-i]
    return total

total = 0
for i in range(10):
    total += fit(i)

print(total)

print("time:",time.time()-t1)  


    
