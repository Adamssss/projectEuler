import math
import time

t1 = time.time()

size = 2000


sizet = size*size

s = [0]*sizet

for k in range(1,56):
    s[k-1] = (100003-200003*k+300007*k*k*k)%1000000-500000

for k in range(56,4000001):
    s[k-1] = (s[k-1-24]+s[k-1-55]+1000000)%1000000-500000

#print(s[10-1],s[100-1])


'''
# test case
s = [-2,5,3,2,9,-6,5,1,3,2,7,3,-1,8,-4,8]
'''
def getrc(n):
    return [n//size,n%size]

def ton(r,c):
    return r*size+c

# 1-dimension solution
def getla(tset):
    maxSoFar = 0
    maxToHere = 0
    for i in tset:
        maxToHere = max(maxToHere+i,0)
        maxSoFar = max(maxToHere,maxSoFar)
    return maxSoFar

la = 0

for i in range(size):
    maxSoFar = 0
    maxToHere = 0
    for j in range(size):
        maxToHere = max(maxToHere+s[ton(i,j)],0)
        maxSoFar = max(maxToHere,maxSoFar)
    if maxSoFar > la:
        la = maxSoFar

for j in range(size):
    maxSoFar = 0
    maxToHere = 0
    for i in range(size):
        maxToHere = max(maxToHere+s[ton(i,j)],0)
        maxSoFar = max(maxToHere,maxSoFar)
    if maxSoFar > la:
        la = maxSoFar

for i in range(size):
    maxSoFar = 0
    maxToHere = 0
    for j in range(i+1):
        maxToHere = max(maxToHere+s[ton(i-j,j)],0)
        maxSoFar = max(maxToHere,maxSoFar)
    if maxSoFar > la:
        la = maxSoFar

for i in range(1,size):
    maxSoFar = 0
    maxToHere = 0
    for j in range(size-i):
        maxToHere = max(maxToHere+s[ton(size-1-j,i+j)],0)
        maxSoFar = max(maxToHere,maxSoFar)
    if maxSoFar > la:
        la = maxSoFar

for i in range(size):
    maxSoFar = 0
    maxToHere = 0
    for j in range(size-i):
        maxToHere = max(maxToHere+s[ton(j,i+j)],0)
        maxSoFar = max(maxToHere,maxSoFar)
    if maxSoFar > la:
        la = maxSoFar

for i in range(1,size):
    maxSoFar = 0
    maxToHere = 0
    for j in range(size-i):
        maxToHere = max(maxToHere+s[ton(i+j,j)],0)
        maxSoFar = max(maxToHere,maxSoFar)
    if maxSoFar > la:
        la = maxSoFar

print(la)

print("time:",time.time()-t1)  


    
