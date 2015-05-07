import math
import time

t1 = time.time()

def digt(num):
    n = num
    digt = 0
    while n > 0:
        digt += n%10
        n = n//10
    return digt

temp = []

for i in range(2,200):
    for j in range(2,50-i//10):
        t = round(math.pow(i,j))
        if digt(t) == i:
            temp.append(t)

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

temp = quickSort(temp,0,len(temp)-1)

i = 0
l = temp[0]
n = 1

while n < 30:
    i += 1
    if l != temp[i]:
        l = temp[i]
        n += 1

print(temp[i])

print("time:",time.time()-t1)  


    
