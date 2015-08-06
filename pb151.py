import math
import time
import random

t1 = time.time()

# A1:16
# A2:8
# A3:4
# A4:2
# A5:1
'''
def getRandom(n):
    return random.randint(1,n)

def getbatch(env,l):
    i = getRandom(l)-1
    t = env[i]
    env.pop(i)
    if t == 1:
        return env
    if t == 2:
        return env+[1]
    if t == 4:
        return env+[1,2]
    if t == 8:
        return env+[1,2,4]

def testweek():
    env = [1,2,4,8]
    el = 4
    count = 0
    for i in range(14):
        env = getbatch(env,el)
        el = len(env)
        if el == 1:
            count += 1
    return count

N = 600000000

total = 0

for i in range(N):
    total += testweek()

avg = total/N
k = math.pow(10,6)

print(round(avg*k)/k) 
'''

def atone(s):
    if s == [1,0,0,0]:
        return 0
    po = 0
    pb = 0
    for i in range(4):
        if s[i] == 0:
            continue
        pb += s[i]
        t = s[:]
        t[i] -= 1
        for j in range(i):
            t[j] += 1
        pt = atone(t)
        if sum(t) == 1 and t[0] != 1:
            pt += 1
        po += s[i]*pt
    return po/pb

avg = atone([1,1,1,1])
k = math.pow(10,6)

print(round(avg*k)/k)
    
print("time:",time.time()-t1)  


    
