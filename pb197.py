import math
import time

t1 = time.time()

def f(x):
    return math.floor(math.pow(2,30.403243784-x*x))/math.pow(10,9)

'''
a = -1
for i in range(2000):
    a = f(a)
    print(a)
'''

# E a,b that satisfy
# a = f(b)
# b = f(a)

N = int(math.pow(10,12))
t = [0,0]
fp = True
a = -1
for i in range(N):
    a = f(a)
    if fp:
        if t[0] == a:
            break
        t[0] = a
    else:
        if t[1] == a:
            break
        t[1] = a
    fp = not fp

print(sum(t))

print("time:",time.time()-t1)  


    
