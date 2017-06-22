import math
import time

t1 = time.time()

# X(1,2,3) = 0
# X(0,0,1) = 1
# X(0,1,1) = 0
# X(1,1,2) = 1

# Wikipedia Nim-sum
def ns(a,b,c):
    return a^b^c

count = 0
for i in range(1,int(math.pow(2,30))+1):
    if ns(i,2*i,3*i) == 0:
        count += 1

print(count)

print("time:",time.time()-t1)  


    
