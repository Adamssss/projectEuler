import math
import time

t1 = time.time()

two = [2,0,0,0,0,0,0,0,0,0]

def double(lst):
    for i in range(0,10):
        lst[i] *= 2
    for i in range(0,10):
        if lst[i] > 9:
            lst[i] -= 10
            if i < 9:
                lst[i+1] += 1
    return lst

def tonumber(lst):
    result = 0
    for i in range(9,-1,-1):
        result = result * 10 + lst[i]
    return result

def power():
    temp = two[:]
    for i in range(1,7830457):
        temp = double(temp)
    return tonumber(temp)

result = power()*28433 +1

result = result %10000000000

print(result)

print("time:",time.time()-t1)  


    
