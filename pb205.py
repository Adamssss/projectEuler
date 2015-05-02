import math
import time

t1 = time.time()

def dices(n,f):
    if n == 1:
        temp = []
        for i in range(1,f+1):
            temp.append([i])
        return temp
    result = []
    for j in range(1,f+1):
        for i in dices(n-1,f):
            result.append([j]+i)
    return result

four = [0]*37
six = [0]*37

for i in dices(6,6):
    six[sum(i)] += 1

for i in dices(9,4):
    four[sum(i)] += 1

t = 0
for i in range(6,37):
    for j in range(i+1,37):
        t += six[i]*four[j]

print(t/math.pow(4,9)/math.pow(6,6))

print("time:",time.time()-t1)
    


    
