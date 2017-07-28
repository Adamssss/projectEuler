import math
import time

t1 = time.time()


a = 1

Lsectionarea = (a*a-math.pi*a*a/4)/4

#print(Lsectionarea)


def areaof(n):
    # (a/2-x)^2+(a/2-x/n)^2 = (a/2)^2
    # a^2/4-ax+x^2+a^2/4-ax/n+x^2/n^2 = a^2/4
    # x^2*(1+1/n^2)+x*(-a-a/n)+a^2/4 = 0
    p = 1+1/n/n
    q = -a-a/n
    r = a*a/4
    x = (-q-math.sqrt(q*q-4*p*r))/(2*p)
    area = 0
    area += x*x/n/2
    area += (x/n+a/2)*(a/2-x)/2
    theta = math.asin((a/2-x)/(a/2))
    area -= (a*a/4*theta/2)
    return area
    


def areaper(n):
    return areaof(n)/Lsectionarea*100

def example():
    print(areaper(1))
    print(areaper(2))

#example()

def answer():
    r = 1
    while True:
        t = areaper(r)
        if t < 0.1:
            return r
        r += 1


print(answer())

print("time:",time.time()-t1)  





