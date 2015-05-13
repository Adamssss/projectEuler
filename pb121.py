import math
import time

t1 = time.time()

T = 15

stat = [[0,1],[1,1]]

def turn(n):
    global stat
    t = n+1
    result = []
    result.append([0,stat[0][1]*n])
    for i in range(0,len(stat)-1):
        result.append([stat[i+1][0],stat[i][1]+stat[i+1][1]*n])
    result.append([n,1])
    stat = result


for i in range(2,T+1):
    turn(i)

h = T/2
p = [0,0]
for i in stat:
    if i[0] > h:
        p[0] += i[1]
    else:
        p[1] += i[1]

print(math.floor(p[1]/p[0])+1)
    
print("time:",time.time()-t1)  


    
