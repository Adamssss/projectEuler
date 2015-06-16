import math
import time

t1 = time.time()

def isSquare(n):
    r = math.sqrt(n)
    return r == int(r)

# x+y+z = n
# x>y>z>0

# x+y = a
# x-y = b
# x+z = c
# x-z = d
# y+z = e
# y-z = f

# x = (a+b)/2 = (c+d)/2
# y = (a-b)/2 = (e+f)/2
# z = (c-d)/2 = (e-f)/2

# a>c>e
# b = x-y = x+z-y-z = c-e
# d = x-z = x+y-z-y = a-e
# f = y-z = y+x-z-x = a-c

Solved = False

ar = 6
while not Solved:
    a = ar*ar
    cr = 5
    while not Solved:
        c = cr*cr
        f = a-c
        if isSquare(f):
            er = 3
            while not Solved:
                e = er*er
                b = c-e
                d = a-e
                if c > d and (a+b)%2 == 0 and isSquare(b) and isSquare(d):
                    Solved = True
                    #print((a+b)/2,(a-b)/2,(c-d)/2)
                er += 1
                if er >= cr:
                    break
        cr += 1
        if cr >= ar:
            break
    ar += 1

print((a+c+e)//2)
        
print("time:",time.time()-t1)  


    
