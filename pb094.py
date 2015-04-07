import math
import time

t1 = time.time()

N = 1000000000

# a,a,a+1 triangle
# h = sqrt(a^2-((a+1)/2)^2)
# s = (1+a)/4*sqrt(3a^2-2a-1)
# 3a^2-2a-1 must be square
# a != 3k or 2k
# a mod 6 = 1 or 5
def tap1(n):
    r = n%6
    if r != 1 and r != 5:
        return 0
    temp = 3*n*n-2*n-1
    if not isSquare(temp):
        return 0
    return 3*n+1

# a,a,a-1 triangle
# h = sqrt(a^2-((a-1)/2)^2)
# s = (a-1)/4*sqrt(3a^2+2a-1)
# 3a^2+2a-1 must be square
# a != 3k or 2k
# a mod 6 = 1 or 5
def tam1(n):
    r = n%6
    if r != 1 and r != 5:
        return 0
    temp = 3*n*n+2*n-1
    if not isSquare(temp):
        return 0
    return 3*n-1

def isSquare(n):
    r = math.floor(math.sqrt(n))
    if n-r*r == 0:
        return True
    return False

n = N//3

count = 0

for i in range(2,n+1):
    count += tap1(i)
    count += tam1(i)

print(count)

print("time:",time.time()-t1)
# time: 569.6165800094604   


    
