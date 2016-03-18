import math
import time

t1 = time.time()

# m = 2
# P = 2/3*(4/3)^2
# 2/3:4/3 = 1:2

# ln(p) = ln(x1)+2ln(x2)+...+mln(xm)
# assume (x2...m) = (m-x1)/(m-1)
# 1/x1 = (m-1)*(2+..+m)/(m-x1)*-1/(m-1)
# x1 = m/(1+2+..+m)

def P(m):
    t = (1+m)*m/2
    r = 1
    for i in range(1,m+1):
        r *= math.pow(i*m/t,i)
    return r

t = 0
for i in range(2,16):
    t += math.floor(P(i))

print(t)

print("time:",time.time()-t1)  


    
