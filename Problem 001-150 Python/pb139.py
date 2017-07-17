import math
import time

t1 = time.time()

# a^2+b^2 = c^2
# (m^2-n^2)^2+(2mn)^2 = (m^2+n^2)^2

N = 100000000

count = 0

def check(a,b,c):
    d = abs(a-b)
    if c%d == 0:
        #print(a,b,c)
        return True
    return False

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

ml = math.floor(math.sqrt(N/2))+2
for m in range(2,ml):
    for n in range(1,m):
        mm = m*m
        nn = n*n
        bs = 2*m*n
        ps = 2*mm+bs
        p = ps
        a = mm-nn
        b = bs
        if gcd(a,b) == 1:
            c = mm+nn
            t = False
            #print(a,b,c)
            if p <= N:
                t = check(a,b,c)
            if t:
                count += N//p

print(count)

print("time:",time.time()-t1)
    
