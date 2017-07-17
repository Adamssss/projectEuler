import math
import time

t1 = time.time()

cbc = [1,1,1]

N = 50

def bc(n):
    # starting with a black block
    result = cbc[n-1]
    # starting with a red block
    for i in range(3,n+1):
        temp = n-i-1
        if temp >= 0:
            result += cbc[temp]
        else:
            result += 1
    return result

for i in range(3,N+1):
    cbc.append(bc(i))

print(cbc[-1])


        

print("time:",time.time()-t1)  


    
