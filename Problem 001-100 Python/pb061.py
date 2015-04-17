import math
import time

t1 = time.time()

# p8,59 > 9999
# p8,18 < 1000
gons = []
for i in range(19,59):
    o = i*(3*i-2)
    a = o//100
    b = o%100
    gons.append([[a,b],[8]])

#p7,64 > 9999
#p7,20 < 1000
for i in range(21,64):
    h = i*(5*i-3)//2
    a = h//100
    b = h%100
    gons.append([[a,b],[7]])

#p6,71 > 9999
#p6,22 < 1000
for i in range(23,71):
    h = i*(2*i-1)
    a = h//100
    b = h%100
    gons.append([[a,b],[6]])
    
#p5,82 > 9999
#p5,25 < 1000
for i in range(26,82):
    p = i*(3*i-1)//2
    a = p//100
    b = p%100
    gons.append([[a,b],[5]])

#p4,100 > 9999
#p4,31 < 1000
for i in range(32,100):
    s = i*i
    a = s//100
    b = s%100
    gons.append([[a,b],[4]])

#p3,141 > 9999
#p3,44 < 1000
for i in range(45,141):
    t = i*(i+1)//2
    a = t//100
    b = t%100
    gons.append([[a,b],[3]])

l = len(gons)

def gothrough(n):
    for i in range(0,len(gons)):
        if len(gons[i][1]) == n-1:
            b = gons[i][0][-1]
            for j in range(0,l):
                if b == gons[j][0][0] and not gons[j][1][0] in gons[i][1]:
                    temp = []
                    temp.append(gons[i][0][:])
                    temp.append(gons[i][1][:])
                    temp[1].append(gons[j][1][0])
                    temp[0].append(gons[j][0][1])
                    gons.append(temp)

for i in range(2,7):
    gothrough(i)

for i in gons:
    if len(i[1]) == 6:
        if i[0][0] == i[0][-1]:
            total = 0
            for j in range(0,len(i[0])-1):
                total += i[0][j]*101
            print (total)
            break
                



print("time:",time.time()-t1)
