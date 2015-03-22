import time

t1 = time.time()

# read the matrix into a 2D list
f = open('pb081_matrix.txt','r')

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

pv = [[0]*L]*L

def minp(a,b):
    if a == 0 and b == 0:
        return m[0][0]
    if a == 0:
        return pv[0][b-1]+m[0][b]
    if b == 0:
        return pv[a-1][0]+m[a][0]
    if pv[a-1][b] > pv[a][b-1]:
        return pv[a][b-1]+m[a][b]
    return pv[a-1][b]+m[a][b]
    
for i in range(0,L):
    for j in range(0,L):
        pv[i][j] = minp(i,j)

print(pv[-1][-1])



print("time:",time.time()-t1)
    
