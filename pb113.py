import math
import time

t1 = time.time()

N = 100

# increasing numbers
# terms i stands for start with i
# it[n] stands for below 10 to the nth
# it[1][1] = 1 means below 10 start with 1 
it = [[]]
it.append([0,1,1,1,1,1,1,1,1,1])

def increto(n):
    temp = it[n-1]
    result = [0,0,0,0,0,0,0,0,0,0]
    for i in range(1,10):
        result[i] += sum(temp[i:])
    return result

# decreasing numbers
# terms i stands for end with i
dt = [[]]
dt.append([0,1,1,1,1,1,1,1,1,1])

def decreto(n):
    temp = dt[n-1]
    result = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        result[i] += sum(temp[i:])
    return result

total = sum(it[-1])+sum(dt[-1])
for i in range(2,N+1):
    it.append(increto(i))
    dt.append(decreto(i))
    total += sum(it[-1])+sum(dt[-1])
    
# the numbers with exactly the same digits
total -= 9*N

print(total)     
    
print("time:",time.time()-t1)  


    
