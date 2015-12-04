import math
import time

t1 = time.time()

# C(n,k):
# n!/k!/(n-k)!

N = 1000000000
# return how many factor 7
def c7(n):
    t = 0
    on = n
    while n > 1:
        n = n//7
        t += n
    return t


# line i = 7k+a
# count line i = (a+1)*cl(7k)
# line i = 7k
# count line i = cl(k)

def cl(n):
    if n == 0:
        return 1
    return cl(n//7)*(n%7+1)  

# S of lines from a0,a1,a2....
# a0 = 0
def Scl(an):
    q = an//7
    r = an%7
    if q == 0:
        return r*(1+r)//2
    return Scl(q)*28+cl(an-r)*r*(1+r)//2
'''
count = 0
for i in range(0,N,7):
    c = cl(i)
    #print(i,c)
    d = N-i
    if d > 7:
        count += c*28
    else:
        count += c*(1+d)*d//2

print(count)
'''
print(Scl(N))

print("time:",time.time()-t1)  


    
