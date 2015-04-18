import math
import time

t1 = time.time()

# using all the numbers
# the sub pairs cover the exact original set
def exactsub(oset):
    l = len(oset)
    if l == 2:
        return [[[oset[0]],[oset[1]]]]
    result = []
    f = oset[0]
    rest = oset[1:]
    result.append([[f],rest])
    for i in exactsub(rest):
        a = i[0]
        b = i[1]
        result.append([a+[f],b])
        result.append([a,b+[f]])
    return result

def allsub(oset):
    temp = exactsub(oset)
    result = temp[:]
    for i in temp:
        if len(i[0]) > 1:
            result += exactsub(i[0])
        if len(i[1]) > 1:
            result += exactsub(i[1])
    return result

def checksub(setp):
    B = setp[0]
    C = setp[1]
    sb = sum(B)
    sc = sum(C)
    if sb == sc:
        return False
    lb = len(B)
    lc = len(C)
    if lb > lc and sb <= sc:
        return False
    if lb < lc and sb >= sc:
        return False
    return True

def checkset(tset):
    for i in allsub(tset):
        if not checksub(i):
            return False
    return True

def toString(aset):
    temp = 0
    for i in aset:
        dig = math.floor(math.log10(i)+1)
        temp = temp*math.pow(10,dig)+i
    return int(temp)

sset = [[],[1],[1,2],[2,3,4],[3,5,6,7],[6,9,11,12,13],[11,18,19,20,22,25]]

AL = 2

def near(n):
    if n == 1:
        result = []
        for i in range(0,AL*2):
            result.append([i])
        return result
    result = []
    for i in range(0,AL*2):
        for j in near(n-1):
            result.append([i]+j)
    return result

def addaprox(seta,setb):
    result = seta[:]
    for i in range(len(seta)):
        result[i] += setb[i]
    return result

def makeset(n):
    temp = sset[n-1]
    a = temp[n//2-1]
    base = [a]
    for i in range(n-1):
        base.append(temp[i]+a-AL)
    for j in near(n):
        temp = addaprox(base,j)
        if checkset(temp):
            return temp

print(toString(makeset(7)))

print("time:",time.time()-t1)  


    
