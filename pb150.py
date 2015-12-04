import math
import time

t1 = time.time()

size = 1000


sizet = size*(size+1)//2

s = [0]*(sizet+1)

a19 = int(math.pow(2,19))
a20 = 2*a19

t = 0
for k in range(1,500501):
    t = (615949*t+797807)%a20
    s[k] = t-a19
'''
# test case
s = [0,15,-14,-7,20,-13,-5,-3,8,23,-26,1,-4,-5,-18,5,-16,31,2,9,28,3]
'''
sst = [0]*(sizet+1)

def getrc(n):
    r = round(math.sqrt(n*2))
    c = n-r*(r-1)//2
    return [r,c]

def ton(r,c):
    return r*(r-1)//2+c

def getsst(n,er):
    rc = getrc(n)
    if rc[0] == er:
        return s[n]
    if rc[0] == er-1:
        return s[n]+sst[ton(rc[0]+1,rc[1])]+sst[ton(rc[0]+1,rc[1]+1)]
    return s[n]+sst[ton(rc[0]+1,rc[1])]+sst[ton(rc[0]+1,rc[1]+1)]-sst[ton(rc[0]+2,rc[1]+1)]

def getser(er):
    ker = er*(er+1)//2
    for k in range(ker,0,-1):
        sst[k] = getsst(k,er)
    
    smallest = 999999999
    for k in range(1,ker+1):
        if sst[k] < smallest:
            smallest = sst[k]
    #print(sst[:ker+1])
    return smallest

sm = 99999999
for i in range(size,0,-1):
    t = getser(i)
    if sm > t:
        sm = t
        
print(sm)

print("time:",time.time()-t1)  
# time: 570.1156089305878

    
