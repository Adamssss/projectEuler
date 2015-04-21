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

def quickSort(L, low, high):
    i = low 
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1                                                             
        L[i] = L[j]
        while i < j and L[i] <= key:    
            i = i+1 
        L[j] = L[i]
    L[i] = key 
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L

def undsub(setp):
    B = setp[0]
    C = setp[1]
    lb = len(B)
    lc = len(C)
    if lb != lc:
        return False
    if lb == 1:
        return False
    count = 0
    copy = quickSort(C[:],0,lc-1)
    for i in range(lb):
        temp = B[i]
        for j in copy:
            if j > temp:
                copy.remove(j)
                count += 1
                break
    if count == lb:
        return False
    count = 0
    copy = quickSort(B[:],0,lb-1)
    for i in range(lc):
        temp = C[i]
        for j in copy:
            if j > temp:
                copy.remove(j)
                count += 1
                break
    if count == lc:
        return False
    return True

def needtocheck(oset):
    countt = 0
    countn = 0
    for i in allsub(oset):
        countt += 1
        if undsub(i):
            countn += 1
    return [countn,countt]

N = 12

temp = []

for i in range(1,N+1):
    temp.append(i)

answer = needtocheck(temp)

print(answer[0])
    

print("time:",time.time()-t1)  


    
