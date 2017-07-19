import math
import time

t1 = time.time()

# a^2+b^2 = c^2
# a = 2xy
# b = x^2-y^2
# c = x^2+y^2

# c = z^2
# x^2+y^2 = z^2
# x = 2pq
# y = p^2-q^2
# z = p^2+q^2

# *gcd(p,q) = 1
# a*b/2 % 84 != 0
# p^4+q^4 +2p^2q^2 <= 10^16

def gcd(x,y):
    if x < y:
        temp = x
        x = y
        y = temp
    while y > 0:
        temp = x%y
        x = y
        y = temp

    return x

N = 10**16
result = 0
pb = math.ceil(math.sqrt(math.sqrt(N)))+1
for p in range(1,pb):
    qb = math.ceil(math.sqrt(math.sqrt(N)))+1
    for q in range(p+1,qb):
        if gcd(p,q) != 1:
            continue
        x = 2*p*q
        y = q*q-p*p
        c = x*x+y*y
        if c > N:
            break
        a = 2*x*y
        b = abs(x*x-y*y)
        if (a*b//2) % 84 > 0:
            result += 1

print(result)
# 0!!!!!!!!!!!!!!        
        




print("time:",time.time()-t1)  





