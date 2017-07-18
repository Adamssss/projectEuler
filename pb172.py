import math
import time

t1 = time.time()
'''
def count(l,n,c):
    if n == 10:
        return c+1
    for i in range(10):
        if l[i] <= 2:
            nl = l[:]
            nl[i] += 1
            c = count(nl,n+1,c)
    return c

l = [0,0,0,0,0,0,0,0,0,0]
t = 0
for i in range(1,10):
    nl = l[:]
    nl[i] += 1
    t += count(nl,1,0)

print(t)
'''
# 3 900
# 4 8991
# 5 89586
# 6 888570
# 7 8754480
# 8 85480920
# 9 825234480


# l = [a,b,c,d,e,f,g,h,i,j]
# each can be a value from 0 to 3
# store count in lc[a*4^9+b*4^8+c*4^7+d*4^6+e*4^5+f*4^4+g*4^3+h*4^2+i*4+j]

N = 18

lc = [-1]*(4**10+100)

def counts(l):
    global lc
    lci = toi(l)
    if lc[lci] > 0:
        return lc[lci]
    lcn = ton(l)
    if lcn == N:
        lc[lci] == 1
        return 1
    r = 0
    for i in range(10):
        if l[i] <= 2:
            nl = l[:]
            nl[i] += 1
            r += counts(nl)
    lc[lci] = r
    return r

def toi(l):
    i = 0
    for j in l:
        i = i*4+j
    #print(i,l)
    return i

def ton(l):
    return sum(l)

def answer():
    l = [0,0,0,0,0,0,0,0,0,0]
    r = 0
    for i in range(1,10):
        nl = l[:]
        nl[i] += 1
        r += counts(nl)
    return r

print(answer()) 

print("time:",time.time()-t1)  


    
