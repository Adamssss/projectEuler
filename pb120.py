import math
import time

t1 = time.time()

# a-1  = -1 mod a
# a+1  = 1 mod a
# if n = 2k+1
# r  = 0 mod a
# if n = 2k
# (-2a+1)^k + (2a+1)^k
# 1+1 = 2 mod a^2

# so n != 2k

# r max = a*a-a
# r = (a-1)^n+(a+1)^n   n is odd
# = na-1+na+1   mod a^2 (binary series)
# = 2*n*a
# 2*n  = -1 mod a
# when a is odd
# 2*n  = -2 mod a
# when a is even


# so for a is odd
# r max = a*(a-1)
# for a is even
# r max = a*(a-2)

def rmax(a):
    if a%2 == 0:
        return a*(a-2)
    return a*(a-1)

total = 0
for i in range(3,1001):
    total += rmax(i)

print(total)

print("time:",time.time()-t1)  


    
