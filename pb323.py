import math
import time

t1 = time.time()

# 32 slots starts with 0 with 50% chance to became 1
# 1 turn is to go through all the slots

# from a zeros to b zeros
# select b to be still zero in a
# P = C(a,b)*0.5^a

# pzeros
pz = [0]*33
# starting with 32 zeros
# chance is 100%
pz[32] = 1

# factorial
def f(n):
    if n == 0:
        return 1
    return n*f(n-1)

# select b from a
def c(a,b):
    return f(a)//f(b)//f(a-b)


def p(a,b):
    return c(a,b)*math.pow(0.5,a)


e = 0
for i in range(1,100):
    npz = [0]*33
    for j in range(1,33):
        e += pz[j]*p(j,0)*i
        for k in range(1,j+1):
            npz[k] += pz[j]*p(j,k)
    pz = npz[:]

    #print(i,e)

print(round(e*(10**10))/(10**10))


print("time:",time.time()-t1)  





