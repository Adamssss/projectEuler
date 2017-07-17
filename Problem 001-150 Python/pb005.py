import time

t1 = time.time()

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

N = 20
lcm = 1
i = 1
while i < N:
    lcm = lcm * i / gcd(lcm,i)
    i = i+1

print (lcm)

print("time:",time.time()-t1)
