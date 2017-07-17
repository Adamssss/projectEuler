import math
import time

t1 = time.time()


#https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem
# z(1) = 1
# z(2) = 1
# z(3) = 1
# z(4) = 1(3)+z(1) = 2
# z(5) = 1
# z(6) = 1(5)+z(1) = 2
# z(7) = 1(5)+z(2) = 2
# z(8) = 1
# z(9) = 1(8)+z(1) = 2
# z(10) = 1(8)+z(2) = 2
# z(11) = 1(8)+z(3) = 2
# z(12) = 1(8)+z(4) = 3
# z(13) = 1


N = 10**17

fab = [1,1,2]
f = 0
while f < N:
    f = fab[-1]+fab[-2]
    fab.append(f)

def sz(n):
    r = 0
    for i in range(1,n):
        r += z(i)
    return r

def z(n):
    i = 1
    if n == fab[i]:
        return 1
    while True:
        i += 1
        if fab[i] == n:
            return 1
        if fab[i] > n:
            return 1+z(n-fab[i-1])


# sz(fi) = fi-f(i-1)+2*sz(f(i-1))
def szf(f):
    if f <= 3:
        return f
    return szf(f-2)-1+szf(f-1)+fab[f]-fab[f-1]

def szl(n):
    if n <= 3:
        return n-1
    i = 3
    while True:
        i += 1
        if fab[i] == n:
            return szf(i)-1
        if fab[i] > n:
            return szl(n-fab[i-1])+n-fab[i-1]-1+szf(i-1)


nszf = [0,1,2,3]
i = 3
while True:
    i += 1
    if fab[i] > N:
        break
    t = nszf[i-2]-1+nszf[i-1]+fab[i]-fab[i-1]
    nszf.append(t)
    
def nsz(n):
    if n <= 3:
        return n-1
    i = 3
    while True:
        i += 1
        if fab[i] == n:
            return nszf[i]-1
        if fab[i] > n:
            return nsz(n-fab[i-1])+n-fab[i-1]-1+nszf[i-1]





#print(len(fab))

        
#print(sz(N))
#print(szl(N))
print(nsz(N))

print("time:",time.time()-t1)  


    
