import math
import time

t1 = time.time()

temp = [0]*100
temp[2] = 2
temp[3] = 4
temp[4] = 8

def threetile(n):
    if n < 2:
        return 1
    if temp[n] > 0:
        return temp[n]
    # starting with a black block
    result = threetile(n-1)
    # starting with a red block
    result += threetile(n-2)
    # starting with a green block
    result += threetile(n-3)
    # starting with a blue block
    result += threetile(n-4)
    temp[n] = result
    return result

print(threetile(50))

print("time:",time.time()-t1)  


    
