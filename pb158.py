import math
import time

t1 = time.time()

# p(2) = (25+1)*25/2

# p(n) with l[i+1] > l[i]
# n leters with 0,1,...i decreasing
# i+1,i+2,...n-1 decreasing

fac = [1]*27
for i in range(2,27):
    fac[i] = fac[i-1]*i

def p(n):
    r = 0
    for i in range(1,n):
        for j in range(1,27):
            for k in range(1,j):
                for f in range(0,27-j):
                    c = fac[26-j]//fac[f]//fac[26-j-f]
                    if j-k-i+f >= 0 and j+f-n >= 0:
                        b = fac[j-1-k]//fac[i-1-f]//fac[j-k-i+f]
                        a = fac[j-1-i+f]//fac[n-i-1]//fac[j+f-n]
                        r += a*b*c
    return r

b = 0
for i in range(2,26):
    t = p(i)
    #print(i,t)
    if t > b:
        b = t

print(b)

print("time:",time.time()-t1)  


    
