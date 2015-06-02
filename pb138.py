import math
import time

t1 = time.time()

# h^2+(b/2)^2 = L^2
# h ~= b
# m^2-n^2,2*m*n

# 15 8          4,1
# 273 136       17,4
# 4895 2448     72,17
# 87841 43920   305,72
# 1576239 788120    1292,305

# 17 = 4*4+1
# 72 = 17*4+4
# 305 = 72*4+17
# 1292 = 305*4+72

'''
N = 10000000

def check(a,b):
    if a > b:
        h = a
    else:
        h = b
        b = a
    if abs(h-b*2) == 1:
        print(h,b)
        return True
    return False

total = 0

ml = math.floor(math.sqrt(N/2))+2
for m in range(2,ml):
    for n in range(1,m):
        if (m+n)%2 == 1:
            mm = m*m
            nn = n*n
            a = mm-nn
            b = 2*m*n
            if check(a,b):
                total += mm+nn
'''

tset = [[15,8,17]]

m = 4
n = 1
while True:
    tm = m*4+n
    n = m
    m = tm
    a = m*m-n*n
    b = 2*m*n
    c = m*m+n*n
    tset.append([a,b,c])
    if len(tset) == 12:
        break

total = 0
for i in tset:
    #print(i)
    total += i[2]    

print(total)

print("time:",time.time()-t1)
    
