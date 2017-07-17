import math
import time

t1 = time.time()

# read the sets into a list
f = open('pb105_sets.txt','r')

sets= f.read().split('\n')

f.close()

def tonumber(p):
    number = 0
    for i in range(0,len(p)):
        temp = ord(p[i])-48
        number = number*10 + temp
    return number

def toset(tset):
    result = []
    n = tset.split(',')
    for i in n:
        result.append(tonumber(i))
    return result

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

test = []

for i in sets:
    test.append(toset(i))

total = 0
for i in test:
    if checkset(i):
        total += sum(i)

print(total)

print("time:",time.time()-t1)  


    
