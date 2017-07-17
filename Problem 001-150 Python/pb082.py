import math
import time

t1 = time.time()

# read the matrix into a 2D list
f = open('pb082_matrix.txt','r')

mr= f.read().split('\n')

f.close()
'''
mr[0] = '131,673,234,103,18'
mr[1] = '201,96,342,965,150'
mr[2] = '630,803,746,422,111'
mr[3] = '537,699,497,121,956'
mr[4] = '805,732,524,37,331'
'''
L = 80
        
mc = []

for i in range(0,L):
    mc.append(mr[i].split(','))

m = []
for i in range(L):
    m.append([0]*L)

for i in range(0,L):
    for j in range(0,L):
        temp = 0
        for d in mc[i][j]:
            temp = temp*10+ord(d)-48
        m[i][j] += temp

pv = []
for i in range(L):
    pv.append([0]*L)

def minp(a,b):
    if b == 0:
        return m[a][b]
    
    if a == 0:
        low = pv[a][b-1]
        temp = low
        for i in range(1,L):
            temp = temp-pv[i-1][b-1]+pv[i][b-1]+m[i][b]
            if temp < low:
                low = temp
        return low+m[a][b]
    
    low = pv[a][b-1]
    temp = low
    for i in range(a+1,L):
        temp = temp-pv[i-1][b-1]+pv[i][b-1]+m[i][b]
        if temp < low:
            low = temp
    if low > pv[a-1][b]:
        low = pv[a-1][b]
    return low+m[a][b]
    
for j in range(0,L):
    for i in range(0,L):
        pv[i][j] = minp(i,j)

minpath = math.pow(10,10)
for i in range(0,L):
    if pv[i][-1] < minpath:
        minpath = pv[i][-1]

print(minpath)

print("time:",time.time()-t1)
    
