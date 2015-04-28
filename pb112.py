import math
import time

t1 = time.time()

N = 10000000

def bouncy(n):
    incre = True
    decre = True
    l = n%10
    n = n//10
    while n > 0:
        t = n%10
        n = n//10
        if incre and l < t:
            incre = False
        if decre and l > t:
            decre = False
        if not (incre or decre):
            return True
        l = t
    return False

cb = 0
ct = 0

for i in range(1,N+1):
    if bouncy(i):
        cb += 1
    ct += 1
    if cb/ct >= 0.99:
        break

print(ct)
        
    

print("time:",time.time()-t1)  


    
