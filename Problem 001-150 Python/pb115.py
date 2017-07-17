import math
import time

t1 = time.time()

N = 1000000

def cbc(m,n):
    if n < m:
        return 1
    result = cbc(m,n-1)
    for i in range(-1,n-m):
        result += cbc(m,i)
    return result

for i in range(50,500):
    if cbc(50,i) > N:
        print(i)
        break

print("time:",time.time()-t1)  


    
