import math
import time

t1 = time.time()

N = 200

m = [N]*(N+1)
m[1] = 0

tempc = []
nextc = []

# generate a tree
# index 0 is the previous nodes to this node
# index 1 is the value of the node
startcase = [[1],1]
tempc.append(startcase)

# by chose a previous node and add the current value
# to create the next level node
def genc(case):
    global nextc
    global m
    l = len(case[0])
    for i in case[0]:
        t = case[1]+i
        if t <= N and m[t] > l-1:
            m[t] = l
            temp = []
            temp.append(case[0]+[t])
            temp.append(t)
            nextc.append(temp[:])

def gent():
    global tempc
    global nextc
    while len(tempc) > 0:
        case = tempc[0]
        tempc.pop(0)
        genc(case)
    tempc = nextc[:]
    nextc = []
    
for i in range(N):
    gent()
    if len(tempc) == 0:
        break

total = 0
for i in range(1,N+1):
    total += m[i]

print(total)

print("time:",time.time()-t1)  


    
