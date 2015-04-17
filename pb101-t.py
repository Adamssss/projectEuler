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

# op(1,n) = 1
FIT = []
FIT.append(1)

print(un)

print("time:",time.time()-t1)  


    
