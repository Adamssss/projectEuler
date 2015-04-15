import math
import time

t1 = time.time()

N = 12000

nk = [0,0,4]

for i in range(3,N+1):
    nk.append(2*i)

def product(lst):
    result = 1
    for i in lst:
        result *= i
    return result

ul = N*2

pc = []
tc = [3,3]
tl = 2
td = 1

while math.pow(2,tl) <= ul:
    if product(tc) > ul:
        while td > 0 and tc[td] == tc[td-1]:
            td -= 1
        if td == 0:
            tl += 1
            td = tl-1
            tc = [2]*tl
            continue
        tc[td-1] += 1
        for i in range(td,tl):
            tc[i] = tc[td-1]
        td = tl-1
        continue
    pc.append(tc[:])
    tc[td] += 1
        
for i in pc:
    n = product(i)
    k = len(i)+n-sum(i)
    if k > N:
        continue
    if nk[k] > n:
        nk[k] = n

ns = []

total = 0

for i in nk:
    if not i in ns:
        total += i
        ns.append(i)

print(total)

print("time:",time.time()-t1)  


    
