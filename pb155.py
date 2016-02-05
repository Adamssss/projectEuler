import math
import time
import random

t1 = time.time()

DETS = [[]]*19

DETS[1] = [[1,1]]

def det(n):
    global DETS
    if DETS[n] != []:
        return DETS[n]
    result = []
    for k in range(n//2):
        ti = det(k+1)
        tj = det(n-k-1)
        for i in ti:
            for j in tj:
                t = [i[0]*j[1]+i[1]*j[0],j[1]*i[1]]
                g = gcd(t[0],t[1])
                result.append([t[0]//g,t[1]//g])
                t = [i[0]*j[0],i[1]*j[0]+j[1]*i[0]]
                g = gcd(t[0],t[1])
                result.append([t[0]//g,t[1]//g])
    result = cleanlist(result)
    DETS[n] = result
    return result

def gcd(x,y):
    if x < y:
        temp = x
        x = y
        y = temp
    while y > 0:
        temp = x%y
        x = y
        y = temp
    return x

def cleanlist(L):
    temp = []
    L.sort()
    s = [0,0]
    for i in L:
        if i > s:
            temp.append(i)
        s = i
    return temp

# 4 can form a 1
def dt(n):
    temp = []
    for i in range(max(1,n-4),n+1):
        temp += det(i)
    return cleanlist(temp)

print(len(dt(18)))

print("time:",time.time()-t1)  
# time: 125.42017388343811

    
