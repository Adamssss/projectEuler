import math

# n(3n-1)/2
def isPentagon(item):
    num = math.floor(math.sqrt(item*2//3))+1
    if num*(3*num-1)//2 == item:
        return True
    return False

# n(2n-1)
def isHexagon(item):
    num = math.floor(math.sqrt(item//2))+1
    if num*(2*num-1) == item:
        return True
    return False


i = 285
t = 0
while t == 0:
    i += 1
    n = i*(i+1)//2
    if isPentagon(n) and isHexagon(n):
        t = 1
        print (n)
