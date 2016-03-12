import math
import time
t1 = time.time()

# 4,3 = 258
# 3,2 = 90
# 2,2 = 2
# 2,1 = 31
# 1,1 = 1
# 1,0 = 16

# length i with j required
# start with else:
#    (16-j)*(i-1,j)
# start with one of j
#    j*(i-1,j-1)
def foo(i,j):
    if j > i:
        # not possible
        return 0
    if i == 1 and j == 1:
        # only that number
        return 1
    if j == 0:
        # whatever
        return int(math.pow(16,i))
    # dynamic programming
    return (16-j)*foo(i-1,j)+j*foo(i-1,j-1)

def lc(i):
    # not starting with 0
    return foo(i,3)-foo(i-1,2)

def tlc(i):
    total = 0
    for j in range(3,i+1):
        total += lc(j)
    return total

print(hex(tlc(16))[2:].upper())

print("time:",time.time()-t1)  


    
