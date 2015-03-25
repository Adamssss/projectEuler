import math
import time

t1 = time.time()

# read the matrix into a 2D list
f = open('pb083_matrix.txt','r')

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
mc = []
for i in range(L):
    pv.append([999999]*L)
    mc.append([False]*L)

i = 0
j = 0
while j < L:
    #for t in pv:
        #print(t)
    #print('==============================')
    if mc[i][j]:
        if j != 0:
            if pv[i][j] + m[i][j-1] < pv[i][j-1]:
                pv[i][j-1] = pv[i][j] + m[i][j-1]
                mc[i][j-1] = True
                j -= 1
                continue
        if i != 0:
            if pv[i][j] + m[i-1][j] < pv[i-1][j]:
                pv[i-1][j] = pv[i][j] + m[i-1][j]
                mc[i-1][j] = True
                i -= 1
                continue
    if j == 0:
        if i == 0:
            pv[i][j] = m[i][j]
        else:
            temp = m[i][j] + pv[i-1][j]
            if temp < pv[i][j]:
                pv[i][j] = temp
                mc[i][j] = True
                continue
    else:
        if i == 0:
            temp = m[i][j] + pv[i][j-1]
            if temp < pv[i][j]:
                pv[i][j] = temp
                mc[i][j] = True
                continue
        else:
            if pv[i-1][j] > pv[i][j-1]:
                temp = pv[i][j-1]
            else:
                temp = pv[i-1][j]
            temp += m[i][j]
            if temp < pv[i][j]:
                pv[i][j] = temp
                mc[i][j] = True
                continue

    i += 1
    if i == L:
        i = 0
        j += 1

print(pv[-1][-1])

print("time:",time.time()-t1)
    
