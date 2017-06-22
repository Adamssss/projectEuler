import math
import time

t1 = time.time()


# f(0) = 1  000
# f(1) = 1  001
# f(2) = 2  010
# f(3) = 1  011
# f(4) = 3  100 
# f(5) = 2  101
# f(6) = 3  110
# f(7) = 1  111
# f(8) = 4  1000
                  
def tobin(n):
    if n == 0:
        return [0]
    r = []
    while n != 0:
        if n%2 == 0:
            r.insert(0,0)
        else:
            r.insert(0,1)
        n = n//2
    return r

def fbin(lb):
    l = len(lb)
    if l == 1:
        return 1
    if lb[0] > 0:
        if lb[1] == 0:
            return fbin(lb[1:])+fbin([2]+lb[2:])
        else:
            for i in range(2,l):
                if lb[i] == 2:
                    break
                if lb[i] == 0:
                    return fbin(lb[1:])+fbin([2]+lb[i+1:])
    return fbin(lb[1:])

def f(n):
    return fn(n)
    if n == 0:
        return 1
    return fbin(tobin(n))

N = 10000000
ns = [0]*N
ns[0] = 1
ns[1] = 1
ns[2] = 2
ns[3] = 1


def fn(n):
    global ns
    if n < N:
        if ns[n] > 0:
            return ns[n]
    d = 1
    while d <=n:
        d *= 2
    d = d//2
    r = 0
    nn = n-d
    r += fn(nn)
    d = d//2
    if nn >= d:
        nn -= d
        d = d//2
        while nn >= d and d > 0:
            nn -= d
            d = d//2
        r += fn(nn+d)
    elif d > 0:
        r += fn(nn+d)
    #print(n,r)
    if n < N:
        ns[n] = r
    return r

n = 25
a = f(5**n) 
b = f(2*(5**n))
#print(a,b)
print((b-a)*n+a)

print("time:",time.time()-t1)  


    
